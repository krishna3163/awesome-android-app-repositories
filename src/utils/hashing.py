"""Hashing and slug utilities for deterministic filenames."""

from __future__ import annotations

import hashlib
import re
import unicodedata


def slugify(name: str, max_length: int = 50) -> str:
    """Convert a project name into a filesystem-safe slug.

    Examples:
        >>> slugify("Neuronpedia")
        'neuronpedia'
        >>> slugify("Play Integrity Fix (inject)")
        'play-integrity-fix-inject'
        >>> slugify("  Some App!!  ")
        'some-app'
    """
    # Normalize unicode
    text = unicodedata.normalize("NFKD", name)
    # Remove non-ASCII
    text = text.encode("ascii", "ignore").decode("ascii")
    # Lowercase
    text = text.lower().strip()
    # Replace non-alphanumeric with hyphens
    text = re.sub(r"[^a-z0-9]+", "-", text)
    # Collapse multiple hyphens and strip edges
    text = re.sub(r"-+", "-", text).strip("-")
    if len(text) > max_length:
        text = text[:max_length].rstrip("-")
    return text or "project"


def content_hash(filepath: str) -> str:
    """Return the SHA-256 hex digest of a file's contents.

    Used to detect duplicate image downloads.
    """
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def deterministic_filename(slug: str, index: int, extension: str = ".jpg") -> str:
    """Generate a deterministic image filename.

    Args:
        slug: Project slug (e.g. 'neuronpedia').
        index: 0-based image index. 0 = cover, 1+ = screenshots.
        extension: File extension including the dot.

    Returns:
        'cover.jpg' for index 0, 'screenshot-1.jpg' for index 1, etc.
    """
    if index == 0:
        return f"cover{extension}"
    return f"screenshot-{index}{extension}"
