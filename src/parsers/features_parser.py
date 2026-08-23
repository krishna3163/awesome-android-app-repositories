"""Parse feature posts from the features Telegram channel (@popCLOUDS)."""

from __future__ import annotations

import re

from src.config import Feature, ParsedFeatures
from src.utils.logger import get_logger

logger = get_logger()


# Common bullet characters
_BULLET_RE = re.compile(r"^\s*(?:[•\-\*▸▹►▻➤➜➡→⬥⬦]|\d+[.)]\s)", re.UNICODE)

# Emoji prefix pattern (one or more emojis at the start)
_EMOJI_PREFIX_RE = re.compile(
    r"^[\U00010000-\U0010ffff\u2600-\u27bf\u2700-\u27bf\ufe00-\ufe0f\u200d\u20e3"
    r"\u2300-\u23ff\u2b50\u2b55\u3030\u303d\U0001f000-\U0001f9ff]+\s*",
    re.UNICODE,
)

# Title patterns — lines like "Features of X:", "X Features", etc.
_TITLE_PATTERNS = [
    re.compile(r"^[Ff]eatures?\s+(?:of|for)\s+(.+?)\s*:?\s*$"),
    re.compile(r"^(.+?)\s+[Ff]eatures?\s*:?\s*$"),
    re.compile(r"^(.+?)\s*:?\s*$"),  # Fallback: entire first line
]

# Separator between title and description in a bullet point
_SEPARATOR_RE = re.compile(r"\s*[—–:]\s*")


class FeatureParseError(Exception):
    """Raised when a features post cannot be parsed."""


def parse_features(
    text: str,
    message_id: int | None = None,
    channel: str = "",
) -> ParsedFeatures:
    """Parse a features channel post into structured features.

    Args:
        text: The full message text.
        message_id: Telegram message ID.
        channel: Channel username.

    Returns:
        A ParsedFeatures with extracted title, project name guess, and features list.

    Raises:
        FeatureParseError: If the message cannot be parsed.
    """
    if not text or not text.strip():
        raise FeatureParseError("Empty message text")

    lines = text.strip().split("\n")

    # 1. Extract the title / project name from the first line
    raw_title = lines[0].strip()
    project_name = _extract_project_name(raw_title)

    # 2. Extract feature bullet points
    features = _extract_features(lines[1:])

    return ParsedFeatures(
        raw_title=raw_title,
        project_name_guess=project_name,
        features=features,
        message_id=message_id,
        channel=channel,
    )


def _extract_project_name(title_line: str) -> str:
    """Extract the probable project name from a features post title.

    Handles patterns like:
        'Features of Neuron Pedia:' → 'Neuron Pedia'
        'Neuron Pedia Features'     → 'Neuron Pedia'
        'Neuron Pedia:'             → 'Neuron Pedia'
    """
    # Remove trailing colons
    cleaned = title_line.rstrip(":").strip()
    # Remove emoji prefix
    cleaned = _EMOJI_PREFIX_RE.sub("", cleaned).strip()

    for pattern in _TITLE_PATTERNS[:-1]:  # Try specific patterns first
        match = pattern.match(cleaned)
        if match:
            return match.group(1).strip()

    # Fallback: the entire cleaned line is the project name
    return cleaned


def _extract_features(lines: list[str]) -> list[Feature]:
    """Extract feature entries from the body of a features post.

    Each feature is expected to be a bullet point, optionally with an emoji
    prefix and a separator (—, –, or :) between title and description.

    Examples:
        • 🧠 Feature exploration — inspect model features
        - Semantic search: search by meaning
        * Activation analysis
    """
    features: list[Feature] = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        # Check if it looks like a bullet point
        if not _BULLET_RE.match(stripped):
            continue

        # Remove the bullet character
        content = _BULLET_RE.sub("", stripped).strip()
        if not content:
            continue

        # Remove emoji prefix from the content
        content = _EMOJI_PREFIX_RE.sub("", content).strip()
        if not content:
            continue

        # Split into title and description by separator
        feature = _parse_single_feature(content)
        if feature:
            features.append(feature)

    return features


def _parse_single_feature(content: str) -> Feature | None:
    """Parse a single feature line into a Feature object.

    Splits on '—', '–', or ':' separator. If no separator is found,
    the entire content becomes the title.
    """
    # Try splitting on common separators
    parts = _SEPARATOR_RE.split(content, maxsplit=1)

    if len(parts) == 2:
        title = parts[0].strip()
        description = parts[1].strip()
        if title:
            return Feature(title=title, description=description)
    elif len(parts) == 1:
        title = parts[0].strip()
        if title:
            return Feature(title=title, description="")

    return None
