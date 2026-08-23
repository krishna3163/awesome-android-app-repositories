"""Unit tests for README generator."""

from pathlib import Path

from src.config import Project
from src.generators.readme_generator import generate_main_content, update_readme


def test_generate_main_content(sample_project: Project):
    md = generate_main_content([sample_project], {"android": 1, "web-ai": 1})

    assert "## 📊 Catalog Overview" in md
    assert "**Total Discovered Apps & Projects:** `1`" in md
    assert "**Unique Categories / Tags:** `3`" in md
    assert "## 📁 Browse by Platform & Category" in md
    assert "docs/categories/android.md" in md
    assert "docs/all-apps.md" in md
    assert "### 📦 Neuronpedia" in md
    assert "assets/apps/neuronpedia/cover.jpg" in md
    assert "https://neuronpedia.org" in md
    assert "https://github.com/hijohnnylin/neuronpedia" in md
    assert "[Johnny Lin](https://github.com/hijohnnylin)" in md


def test_update_readme_with_markers(tmp_path: Path, sample_project: Project, monkeypatch):
    test_readme = tmp_path / "README.md"
    test_readme.write_text(
        "# Header\n\n<!-- AUTO-GENERATED-START -->\nold\n<!-- AUTO-GENERATED-END -->\n\n## Footer",
        encoding="utf-8",
    )
    test_docs = tmp_path / "docs"
    test_cats = test_docs / "categories"
    test_all = test_docs / "all-apps.md"

    monkeypatch.setattr("src.generators.readme_generator.README_PATH", test_readme)
    monkeypatch.setattr("src.generators.readme_generator.DOCS_DIR", test_docs)
    monkeypatch.setattr("src.generators.readme_generator.CATEGORIES_DIR", test_cats)
    monkeypatch.setattr("src.generators.readme_generator.ALL_APPS_PATH", test_all)

    changed = update_readme([sample_project])
    assert changed is True

    content = test_readme.read_text(encoding="utf-8")
    assert "# Header" in content
    assert "## Footer" in content
    assert "### 📦 Neuronpedia" in content
    assert "old" not in content

    # Verify docs were created
    assert test_all.exists()
    assert (test_cats / "android.md").exists()
    assert (test_cats / "web-ai.md").exists()
