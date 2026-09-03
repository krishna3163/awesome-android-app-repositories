"""Main entry point — orchestrates the complete Telegram → GitHub sync workflow.

Usage:
    python -m src.main                   # Full sync
    python -m src.main --dry-run         # Check without committing
    python -m src.main --force-resync    # Reprocess all channels from scratch
"""

from __future__ import annotations

import argparse
import asyncio
import logging
import sys

from src.config import (
    FailedPost,
    PendingFeature,
    ReviewMatch,
    Settings,
)
from src.database.merger import (
    create_project_from_parsed,
    merge_features_into_project,
    merge_pending_into_project,
)
from src.database.repository import (
    load_apps,
    load_failed_posts,
    load_pending_features,
    load_processed_messages,
    load_review_required,
    save_apps,
    save_failed_posts,
    save_pending_features,
    save_processed_messages,
    save_review_required,
)
from src.generators.readme_generator import update_readme
from src.matching.normalize import normalize_name
from src.matching.project_matcher import MatchType, find_matching_project
from src.parsers.features_parser import FeatureParseError, parse_features
from src.parsers.main_project_parser import ParseError, parse_main_project
from src.telegram.channel_monitor import fetch_new_messages
from src.telegram.client import TelegramAuthError, TelegramClient
from src.telegram.media_downloader import download_message_media
from src.utils.hashing import slugify
from src.utils.logger import setup_logging

logger = logging.getLogger("telegram-sync")


async def sync(settings: Settings, dry_run: bool = False, force_resync: bool = False) -> dict:
    """Run the complete synchronization workflow.

    Args:
        settings: Application settings.
        dry_run: If True, parse and match but don't save or commit.
        force_resync: If True, reprocess all channels from message ID 0.

    Returns:
        Dict with sync result counts.
    """
    results = {"new": 0, "updated": 0, "pending": 0, "review": 0, "failed": 0, "skipped": 0}

    # Load databases
    projects = load_apps()
    pending_features = load_pending_features()
    failed_posts = load_failed_posts()
    review_required = load_review_required()
    processed = load_processed_messages()

    if force_resync:
        processed = {}
        logger.info("[INFO] Force resync — clearing processed message IDs")

    # Connect to Telegram
    async with TelegramClient(
        settings.telegram_api_id,
        settings.telegram_api_hash,
        settings.telegram_session_string,
    ) as client:

        # ---------------------------------------------------------------
        # Phase 1: Process main project channel(s)
        # ---------------------------------------------------------------
        for channel_cfg in settings.channels:
            if channel_cfg.type != "main_project":
                continue

            channel = channel_cfg.username
            last_id = processed.get(channel, 0)

            logger.info("")
            logger.info("=" * 56)
            logger.info("[INFO] Processing main channel: @%s", channel)
            logger.info("=" * 56)

            channel_messages = await fetch_new_messages(client, channel, last_id)

            for message in channel_messages.messages:
                try:
                    parsed = parse_main_project(
                        text=message.text,
                        entities=message.entities,
                        message_id=message.id,
                        channel=channel,
                        posted_at=message.date.isoformat() if message.date else "",
                    )
                except ParseError as exc:
                    logger.warning(
                        "[WARNING] Failed to parse message %d from @%s: %s",
                        message.id, channel, exc,
                    )
                    failed_posts.append(FailedPost(
                        channel=f"@{channel}",
                        message_id=message.id,
                        error=str(exc),
                        raw_text=message.text[:500] if message.text else "",
                    ))
                    results["failed"] += 1
                    continue

                logger.info("[INFO] Parsed project: %s", parsed.name)

                # Check for duplicates
                match = find_matching_project(
                    name=parsed.name,
                    repo_url=parsed.source_code,
                    existing_projects=projects,
                    duplicate_threshold=settings.duplicate_threshold,
                    review_threshold_low=settings.review_threshold_low,
                )

                if match.match_type in (MatchType.EXACT_REPO, MatchType.EXACT_NAME, MatchType.FUZZY_HIGH):
                    # Update existing project
                    logger.info(
                        "[INFO] Match found (%s, %.0f%%): updating %s",
                        match.match_type.value, match.confidence,
                        match.project.name if match.project else match.project_id,
                    )
                    if match.project and not dry_run:
                        idx = next(
                            (i for i, p in enumerate(projects) if p.id == match.project_id),
                            None,
                        )
                        if idx is not None:
                            update_data = {
                                "description": parsed.description,
                                "website": parsed.website,
                                "repository": parsed.source_code,
                                "developer": {"name": parsed.developer_name, "url": parsed.developer_url},
                                "tags": parsed.tags,
                            }
                            from src.database.merger import merge_project
                            projects[idx] = merge_project(projects[idx], update_data)
                    results["updated"] += 1

                elif match.match_type == MatchType.FUZZY_REVIEW:
                    # Store for review
                    logger.info(
                        "[WARNING] Uncertain match (%.0f%%): %s ↔ %s — stored for review",
                        match.confidence, parsed.name,
                        match.project.name if match.project else "?",
                    )
                    review_required.append(ReviewMatch(
                        incoming_name=parsed.name,
                        incoming_normalized=normalize_name(parsed.name),
                        matched_project_id=match.project_id,
                        matched_project_name=match.project.name if match.project else "",
                        similarity_score=match.confidence,
                        channel=f"@{channel}",
                        message_id=message.id,
                        raw_text=message.text[:500] if message.text else "",
                    ))
                    results["review"] += 1

                else:
                    # New project
                    new_project = create_project_from_parsed(parsed, channel)
                    logger.info("[INFO] New project created: %s (id: %s)", new_project.name, new_project.id)

                    # Check if any pending features match
                    if not dry_run:
                        remaining_pending = []
                        for pf in pending_features:
                            pf_normalized = pf.normalized_title or normalize_name(pf.raw_title)
                            project_normalized = normalize_name(new_project.name)
                            if pf_normalized and project_normalized and pf_normalized == project_normalized:
                                logger.info(
                                    "[INFO] Merging pending features: %s → %s",
                                    pf.raw_title, new_project.name,
                                )
                                new_project = merge_pending_into_project(new_project, pf)
                            else:
                                remaining_pending.append(pf)
                        pending_features = remaining_pending

                    projects.append(new_project)
                    results["new"] += 1

            # Update last processed message ID
            if channel_messages.latest_message_id > last_id:
                processed[channel] = channel_messages.latest_message_id

        # ---------------------------------------------------------------
        # Phase 2: Process features channel(s)
        # ---------------------------------------------------------------
        for channel_cfg in settings.channels:
            if channel_cfg.type != "features":
                continue

            channel = channel_cfg.username
            last_id = processed.get(channel, 0)

            logger.info("")
            logger.info("=" * 56)
            logger.info("[INFO] Processing features channel: @%s", channel)
            logger.info("=" * 56)

            channel_messages = await fetch_new_messages(client, channel, last_id)

            for message in channel_messages.messages:
                try:
                    parsed_feat = parse_features(
                        text=message.text,
                        message_id=message.id,
                        channel=channel,
                    )
                except FeatureParseError as exc:
                    logger.warning(
                        "[WARNING] Failed to parse features message %d from @%s: %s",
                        message.id, channel, exc,
                    )
                    failed_posts.append(FailedPost(
                        channel=f"@{channel}",
                        message_id=message.id,
                        error=str(exc),
                        raw_text=message.text[:500] if message.text else "",
                    ))
                    results["failed"] += 1
                    continue

                logger.info(
                    "[INFO] Parsed features for: %s (%d features)",
                    parsed_feat.project_name_guess,
                    len(parsed_feat.features),
                )

                # Try to match to an existing project first
                match = find_matching_project(
                    name=parsed_feat.project_name_guess,
                    repo_url="",
                    existing_projects=projects,
                    duplicate_threshold=settings.duplicate_threshold,
                    review_threshold_low=settings.review_threshold_low,
                )

                # Download images using resolved project slug
                image_paths: list[str] = []
                if message.media and not dry_run:
                    target_slug = slugify(match.project_id if match.project_id else parsed_feat.project_name_guess)
                    try:
                        image_paths = await download_message_media(client, message, target_slug)
                        if image_paths:
                            logger.info("[INFO] Downloaded %d image(s)", len(image_paths))
                    except Exception as exc:
                        logger.warning("[WARNING] Failed to download media for %s: %s", target_slug, exc)

                if match.match_type in (MatchType.EXACT_REPO, MatchType.EXACT_NAME, MatchType.FUZZY_HIGH):
                    logger.info(
                        "[INFO] Matched features to project: %s (%.0f%%)",
                        match.project.name if match.project else match.project_id,
                        match.confidence,
                    )
                    if match.project and not dry_run:
                        idx = next(
                            (i for i, p in enumerate(projects) if p.id == match.project_id),
                            None,
                        )
                        if idx is not None:
                            projects[idx] = merge_features_into_project(
                                projects[idx],
                                parsed_feat,
                                image_paths=image_paths,
                                features_channel=channel,
                            )
                    results["updated"] += 1

                else:
                    # No match — store as pending
                    logger.info(
                        "[INFO] No matching project found for '%s' — storing as pending",
                        parsed_feat.project_name_guess,
                    )
                    if not dry_run:
                        pending_features.append(PendingFeature(
                            raw_title=parsed_feat.raw_title,
                            normalized_title=normalize_name(parsed_feat.project_name_guess),
                            features=parsed_feat.features,
                            image_paths=image_paths,
                            channel=channel,
                            message_id=message.id,
                        ))
                    results["pending"] += 1

            # Update last processed message ID
            if channel_messages.latest_message_id > last_id:
                processed[channel] = channel_messages.latest_message_id

    # ---------------------------------------------------------------
    # Phase 3: Save and generate
    # ---------------------------------------------------------------
    if not dry_run:
        save_apps(projects)
        save_pending_features(pending_features)
        save_failed_posts(failed_posts)
        save_review_required(review_required)
        save_processed_messages(processed)
        logger.info("")
        logger.info("[INFO] 💾 All data saved")

        readme_changed = update_readme(projects)
        if readme_changed:
            logger.info("[INFO] 📝 README.md updated")

    return results


def main() -> int:
    """CLI entry point."""
    setup_logging()

    parser = argparse.ArgumentParser(
        description="Telegram → GitHub App Repository Sync"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Parse and match without saving or committing",
    )
    parser.add_argument(
        "--force-resync",
        action="store_true",
        help="Reprocess all channels from the beginning",
    )
    args = parser.parse_args()

    logger.info("")
    logger.info("🚀 Telegram → GitHub App Repository Sync")
    logger.info("=" * 56)
    if args.dry_run:
        logger.info("🔍 DRY RUN MODE — no changes will be saved")
    logger.info("")

    try:
        settings = Settings()
    except Exception as exc:
        logger.error("[ERROR] Failed to load settings: %s", exc)
        logger.error("[ERROR] Make sure .env file exists or environment variables are set")
        return 1

    if not settings.telegram_api_id or not settings.telegram_api_hash:
        logger.error("[ERROR] TELEGRAM_API_ID and TELEGRAM_API_HASH are required")
        return 1

    if not settings.telegram_session_string:
        logger.warning("::warning title=Missing Telegram Session::TELEGRAM_SESSION_STRING is not set.")
        logger.warning("[WARNING] TELEGRAM_SESSION_STRING is required. Skipping sync to avoid recurring failure alerts.")
        logger.warning("[WARNING] Generate one with: python scripts/request_code.py")
        return 0

    # Run the async sync
    try:
        results = asyncio.run(sync(settings, dry_run=args.dry_run, force_resync=args.force_resync))
    except TelegramAuthError as exc:
        logger.warning("::warning title=Telegram Session Expired::%s", exc)
        logger.warning("")
        logger.warning("=" * 56)
        logger.warning("[WARNING] Telegram session is unauthorized or expired: %s", exc)
        logger.warning("[WARNING] Sync skipped gracefully to prevent recurring CI failure emails.")
        logger.warning("[WARNING] Please re-authenticate using scripts/request_code.py and update your secret.")
        logger.warning("=" * 56)
        return 0
    except Exception as exc:
        logger.error("[ERROR] Sync failed: %s", exc)
        return 1

    # Print summary
    logger.info("")
    logger.info("=" * 56)
    logger.info("SYNC SUMMARY")
    logger.info("=" * 56)
    logger.info("New projects:        %d", results.get("new", 0))
    logger.info("Updated projects:    %d", results.get("updated", 0))
    logger.info("Pending features:    %d", results.get("pending", 0))
    logger.info("Needs review:        %d", results.get("review", 0))
    logger.info("Failed:              %d", results.get("failed", 0))
    logger.info("=" * 56)

    return 0


if __name__ == "__main__":
    sys.exit(main())
