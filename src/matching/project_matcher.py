"""Multi-step project matching orchestrator.

Implements the matching strategy:
    1. Repository URL exact match
    2. Normalized name exact match
    3. Fuzzy name match (≥90% → auto-merge)
    4. Fuzzy name match (75–89% → store for review)
    5. No match (<75% → new project or pending)
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from src.config import Project
from src.matching.fuzzy_matcher import fuzzy_match
from src.matching.normalize import normalize_name
from src.utils.validators import normalize_github_url


class MatchType(Enum):
    """Type of match found."""

    EXACT_REPO = "exact_repo"
    EXACT_NAME = "exact_name"
    FUZZY_HIGH = "fuzzy_high"       # ≥90% — auto-merge
    FUZZY_REVIEW = "fuzzy_review"   # 75–89% — needs review
    NO_MATCH = "no_match"


@dataclass
class MatchResult:
    """Result of the project matching process."""

    match_type: MatchType
    project: Project | None = None
    project_id: str = ""
    confidence: float = 0.0


def find_matching_project(
    name: str,
    repo_url: str,
    existing_projects: list[Project],
    duplicate_threshold: int = 90,
    review_threshold_low: int = 75,
) -> MatchResult:
    """Find an existing project that matches the given name and/or repo URL.

    Implements a multi-step matching strategy with decreasing confidence.

    Args:
        name: The incoming project or feature post name.
        repo_url: The repository URL (if available).
        existing_projects: List of all existing projects in the database.
        duplicate_threshold: Score threshold for auto-merge (default 90).
        review_threshold_low: Score threshold for review-required (default 75).

    Returns:
        A MatchResult indicating what was found and the confidence level.
    """
    if not existing_projects:
        return MatchResult(match_type=MatchType.NO_MATCH)

    # Step 1: Exact repository URL match (highest priority)
    if repo_url:
        normalized_repo = normalize_github_url(repo_url)
        for project in existing_projects:
            if project.repository and normalize_github_url(project.repository) == normalized_repo:
                return MatchResult(
                    match_type=MatchType.EXACT_REPO,
                    project=project,
                    project_id=project.id,
                    confidence=100.0,
                )

    # Step 2: Normalized name exact match
    incoming_normalized = normalize_name(name)
    if incoming_normalized:
        for project in existing_projects:
            if normalize_name(project.name) == incoming_normalized:
                return MatchResult(
                    match_type=MatchType.EXACT_NAME,
                    project=project,
                    project_id=project.id,
                    confidence=100.0,
                )

    # Step 3 & 4: Fuzzy name matching
    if incoming_normalized:
        candidates = {
            project.id: normalize_name(project.name)
            for project in existing_projects
            if normalize_name(project.name)  # Skip projects with empty normalized names
        }

        if candidates:
            result = fuzzy_match(incoming_normalized, candidates, threshold=review_threshold_low)

            if result.matched and result.score >= duplicate_threshold:
                # High confidence — auto-merge
                matched_project = next(
                    (p for p in existing_projects if p.id == result.matched_key),
                    None,
                )
                return MatchResult(
                    match_type=MatchType.FUZZY_HIGH,
                    project=matched_project,
                    project_id=result.matched_key,
                    confidence=result.score,
                )
            elif result.matched and result.score >= review_threshold_low:
                # Medium confidence — needs review
                matched_project = next(
                    (p for p in existing_projects if p.id == result.matched_key),
                    None,
                )
                return MatchResult(
                    match_type=MatchType.FUZZY_REVIEW,
                    project=matched_project,
                    project_id=result.matched_key,
                    confidence=result.score,
                )

    # Step 5: No match found
    return MatchResult(match_type=MatchType.NO_MATCH)
