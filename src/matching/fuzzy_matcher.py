"""Fuzzy string matching wrapper around RapidFuzz."""

from __future__ import annotations

from dataclasses import dataclass

from rapidfuzz import fuzz, process


@dataclass
class FuzzyResult:
    """Result of a fuzzy match attempt."""

    matched: bool
    score: float
    matched_key: str = ""
    matched_value: str = ""


def fuzzy_match(
    query: str,
    candidates: dict[str, str],
    threshold: int = 85,
) -> FuzzyResult:
    """Find the best fuzzy match for a query against candidate names.

    Uses RapidFuzz's token_sort_ratio for robust comparison that handles
    word order differences (e.g. "Neuron Pedia" vs "Pedia Neuron").

    Args:
        query: The normalized name to search for.
        candidates: Dict mapping project ID → normalized name.
        threshold: Minimum similarity score (0–100) to consider a match.

    Returns:
        A FuzzyResult with match status, score, and matched project info.
    """
    if not query or not candidates:
        return FuzzyResult(matched=False, score=0.0)

    # Build a list of (candidate_name, key) for process.extractOne
    choices = {key: name for key, name in candidates.items()}

    result = process.extractOne(
        query,
        choices,
        scorer=fuzz.ratio,
        score_cutoff=0,
    )

    if result is None:
        return FuzzyResult(matched=False, score=0.0)

    matched_name, score, matched_key = result

    return FuzzyResult(
        matched=score >= threshold,
        score=score,
        matched_key=matched_key,
        matched_value=matched_name,
    )


def similarity_score(a: str, b: str) -> float:
    """Calculate the similarity score between two strings.

    Args:
        a: First string.
        b: Second string.

    Returns:
        Similarity score from 0.0 to 100.0.
    """
    return fuzz.ratio(a, b)
