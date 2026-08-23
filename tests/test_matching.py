"""Unit tests for name normalization and fuzzy matching."""

from src.config import Project
from src.matching.fuzzy_matcher import fuzzy_match
from src.matching.normalize import normalize_name
from src.matching.project_matcher import MatchType, find_matching_project


def test_normalize_name_variations():
    assert normalize_name("Neuronpedia") == "neuronpedia"
    assert normalize_name("Features of Neuron Pedia") == "neuronpedia"
    assert normalize_name("Features of Neuron Pedia:") == "neuronpedia"
    assert normalize_name("Neuron Pedia App") == "neuronpedia"
    assert normalize_name("🧠 Neuron-Pedia") == "neuronpedia"
    assert normalize_name("Neuron_Pedia") == "neuronpedia"
    assert normalize_name("NEURONPEDIA") == "neuronpedia"


def test_fuzzy_match_high_similarity():
    query = "neuronpedia"
    candidates = {"neuronpedia": "neuronpedia", "otherapp": "otherapp"}

    result = fuzzy_match(query, candidates, threshold=85)
    assert result.matched is True
    assert result.matched_key == "neuronpedia"
    assert result.score == 100.0


def test_project_matcher_exact_repo(sample_project: Project):
    match = find_matching_project(
        name="Different Name",
        repo_url="https://github.com/hijohnnylin/neuronpedia.git",
        existing_projects=[sample_project],
    )
    assert match.match_type == MatchType.EXACT_REPO
    assert match.project_id == "neuronpedia"
    assert match.confidence == 100.0


def test_project_matcher_normalized_name(sample_project: Project):
    match = find_matching_project(
        name="Features of Neuron Pedia",
        repo_url="",
        existing_projects=[sample_project],
    )
    assert match.match_type == MatchType.EXACT_NAME
    assert match.project_id == "neuronpedia"
    assert match.confidence == 100.0


def test_project_matcher_no_match(sample_project: Project):
    match = find_matching_project(
        name="Completely Unrelated Tool",
        repo_url="https://github.com/someone/unrelated",
        existing_projects=[sample_project],
    )
    assert match.match_type == MatchType.NO_MATCH
