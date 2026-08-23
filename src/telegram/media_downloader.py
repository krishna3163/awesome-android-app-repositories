"""Download images and media from Telegram messages.

Saves media to assets/apps/<slug>/ with deterministic filenames.
Supports JPEG, PNG, and WebP images.
"""

from __future__ import annotations

import logging
from pathlib import Path

from telethon.tl.types import Message, MessageMediaDocument, MessageMediaPhoto

from src.telegram.client import TelegramClient
from src.utils.hashing import deterministic_filename

logger = logging.getLogger("telegram-sync")

ROOT = Path(__file__).resolve().parents[2]
ASSETS_DIR = ROOT / "assets" / "apps"

# Supported image MIME types
_IMAGE_MIMES = {"image/jpeg", "image/png", "image/webp"}

# Extension mapping
_MIME_TO_EXT = {
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/webp": ".webp",
}


async def download_message_media(
    client: TelegramClient,
    message: Message,
    project_slug: str,
) -> list[str]:
    """Download all supported images from a Telegram message.

    Args:
        client: Connected TelegramClient instance.
        message: The Telegram message containing media.
        project_slug: Slug for the project (used for directory name).

    Returns:
        List of relative paths (from repo root) to downloaded images.
        First image is treated as cover, rest as screenshots.
    """
    if not message.media:
        return []

    # Determine the output directory
    output_dir = ASSETS_DIR / project_slug
    output_dir.mkdir(parents=True, exist_ok=True)

    downloaded: list[str] = []

    if isinstance(message.media, MessageMediaPhoto):
        # Single photo
        path = await _download_photo(client, message, output_dir, index=len(downloaded))
        if path:
            downloaded.append(path)

    elif isinstance(message.media, MessageMediaDocument):
        # Could be a document (image, GIF, etc.)
        mime = ""
        if message.media.document:
            mime = getattr(message.media.document, "mime_type", "")
        if mime in _IMAGE_MIMES:
            path = await _download_document(client, message, output_dir, index=len(downloaded), mime=mime)
            if path:
                downloaded.append(path)

    # Also check for grouped media (albums)
    # Telethon handles grouped media as separate messages with the same grouped_id,
    # so this function handles one message at a time. The caller should collect
    # all messages in a group.

    return downloaded


async def download_grouped_media(
    client: TelegramClient,
    messages: list[Message],
    project_slug: str,
) -> list[str]:
    """Download all images from a group of messages (album).

    Args:
        client: Connected TelegramClient instance.
        messages: List of messages in the group.
        project_slug: Slug for the project directory.

    Returns:
        List of relative paths to downloaded images.
    """
    output_dir = ASSETS_DIR / project_slug
    output_dir.mkdir(parents=True, exist_ok=True)

    downloaded: list[str] = []

    for message in messages:
        if not message.media:
            continue

        if isinstance(message.media, MessageMediaPhoto):
            path = await _download_photo(client, message, output_dir, index=len(downloaded))
            if path:
                downloaded.append(path)
        elif isinstance(message.media, MessageMediaDocument):
            mime = ""
            if message.media.document:
                mime = getattr(message.media.document, "mime_type", "")
            if mime in _IMAGE_MIMES:
                path = await _download_document(
                    client, message, output_dir, index=len(downloaded), mime=mime
                )
                if path:
                    downloaded.append(path)

    return downloaded


async def _download_photo(
    client: TelegramClient,
    message: Message,
    output_dir: Path,
    index: int,
) -> str:
    """Download a photo from a message.

    Returns:
        Relative path from repo root, or empty string on failure.
    """
    filename = deterministic_filename("", index, ".jpg")
    dest = output_dir / filename

    try:
        await client.client.download_media(message, file=str(dest))
        if dest.exists():
            rel_path = str(dest.relative_to(ROOT)).replace("\\", "/")
            logger.info("[INFO] Downloaded: %s", rel_path)
            return rel_path
    except Exception as exc:
        logger.error("[ERROR] Failed to download photo: %s", exc)

    return ""


async def _download_document(
    client: TelegramClient,
    message: Message,
    output_dir: Path,
    index: int,
    mime: str,
) -> str:
    """Download a document (image) from a message.

    Returns:
        Relative path from repo root, or empty string on failure.
    """
    ext = _MIME_TO_EXT.get(mime, ".jpg")
    filename = deterministic_filename("", index, ext)
    dest = output_dir / filename

    try:
        await client.client.download_media(message, file=str(dest))
        if dest.exists():
            rel_path = str(dest.relative_to(ROOT)).replace("\\", "/")
            logger.info("[INFO] Downloaded: %s", rel_path)
            return rel_path
    except Exception as exc:
        logger.error("[ERROR] Failed to download document: %s", exc)

    return ""
