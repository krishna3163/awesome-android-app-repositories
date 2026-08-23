"""Unit tests for slug and hashing utilities."""

from pathlib import Path

from src.utils.hashing import content_hash, deterministic_filename, slugify


def test_slugify():
    assert slugify("Neuronpedia") == "neuronpedia"
    assert slugify("Play Integrity Fix (inject)") == "play-integrity-fix-inject"
    assert slugify("  App   Name! ") == "app-name"
    assert slugify("App-Name_2026") == "app-name-2026"


def test_deterministic_filename():
    assert deterministic_filename("app", 0, ".jpg") == "cover.jpg"
    assert deterministic_filename("app", 1, ".jpg") == "screenshot-1.jpg"
    assert deterministic_filename("app", 2, ".png") == "screenshot-2.png"


def test_content_hash(tmp_path: Path):
    file = tmp_path / "test.txt"
    file.write_bytes(b"hello world")
    h = content_hash(str(file))
    assert h == "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"
