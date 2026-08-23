"""Language detection and translation utilities for multi-language Telegram channels."""

from __future__ import annotations

import logging
import re

logger = logging.getLogger("telegram-sync")

# Regex to detect non-Latin scripts (Cyrillic, CJK, Arabic, Persian, Hebrew, Devanagari, etc.)
_NON_LATIN_RE = re.compile(
    r"[\u0400-\u04FF\u4E00-\u9FFF\u3040-\u30FF\u0600-\u06FF\u0590-\u05FF\u0900-\u097F\uAC00-\uD7AF]"
)


def contains_foreign_script(text: str) -> bool:
    """Return True if the text contains non-Latin scripts that likely need translation."""
    if not text:
        return False
    return bool(_NON_LATIN_RE.search(text))


def translate_to_english(text: str) -> str:
    """Translate non-English text to English.

    Uses deep_translator with automatic source language detection.
    If the text is already standard English/ASCII or if translation fails,
    returns the original text safely.

    Args:
        text: The source text to translate.

    Returns:
        Translated text in English.
    """
    if not text or not text.strip():
        return text

    # Only translate if foreign script or non-ASCII is present
    if not contains_foreign_script(text):
        return text

    try:
        from deep_translator import GoogleTranslator

        # GoogleTranslator allows up to 5000 chars per call
        cleaned_text = text.strip()
        if len(cleaned_text) > 4500:
            cleaned_text = cleaned_text[:4500]

        translated = GoogleTranslator(source="auto", target="en").translate(cleaned_text)
        if translated and translated.strip():
            return translated.strip()
    except Exception as exc:
        logger.warning("[WARNING] Translation failed: %s (keeping original text)", exc)

    return text
