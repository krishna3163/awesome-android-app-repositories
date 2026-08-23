"""Unit tests for duplicate detection and prevention."""

from src.config import Project
from src.matching.project_matcher import MatchType, find_matching_project


def test_duplicate_repo_url(sample_project: Project):
    # Same repo with slightly different casing / trailing slash
    match = find_matching_project(
        name="Neuronpedia Fork",
        repo_url="https://github.com/hijohnnylin/neuronpedia/",
        existing_projects=[sample_project],
    )
    assert match.match_type == MatchType.EXACT_REPO
    assert match.project_id == sample_project.id


def test_duplicate_normalized_name(sample_project: Project):
    # Same normalized name
    match = find_matching_project(
        name="Neuron Pedia",
        repo_url="",
        existing_projects=[sample_project],
    )
    assert match.match_type == MatchType.EXACT_NAME
    assert match.project_id == sample_project.id


def test_no_duplicate_for_unique_project(sample_project: Project):
    match = find_matching_project(
        name="Magisk",
        repo_url="https://github.com/topjohnwu/Magisk",
        existing_projects=[sample_project],
    )
    assert match.match_type == MatchType.NO_MATCH
