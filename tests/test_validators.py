"""Unit tests for validators and URL normalization."""

from src.utils.validators import (
    normalize_github_url,
    validate_description,
    validate_github_url,
    validate_project_name,
    validate_website_url,
)


def test_normalize_github_url():
    assert normalize_github_url("https://github.com/user/repo") == "https://github.com/user/repo"
    assert normalize_github_url("https://github.com/user/repo/") == "https://github.com/user/repo"
    assert normalize_github_url("https://github.com/user/repo.git") == "https://github.com/user/repo"
    assert normalize_github_url("https://github.com/user/repo/tree/main") == "https://github.com/user/repo"


def test_validate_github_url():
    assert validate_github_url("https://github.com/user/repo") is True
    assert validate_github_url("https://github.com/user/repo.git") is True
    assert validate_github_url("https://notgithub.com/user/repo") is False
    assert validate_github_url("https://github.com/user") is False
    assert validate_github_url("") is False


def test_validate_website_url():
    assert validate_website_url("https://example.com") is True
    assert validate_website_url("http://example.com/path") is True
    assert validate_website_url("ftp://example.com") is False
    assert validate_website_url("not-a-url") is False
    assert validate_website_url("") is False


def test_validate_project_name():
    assert validate_project_name("Neuronpedia") is True
    assert validate_project_name("   ") is False
    assert validate_project_name("") is False


def test_validate_description():
    assert validate_description("Short text", min_length=20) is False
    assert validate_description("This is a long enough description that passes validation.", min_length=20) is True
