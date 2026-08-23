"""Auto-generate README.md from apps.json data.

Uses marker-based injection (same pattern as the existing repos) so the
README template can contain manually written sections above/below the
auto-generated content.
"""

from __future__ import annotations

import logging
from datetime import UTC, datetime
from pathlib import Path

from src.config import Project

logger = logging.getLogger("telegram-sync")

ROOT = Path(__file__).resolve().parents[2]
README_PATH = ROOT / "README.md"

START_MARKER = "<!-- AUTO-GENERATED-START -->"
END_MARKER = "<!-- AUTO-GENERATED-END -->"


def generate_content(projects: list[Project]) -> str:
    """Generate the auto-generated markdown content from the project list.

    Produces:
        1. Statistics header
        2. Latest projects section (detailed cards)
        3. Searchable table (all projects)

    Args:
        projects: List of Project objects, already sorted by created_at desc.

    Returns:
        Markdown string to inject between the markers.
    """
    lines: list[str] = []
    now = datetime.now(UTC).strftime("%Y-%m-%d %H:%M UTC")

    # Collect all unique tags
    all_tags: set[str] = set()
    for project in projects:
        all_tags.update(project.tags)

    # --- Statistics ---
    lines.append("")
    lines.append("## 📊 Statistics")
    lines.append("")
    lines.append(f"- **Total Projects:** {len(projects)}")
    lines.append(f"- **Categories:** {len(all_tags)}")
    lines.append(f"- **Last Updated:** {now}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # --- Latest Projects (detailed cards) ---
    if projects:
        lines.append("## 🆕 Latest Projects")
        lines.append("")

        for project in projects:
            lines.extend(_generate_project_card(project))
            lines.append("")
            lines.append("---")
            lines.append("")

    # --- Searchable Table ---
    lines.append("## 📋 All Projects")
    lines.append("")
    lines.append("| Project | Description | Repository | Tags |")
    lines.append("|:---|:---|:---|:---|")

    if projects:
        for project in projects:
            name = project.name
            desc = _truncate(project.description, 80)
            repo_link = f"[GitHub]({project.repository})" if project.repository else "—"
            tags = ", ".join(project.tags) if project.tags else "—"
            lines.append(f"| **{name}** | {desc} | {repo_link} | {tags} |")
    else:
        lines.append("| _No projects yet._ | — | — | — |")

    lines.append("")
    return "\n".join(lines)


def _generate_project_card(project: Project) -> list[str]:
    """Generate detailed markdown card for a single project."""
    lines: list[str] = []

    lines.append(f"### {project.name}")
    lines.append("")

    # Cover image
    if project.images.cover:
        lines.append(f"![{project.name} Cover]({project.images.cover})")
        lines.append("")

    # Description
    if project.description:
        lines.append(project.description)
        lines.append("")

    # Links
    if project.website:
        lines.append(f"**Website:** {project.website}")
        lines.append("")
    if project.repository:
        lines.append(f"**Source Code:** {project.repository}")
        lines.append("")
    if project.developer.name:
        dev_text = project.developer.name
        if project.developer.url:
            dev_text = f"[{project.developer.name}]({project.developer.url})"
        lines.append(f"**Developer:** {dev_text}")
        lines.append("")

    # Tags
    if project.tags:
        lines.append(f"**Tags:** {' • '.join(project.tags)}")
        lines.append("")

    # Features
    if project.features:
        lines.append("#### Features")
        lines.append("")
        for feature in project.features:
            if feature.description:
                lines.append(f"- **{feature.title}** — {feature.description}")
            else:
                lines.append(f"- {feature.title}")
        lines.append("")

    # Screenshots
    if project.images.screenshots:
        lines.append("<details>")
        lines.append("<summary>📸 Screenshots</summary>")
        lines.append("")
        for i, screenshot in enumerate(project.images.screenshots, 1):
            lines.append(f"![Screenshot {i}]({screenshot})")
            lines.append("")
        lines.append("</details>")
        lines.append("")

    return lines


def _truncate(text: str, max_length: int) -> str:
    """Truncate text to max_length, adding ellipsis if needed."""
    if not text:
        return "—"
    # Take first line only for table
    first_line = text.split("\n")[0].strip()
    if len(first_line) <= max_length:
        return first_line
    return first_line[: max_length - 1].rstrip() + "…"


def update_readme(projects: list[Project]) -> bool:
    """Update the README.md with auto-generated content from project data.

    Finds the START_MARKER and END_MARKER in the existing README and
    replaces everything between them with freshly generated content.

    Args:
        projects: List of Project objects.

    Returns:
        True if the README was modified, False if it was already up-to-date
        or markers were not found.
    """
    if not README_PATH.exists():
        logger.warning("[WARNING] README.md not found at %s", README_PATH)
        return False

    content = README_PATH.read_text(encoding="utf-8")

    if START_MARKER not in content or END_MARKER not in content:
        logger.warning("[WARNING] Auto-generation markers not found in README.md")
        return False

    start_idx = content.index(START_MARKER) + len(START_MARKER)
    end_idx = content.index(END_MARKER)

    generated = generate_content(projects)
    new_content = content[:start_idx] + "\n" + generated + content[end_idx:]

    if new_content == content:
        logger.info("[INFO] README.md is already up-to-date")
        return False

    README_PATH.write_text(new_content, encoding="utf-8")
    logger.info("[INFO] README.md updated with latest project data")
    return True
