"""JSON file CRUD operations for all data stores.

Mirrors the metadata.py pattern from the existing repos, using Pydantic
models for serialization and UTF-8 with indent=2 for consistent formatting.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

from src.config import FailedPost, PendingFeature, Project, ReviewMatch

logger = logging.getLogger("telegram-sync")

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data"

APPS_DB = DATA_DIR / "apps.json"
PENDING_DB = DATA_DIR / "pending-features.json"
REVIEW_DB = DATA_DIR / "review-required.json"
FAILED_DB = DATA_DIR / "failed-posts.json"
PROCESSED_DB = DATA_DIR / "processed-messages.json"


def _ensure_data_dir() -> None:
    """Create the data directory if it doesn't exist."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def _read_json(path: Path) -> Any:
    """Read and parse a JSON file, returning an empty structure on failure."""
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        logger.warning("Could not read %s: %s", path.name, exc)
        return None


def _write_json(path: Path, data: Any) -> None:
    """Write data to a JSON file with consistent formatting."""
    _ensure_data_dir()
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


# ---------------------------------------------------------------------------
# apps.json — main project database
# ---------------------------------------------------------------------------


def load_apps() -> list[Project]:
    """Load all projects from apps.json.

    Returns:
        List of Project objects, sorted by created_at descending (newest first).
    """
    _ensure_data_dir()
    raw = _read_json(APPS_DB)
    if not raw or not isinstance(raw, list):
        return []
    projects = []
    for item in raw:
        try:
            projects.append(Project(**item))
        except Exception as exc:
            logger.warning("Skipping malformed project entry: %s", exc)
    return projects


def save_apps(projects: list[Project]) -> None:
    """Save all projects to apps.json, sorted by created_at descending."""
    sorted_projects = sorted(
        projects,
        key=lambda p: p.created_at,
        reverse=True,
    )
    _write_json(APPS_DB, [p.model_dump() for p in sorted_projects])


# ---------------------------------------------------------------------------
# pending-features.json — unmatched features
# ---------------------------------------------------------------------------


def load_pending_features() -> list[PendingFeature]:
    """Load pending features awaiting project match."""
    _ensure_data_dir()
    raw = _read_json(PENDING_DB)
    if not raw or not isinstance(raw, list):
        return []
    pending = []
    for item in raw:
        try:
            pending.append(PendingFeature(**item))
        except Exception as exc:
            logger.warning("Skipping malformed pending feature: %s", exc)
    return pending


def save_pending_features(pending: list[PendingFeature]) -> None:
    """Save pending features to JSON."""
    _write_json(PENDING_DB, [p.model_dump() for p in pending])


# ---------------------------------------------------------------------------
# review-required.json — uncertain matches
# ---------------------------------------------------------------------------


def load_review_required() -> list[ReviewMatch]:
    """Load matches that need manual review."""
    _ensure_data_dir()
    raw = _read_json(REVIEW_DB)
    if not raw or not isinstance(raw, list):
        return []
    reviews = []
    for item in raw:
        try:
            reviews.append(ReviewMatch(**item))
        except Exception as exc:
            logger.warning("Skipping malformed review entry: %s", exc)
    return reviews


def save_review_required(reviews: list[ReviewMatch]) -> None:
    """Save review-required matches to JSON."""
    _write_json(REVIEW_DB, [r.model_dump() for r in reviews])


# ---------------------------------------------------------------------------
# failed-posts.json — posts that failed parsing
# ---------------------------------------------------------------------------


def load_failed_posts() -> list[FailedPost]:
    """Load failed post records."""
    _ensure_data_dir()
    raw = _read_json(FAILED_DB)
    if not raw or not isinstance(raw, list):
        return []
    failed = []
    for item in raw:
        try:
            failed.append(FailedPost(**item))
        except Exception as exc:
            logger.warning("Skipping malformed failed post: %s", exc)
    return failed


def save_failed_posts(failed: list[FailedPost]) -> None:
    """Save failed post records to JSON."""
    _write_json(FAILED_DB, [f.model_dump() for f in failed])


# ---------------------------------------------------------------------------
# processed-messages.json — last processed message IDs
# ---------------------------------------------------------------------------


def load_processed_messages() -> dict[str, int]:
    """Load last processed message IDs per channel.

    Returns:
        Dict mapping channel username to last processed message ID.
        Example: {"popMODS": 12345, "popCLOUDS": 13548}
    """
    _ensure_data_dir()
    raw = _read_json(PROCESSED_DB)
    if not raw or not isinstance(raw, dict):
        return {}
    return {k: int(v) for k, v in raw.items()}


def save_processed_messages(processed: dict[str, int]) -> None:
    """Save last processed message IDs per channel."""
    _write_json(PROCESSED_DB, processed)
