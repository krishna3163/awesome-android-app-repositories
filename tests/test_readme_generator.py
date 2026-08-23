"""Unit tests for README generator."""

from pathlib import Path

from src.config import Project
from src.generators.readme_generator import generate_content, update_readme


def test_generate_content_structure(sample_project: Project):
    md = generate_content([sample_project])

    assert "## 📊 Catalog Overview" in md
    assert "**Total Discovered Apps & Repositories:** `1`" in md
    assert "**Unique Categories / Tags:** `3`" in md
    assert "Quick Directory Index" in md
    assert "## 📱 Discover Apps & Project Details" in md
    assert "### 📦 Neuronpedia" in md
    assert "assets/apps/neuronpedia/cover.jpg" in md
    assert "https://neuronpedia.org" in md
    assert "https://github.com/hijohnnylin/neuronpedia" in md
    assert "[Johnny Lin](https://github.com/hijohnnylin)" in md
    assert "| **Neuronpedia** |" in md


def test_update_readme_with_markers(tmp_path: Path, sample_project: Project, monkeypatch):
    test_readme = tmp_path / "README.md"
    test_readme.write_text(
        "# Header\n\n<!-- AUTO-GENERATED-START -->\nold\n<!-- AUTO-GENERATED-END -->\n\n## Footer",
        encoding="utf-8",
    )

    monkeypatch.setattr("src.generators.readme_generator.README_PATH", test_readme)

    changed = update_readme([sample_project])
    assert changed is True

    content = test_readme.read_text(encoding="utf-8")
    assert "# Header" in content
    assert "## Footer" in content
    assert "### 📦 Neuronpedia" in content
    assert "old" not in content
