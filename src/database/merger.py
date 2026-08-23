"""Smart merge logic for combining project data across channels.

Core principle: never overwrite existing valid data with null, empty string,
or empty list. Only fill in missing fields or append to lists.
"""

from __future__ import annotations

from datetime import UTC, datetime

from src.config import (
    Developer,
    ParsedFeatures,
    ParsedProject,
    PendingFeature,
    Project,
    TelegramSource,
)
from src.utils.hashing import slugify
from src.utils.logger import get_logger

logger = get_logger()


def create_project_from_parsed(
    parsed: ParsedProject,
    channel: str = "",
) -> Project:
    """Create a new Project from a ParsedProject (main channel post).

    Args:
        parsed: The parsed project data.
        channel: The source channel username.

    Returns:
        A new Project instance with all available fields populated.
    """
    now = datetime.now(UTC).isoformat()
    project_id = slugify(parsed.name)

    return Project(
        id=project_id,
        name=parsed.name,
        description=parsed.description,
        website=parsed.website,
        repository=parsed.source_code,
        developer=Developer(
            name=parsed.developer_name,
            url=parsed.developer_url,
        ),
        tags=parsed.tags,
        telegram=TelegramSource(
            main_channel=f"@{channel}" if channel else "",
            main_message_id=parsed.telegram_message_id,
        ),
        created_at=parsed.posted_at or now,
        updated_at=now,
    )


def merge_project(existing: Project, new_data: dict) -> Project:
    """Merge new data into an existing project without overwriting valid fields.

    Only updates fields that are currently empty/null/[] in the existing project
    and non-empty in new_data.

    Args:
        existing: The existing project to update.
        new_data: Dict of new field values to potentially merge.

    Returns:
        A new Project instance with merged data.
    """
    data = existing.model_dump()
    now = datetime.now(UTC).isoformat()

    for key, new_value in new_data.items():
        if key in ("id", "created_at"):
            continue  # Never change ID or creation timestamp

        if not _is_meaningful(new_value):
            continue  # Don't overwrite with empty values

        current_value = data.get(key)

        if not _is_meaningful(current_value):
            # Current value is empty — fill it in
            data[key] = new_value
        elif key == "features" and isinstance(new_value, list):
            # Append new features that don't already exist
            data[key] = _merge_features(current_value, new_value)
        elif key == "tags" and isinstance(new_value, list):
            # Merge tags, deduplicate
            data[key] = _merge_tags(current_value, new_value)
        elif key == "images" and isinstance(new_value, dict):
            # Merge image sets
            data[key] = _merge_images(current_value, new_value)

    data["updated_at"] = now
    return Project(**data)


def merge_features_into_project(
    project: Project,
    parsed_features: ParsedFeatures,
    image_paths: list[str] | None = None,
    features_channel: str = "",
) -> Project:
    """Merge feature data and images from a features channel post into a project.

    Args:
        project: The existing project.
        parsed_features: The parsed features data.
        image_paths: Optional list of downloaded image paths.
        features_channel: The features channel username.

    Returns:
        An updated Project with merged features and images.
    """
    now = datetime.now(UTC).isoformat()
    data = project.model_dump()

    # Merge features
    existing_features = data.get("features", [])
    new_features = [f.model_dump() for f in parsed_features.features]
    data["features"] = _merge_features(existing_features, new_features)

    # Merge images
    if image_paths:
        existing_images = data.get("images", {})
        if not existing_images.get("cover") and image_paths:
            existing_images["cover"] = image_paths[0]
        screenshots = existing_images.get("screenshots", [])
        for path in image_paths[1:]:
            if path not in screenshots:
                screenshots.append(path)
        existing_images["screenshots"] = screenshots
        data["images"] = existing_images

    # Update telegram source
    telegram = data.get("telegram", {})
    if features_channel:
        telegram["features_channel"] = f"@{features_channel}"
    if parsed_features.message_id is not None:
        telegram["features_message_id"] = parsed_features.message_id
    data["telegram"] = telegram

    data["updated_at"] = now
    return Project(**data)


def merge_pending_into_project(
    project: Project,
    pending: PendingFeature,
) -> Project:
    """Merge a pending feature post into a newly arrived project.

    Args:
        project: The newly created project.
        pending: The pending feature data that was waiting.

    Returns:
        An updated Project with the pending features and images merged in.
    """
    now = datetime.now(UTC).isoformat()
    data = project.model_dump()

    # Merge features
    existing_features = data.get("features", [])
    new_features = [f.model_dump() for f in pending.features]
    data["features"] = _merge_features(existing_features, new_features)

    # Merge images from pending
    if pending.image_paths:
        existing_images = data.get("images", {})
        if not existing_images.get("cover") and pending.image_paths:
            existing_images["cover"] = pending.image_paths[0]
        screenshots = existing_images.get("screenshots", [])
        for path in pending.image_paths[1:]:
            if path not in screenshots:
                screenshots.append(path)
        existing_images["screenshots"] = screenshots
        data["images"] = existing_images

    # Update telegram source
    telegram = data.get("telegram", {})
    if pending.channel:
        telegram["features_channel"] = f"@{pending.channel}"
    if pending.message_id is not None:
        telegram["features_message_id"] = pending.message_id
    data["telegram"] = telegram

    data["updated_at"] = now
    return Project(**data)


# ---------------------------------------------------------------------------
# Private helpers
# ---------------------------------------------------------------------------


def _is_meaningful(value: object) -> bool:
    """Check if a value is non-empty and meaningful."""
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, list):
        return len(value) > 0
    if isinstance(value, dict):
        return any(_is_meaningful(v) for v in value.values())
    return True


def _merge_features(existing: list[dict], new: list[dict]) -> list[dict]:
    """Merge feature lists, avoiding duplicates by title."""
    existing_titles = {f.get("title", "").lower() for f in existing}
    merged = list(existing)
    for feature in new:
        title = feature.get("title", "").lower()
        if title and title not in existing_titles:
            merged.append(feature)
            existing_titles.add(title)
    return merged


def _merge_tags(existing: list[str], new: list[str]) -> list[str]:
    """Merge tag lists, deduplicating case-insensitively."""
    seen = {t.lower() for t in existing}
    merged = list(existing)
    for tag in new:
        lower = tag.lower()
        if lower not in seen:
            merged.append(tag)
            seen.add(lower)
    return merged


def _merge_images(existing: dict, new: dict) -> dict:
    """Merge image sets."""
    result = dict(existing)
    if not result.get("cover") and new.get("cover"):
        result["cover"] = new["cover"]
    existing_screenshots = result.get("screenshots", [])
    new_screenshots = new.get("screenshots", [])
    for s in new_screenshots:
        if s not in existing_screenshots:
            existing_screenshots.append(s)
    result["screenshots"] = existing_screenshots
    return result
