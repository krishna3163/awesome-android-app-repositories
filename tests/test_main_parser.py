"""Unit tests for main project post parsing (@popMODS)."""

import pytest

from src.parsers.main_project_parser import ParseError, parse_main_project


def test_parse_complete_project(sample_main_channel_post: str, sample_main_channel_entities: list[dict]):
    parsed = parse_main_project(
        text=sample_main_channel_post,
        entities=sample_main_channel_entities,
        message_id=12345,
        channel="popMODS",
    )

    assert parsed.name == "Neuronpedia"
    assert "Neuronpedia is an open-source AI interpretability platform" in parsed.description
    assert "Support the Project" not in parsed.description
    assert "Buy a coffee" not in parsed.description
    assert "Star the repo" not in parsed.description

    assert parsed.website == "https://neuronpedia.org/"
    assert parsed.source_code == "https://github.com/hijohnnylin/neuronpedia"
    assert parsed.developer_name == "Johnny Lin"
    assert parsed.developer_url == "https://github.com/hijohnnylin"
    assert parsed.features_message_url == "https://t.me/popCLOUDS/13548"
    assert parsed.tags == ["Website", "AI", "Learning"]
    assert parsed.telegram_message_id == 12345
    assert parsed.telegram_source_message == "https://t.me/popMODS/12345"


def test_parse_bare_urls():
    text = (
        "SimpleApp\n\n"
        "A minimal utility for Android devices.\n\n"
        "Source code: https://github.com/author/simple-app\n"
        "Website: https://simpleapp.io\n\n"
        "#Utility #Android"
    )

    parsed = parse_main_project(text=text)
    assert parsed.name == "SimpleApp"
    assert parsed.description == "A minimal utility for Android devices."
    assert parsed.source_code == "https://github.com/author/simple-app"
    assert parsed.website == "https://simpleapp.io"
    assert parsed.tags == ["Utility", "Android"]


def test_parse_empty_text_raises():
    with pytest.raises(ParseError, match="Empty message text"):
        parse_main_project(text="")

    with pytest.raises(ParseError, match="Empty message text"):
        parse_main_project(text="   \n\n  ")


def test_parse_minimal_project():
    text = "Cool Tool\n\nThis is a minimal utility project description for Android.\n\nWebsite: https://cooltool.dev\n\n#Tool"
    parsed = parse_main_project(text=text)
    assert parsed.name == "Cool Tool"
    assert "minimal utility project" in parsed.description
    assert parsed.tags == ["Tool"]
    assert parsed.website == "https://cooltool.dev"
    assert parsed.source_code == ""
