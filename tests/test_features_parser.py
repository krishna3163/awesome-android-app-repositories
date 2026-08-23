"""Unit tests for feature post parsing (@popCLOUDS)."""

import pytest

from src.parsers.features_parser import FeatureParseError, parse_features


def test_parse_complete_features(sample_features_channel_post: str):
    parsed = parse_features(
        text=sample_features_channel_post,
        message_id=13548,
        channel="popCLOUDS",
    )

    assert parsed.raw_title == "Features of Neuron Pedia:"
    assert parsed.project_name_guess == "Neuron Pedia"
    assert parsed.message_id == 13548
    assert parsed.channel == "popCLOUDS"
    assert len(parsed.features) == 13

    first_feat = parsed.features[0]
    assert first_feat.title == "Feature/latent exploration"
    assert first_feat.description == "inspect individual model features and activations"

    second_feat = parsed.features[1]
    assert second_feat.title == "Semantic search"
    assert second_feat.description == "search millions of latents/features by meaning"


def test_parse_features_various_bullet_styles():
    text = (
        "App Features:\n"
        "- Clean UI: modern Material 3 interface\n"
        "* Fast Engine: optimized C++ core\n"
        "• Root support — works with Magisk & KernelSU\n"
        "1. Cloud Sync — backup settings to Drive"
    )

    parsed = parse_features(text=text)
    assert parsed.project_name_guess == "App"
    assert len(parsed.features) == 4
    assert parsed.features[0].title == "Clean UI"
    assert parsed.features[0].description == "modern Material 3 interface"
    assert parsed.features[1].title == "Fast Engine"
    assert parsed.features[2].title == "Root support"
    assert parsed.features[3].title == "Cloud Sync"


def test_parse_features_empty_raises():
    with pytest.raises(FeatureParseError, match="Empty message text"):
        parse_features(text="")
