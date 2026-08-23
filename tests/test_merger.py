"""Unit tests for project merging logic."""

from src.config import Feature, ParsedFeatures, PendingFeature, Project
from src.database.merger import (
    merge_features_into_project,
    merge_pending_into_project,
    merge_project,
)


def test_merge_project_preserves_existing_data(sample_project: Project):
    # New data has empty description and website, but has new tags
    new_data = {
        "description": "",
        "website": "",
        "tags": ["AI", "Research", "DeepLearning"],
    }
    merged = merge_project(sample_project, new_data)

    # Existing valid description and website must NOT be overwritten
    assert merged.description == sample_project.description
    assert merged.website == sample_project.website
    # Tags should be merged
    assert "Research" in merged.tags
    assert "DeepLearning" in merged.tags
    assert "Website" in merged.tags


def test_merge_features_into_project(sample_project: Project):
    parsed_features = ParsedFeatures(
        raw_title="Features of Neuron Pedia",
        project_name_guess="Neuron Pedia",
        features=[
            Feature(title="Semantic search", description="Search latents"),  # duplicate title
            Feature(title="New Feature", description="Brand new functionality"),
        ],
        message_id=9999,
        channel="popCLOUDS",
    )

    merged = merge_features_into_project(
        project=sample_project,
        parsed_features=parsed_features,
        image_paths=["assets/apps/neuronpedia/cover.jpg", "assets/apps/neuronpedia/screenshot-2.jpg"],
        features_channel="popCLOUDS",
    )

    # Should not duplicate "Semantic search", but should add "New Feature"
    titles = [f.title for f in merged.features]
    assert titles.count("Semantic search") == 1
    assert "New Feature" in titles
    assert "assets/apps/neuronpedia/screenshot-2.jpg" in merged.images.screenshots
    assert merged.telegram.features_message_id == 9999


def test_merge_pending_features(sample_project: Project):
    pending = PendingFeature(
        raw_title="Features of Neuron Pedia",
        normalized_title="neuronpedia",
        features=[Feature(title="Pending Feat", description="Was waiting")],
        image_paths=["assets/apps/neuronpedia/cover.jpg"],
        channel="popCLOUDS",
        message_id=5555,
    )

    merged = merge_pending_into_project(sample_project, pending)
    titles = [f.title for f in merged.features]
    assert "Pending Feat" in titles
    assert merged.telegram.features_channel == "@popCLOUDS"
    assert merged.telegram.features_message_id == 5555
