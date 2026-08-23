"""Parse main project posts from the primary Telegram channel (@popMODS)."""

from __future__ import annotations

import re
from datetime import UTC, datetime
from typing import Any

from src.config import ParsedProject
from src.parsers.link_extractor import extract_links_from_entities
from src.utils.logger import get_logger

logger = get_logger()


# Boilerplate sections to exclude from the project description.
# These are standard Telegram channel text not specific to the project.
_BOILERPLATE_MARKERS = [
    "support the project",
    "star the repo",
    "star the app",
    "buy a coffee",
    "contribute code",
    "contribute",
    "pull-requests",
    "pull requests",
    "❤️ support",
    "⭐ star",
    "☕ buy",
    "🛠 contribute",
    "🛠️ contribute",
]

# Section headers that signal the end of the description
_SECTION_HEADERS = [
    "🔗 links",
    "links:",
    "🏷 tags",
    "tags:",
    "❤️ support the project",
    "support the project",
    "source code:",
    "source:",
    "website:",
    "developer:",
    "developed by",
    "features:",
    "github:",
    "repository:",
    "repo:",
]

# Hashtag pattern
_HASHTAG_RE = re.compile(r"#(\w+)", re.UNICODE)


class ParseError(Exception):
    """Raised when a message cannot be parsed into a valid project."""


def parse_main_project(
    text: str,
    entities: list[Any] | None = None,
    message_id: int | None = None,
    channel: str = "",
    posted_at: str = "",
) -> ParsedProject:
    """Parse a main channel post into a ParsedProject.

    Args:
        text: The full message text content.
        entities: Telegram message entities (hyperlinks, etc.).
        message_id: Telegram message ID.
        channel: Channel username (e.g. 'popMODS').
        posted_at: ISO timestamp when the message was posted.

    Returns:
        A ParsedProject with extracted fields.

    Raises:
        ParseError: If the message cannot be parsed (e.g. no name found).
    """
    if not text or not text.strip():
        raise ParseError("Empty message text")

    lines = text.strip().split("\n")

    # 1. Extract project name (first non-empty line)
    name = _extract_name(lines)
    if not name:
        raise ParseError("Could not extract project name")

    # 2. Extract description (between name and section headers)
    description = _extract_description(lines)

    # 3. Extract links from entities
    links = extract_links_from_entities(text, entities)

    # 4. Extract tags (hashtags)
    tags = _extract_tags(text)

    # 5. Extract developer name from text
    developer_name = _extract_developer_name(text)

    # 6. Build the parsed project
    if not posted_at:
        posted_at = datetime.now(UTC).isoformat()

    # Filter out casual chat, polls, and news posts that have no repository or website link
    if not links.source_code and not links.website:
        raise ParseError("Message does not contain repository or website link")

    return ParsedProject(
        name=name,
        description=description,
        website=links.website,
        source_code=links.source_code,
        developer_name=developer_name or links.developer_name,
        developer_url=links.developer_url,
        features_message_url=links.features_url,
        tags=tags,
        telegram_source_message=f"https://t.me/{channel}/{message_id}" if channel and message_id else "",
        telegram_message_id=message_id,
        posted_at=posted_at,
    )


def _extract_name(lines: list[str]) -> str:
    """Extract the project name from the first non-empty line."""
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith("#") and not stripped.startswith("http"):
            # Remove emoji prefixes if any
            cleaned = re.sub(r"^[\U00010000-\U0010ffff\u2600-\u27bf\u2700-\u27bf\s]+", "", stripped)
            # Remove markdown bold/italic/backtick symbols
            cleaned = cleaned.strip("*_`~# \t")
            return cleaned.strip() if cleaned.strip() else stripped
    return ""


def _extract_description(lines: list[str]) -> str:
    """Extract the main project description.

    Starts after the project name (first non-empty line) and ends before
    the first section header or boilerplate content.
    """
    desc_lines: list[str] = []
    found_name = False
    in_description = False

    for line in lines:
        stripped = line.strip()

        # Skip until we find and pass the name line
        if not found_name:
            if stripped:
                found_name = True
            continue

        # Check if we've hit a section header or boilerplate
        lower = stripped.lower()
        if any(marker in lower for marker in _SECTION_HEADERS):
            break
        if any(marker in lower for marker in _BOILERPLATE_MARKERS):
            break
        # Stop at hashtag-only lines (tags section)
        if stripped and all(word.startswith("#") for word in stripped.split()):
            break

        # Accumulate description lines
        if stripped:
            in_description = True
            desc_lines.append(stripped)
        elif in_description:
            # Allow one blank line within the description
            desc_lines.append("")

    # Clean up trailing blank lines
    while desc_lines and not desc_lines[-1]:
        desc_lines.pop()

    return "\n".join(desc_lines).strip()


def _extract_tags(text: str) -> list[str]:
    """Extract hashtags from the message text.

    Finds all #hashtag occurrences, removes the '#', deduplicates,
    and preserves original capitalization.
    """
    tags = _HASHTAG_RE.findall(text)
    # Deduplicate while preserving order and original case
    seen: set[str] = set()
    unique: list[str] = []
    for tag in tags:
        lower = tag.lower()
        if lower not in seen:
            seen.add(lower)
            unique.append(tag)
    return unique


def _extract_developer_name(text: str) -> str:
    """Extract the developer name from text patterns.

    Looks for patterns like:
        Developer: Johnny Lin
        Developer — Johnny Lin
        Developed by Johnny Lin
    """
    patterns = [
        r"[Dd]eveloper\s*[:—–-]\s*(.+?)(?:\n|$)",
        r"[Dd]eveloped\s+by\s+(.+?)(?:\n|$)",
        r"[Aa]uthor\s*[:—–-]\s*(.+?)(?:\n|$)",
        r"[Cc]reator\s*[:—–-]\s*(.+?)(?:\n|$)",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            name = match.group(1).strip()
            # Remove any trailing URLs or hashtags
            name = re.sub(r"https?://\S+", "", name).strip()
            name = re.sub(r"#\S+", "", name).strip()
            if name:
                return name
    return ""
