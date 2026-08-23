"""Extract and classify URLs from Telegram message text and entities."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

from src.utils.validators import normalize_github_url

# Labels that map to specific link categories
_WEBSITE_LABELS = {"website", "web", "homepage", "home", "site", "official site", "official website"}
_SOURCE_LABELS = {
    "source code",
    "source",
    "github",
    "repository",
    "repo",
    "code",
    "git",
    "open source",
    "sourcecode",
}
_FEATURES_LABELS = {"features", "feature", "feature list", "highlights"}
_DEVELOPER_LABELS = {"developer", "dev", "author", "creator", "maintainer", "developed by"}


@dataclass
class ExtractedLinks:
    """Categorized links extracted from a Telegram message."""

    website: str = ""
    source_code: str = ""
    features_url: str = ""
    developer_url: str = ""
    developer_name: str = ""
    all_urls: list[str] = field(default_factory=list)


def _clean_label(text: str) -> str:
    """Normalize a link label for matching."""
    return text.strip().lower().rstrip(":").strip()


def extract_links_from_entities(
    text: str,
    entities: list[Any] | None = None,
) -> ExtractedLinks:
    """Extract and classify URLs from Telegram message entities.

    Telegram messages can contain hyperlinks as entities (MessageEntityTextUrl)
    where visible text (e.g. "Website") hides the actual URL. This function
    reads those entities and classifies URLs by the visible label text.

    Also falls back to scanning raw text for bare URLs.

    Args:
        text: The message text content.
        entities: List of Telethon message entity objects (or dicts with
            'url', 'offset', 'length' keys for testing).

    Returns:
        An ExtractedLinks instance with categorized URLs.
    """
    result = ExtractedLinks()
    seen_urls: set[str] = set()

    # Process entities (hyperlinks behind text labels)
    if entities:
        for entity in entities:
            url = _get_entity_url(entity)
            if not url:
                continue

            offset = _get_entity_offset(entity)
            length = _get_entity_length(entity)
            label_text = text[offset : offset + length] if offset is not None and length else ""
            label = _clean_label(label_text)
            preceding = text[max(0, (offset or 0) - 30) : (offset or 0)].lower() if offset is not None else ""

            if url not in seen_urls:
                result.all_urls.append(url)
                seen_urls.add(url)

            _classify_url(result, url, label, label_text, preceding)

    # Fallback: scan raw text for bare URLs not already found via entities
    bare_urls = re.findall(r"https?://[^\s)<>\]]+", text)
    for url in bare_urls:
        url = url.rstrip(".,;:!?)")
        if url not in seen_urls:
            result.all_urls.append(url)
            seen_urls.add(url)
            # Try to classify by context (line above the URL)
            _classify_bare_url(result, url, text)

    # Normalize GitHub URL if found
    if result.source_code:
        result.source_code = normalize_github_url(result.source_code)

    return result


def _get_entity_url(entity: Any) -> str:
    """Extract URL from an entity (supports Telethon objects and dicts)."""
    if isinstance(entity, dict):
        return entity.get("url", "")
    return getattr(entity, "url", "") or ""


def _get_entity_offset(entity: Any) -> int | None:
    """Extract offset from an entity."""
    if isinstance(entity, dict):
        return entity.get("offset")
    return getattr(entity, "offset", None)


def _get_entity_length(entity: Any) -> int | None:
    """Extract length from an entity."""
    if isinstance(entity, dict):
        return entity.get("length")
    return getattr(entity, "length", None)


def _classify_url(result: ExtractedLinks, url: str, label: str, raw_label: str, preceding: str = "") -> None:
    """Assign a URL to a category based on the visible label text and context."""
    if (label in _WEBSITE_LABELS or any(w in preceding for w in ("website", "site", "homepage"))) and not result.website:
        result.website = url
    elif (label in _SOURCE_LABELS or any(w in preceding for w in ("source code", "source", "repo", "repository", "github"))) and not result.source_code:
        result.source_code = url
    elif (label in _FEATURES_LABELS or "features" in preceding) and not result.features_url:
        result.features_url = url
    elif label in _DEVELOPER_LABELS or any(w in preceding for w in ("developer", "author", "creator", "dev:")):
        if not result.developer_url:
            result.developer_url = url
        if not result.developer_name and raw_label and label not in _DEVELOPER_LABELS:
            result.developer_name = raw_label
    # Auto-detect GitHub repo vs user profile URLs
    elif "github.com" in url:
        path_parts = url.split("github.com/")[-1].strip("/").split("/")
        if len(path_parts) == 2 and not result.source_code:
            result.source_code = url
        elif len(path_parts) == 1 and not result.developer_url:
            result.developer_url = url


def _classify_bare_url(result: ExtractedLinks, url: str, full_text: str) -> None:
    """Try to classify a bare URL by looking at surrounding text context."""
    # Find the line containing this URL
    lines = full_text.split("\n")
    url_line_idx = None
    for i, line in enumerate(lines):
        if url in line:
            url_line_idx = i
            break

    if url_line_idx is None:
        return

    # Check the line itself and the line above for label clues
    context_lines = []
    if url_line_idx > 0:
        context_lines.append(lines[url_line_idx - 1])
    context_lines.append(lines[url_line_idx])
    context = " ".join(context_lines).lower()

    if any(label in context for label in _WEBSITE_LABELS) and not result.website:
        result.website = url
    elif any(label in context for label in _SOURCE_LABELS) and not result.source_code:
        result.source_code = url
    elif any(label in context for label in _DEVELOPER_LABELS) and not result.developer_url:
        result.developer_url = url
    elif "github.com" in url and not result.source_code:
        path_parts = url.split("github.com/")[-1].strip("/").split("/")
        if len(path_parts) >= 2:
            result.source_code = url
