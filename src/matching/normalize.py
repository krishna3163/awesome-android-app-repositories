"""Name normalization for cross-channel project matching."""

from __future__ import annotations

import re
import unicodedata

# Noise words removed during normalization.
# These appear in feature post titles but are not part of the project name.
_NOISE_WORDS = {
    "features",
    "feature",
    "of",
    "for",
    "the",
    "app",
    "application",
    "apps",
    "applications",
    "tool",
    "tools",
    "review",
    "overview",
    "introduction",
    "intro",
    "screenshots",
    "screenshot",
    "screenrecord",
    "screenrecords",
    "guide",
    "usage",
}

# Emoji pattern — matches most common emoji ranges
_EMOJI_RE = re.compile(
    r"[\U00010000-\U0010ffff\u2600-\u27bf\u2700-\u27bf\ufe00-\ufe0f"
    r"\u200d\u20e3\u2300-\u23ff\u2b50\u2b55\u3030\u303d]",
    re.UNICODE,
)


def normalize_name(name: str) -> str:
    """Normalize a project name for matching.

    Steps:
        1. Remove emojis and markdown formatting (*, _, `, ~)
        2. Normalize unicode (NFKD)
        3. Lowercase
        4. Remove noise words ('features', 'screenshots', 'of', 'app', etc.)
        5. Remove all spaces, hyphens, underscores, punctuation
        6. Strip remaining non-alphanumeric characters

    Examples:
        >>> normalize_name("Neuronpedia")
        'neuronpedia'
        >>> normalize_name("Features of Neuron Pedia")
        'neuronpedia'
        >>> normalize_name("**Features of croc :**")
        'croc'
        >>> normalize_name("Screenshots of SHOWCARD :")
        'showcard'
    """
    # Remove emojis
    text = _EMOJI_RE.sub("", name)

    # Strip markdown symbols
    text = re.sub(r"[\*_`~#]", "", text)

    # Normalize unicode
    text = unicodedata.normalize("NFKD", text)

    # Lowercase
    text = text.lower().strip()

    # Remove trailing/leading colons and dashes
    text = text.strip(":-—– \t\n")

    # Split into words and remove noise words
    words = text.split()
    words = [w.strip(":-—–.,;()") for w in words]
    words = [w for w in words if w and w not in _NOISE_WORDS]

    # Rejoin and remove all non-alphanumeric characters
    text = "".join(words)
    text = re.sub(r"[^a-z0-9]", "", text)

    return text
