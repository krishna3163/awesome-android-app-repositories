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
        2. Detailed project cards with collapsible screenshots & features
        3. Collapsible Searchable Quick Index Table at the bottom

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
    lines.append("## 📊 Catalog Overview")
    lines.append("")
    lines.append(f"- 📦 **Total Discovered Apps & Repositories:** `{len(projects)}`")
    lines.append(f"- 🏷️ **Unique Categories / Tags:** `{len(all_tags)}`")
    lines.append(f"- 🔄 **Last Automatically Synchronized:** `{now}`")
    lines.append("")
    lines.append("---")
    lines.append("")

    # --- Detailed Projects Directory ---
    if projects:
        lines.append("## 📱 Discover Apps & Project Details")
        lines.append("")
        lines.append("> Click on the **🖼️ Preview Screenshots & Media** dropdown under any project to view screenshots before deciding to download or use.")
        lines.append("")

        for project in projects:
            lines.extend(_generate_project_card(project))
            lines.append("")
            lines.append("---")
            lines.append("")

    # --- Collapsible Searchable Table / Quick Index at the bottom ---
    lines.append("<details id=\"quick-index\">")
    lines.append(f"<summary><h2>📋 Quick Directory Index ({len(projects)} Apps Table) — <i>Click to expand full list</i></h2></summary>")
    lines.append("")
    lines.append("| App / Project | Description | Repository | Categories |")
    lines.append("|:---|:---|:---|:---|")

    if projects:
        for project in projects:
            name = project.name
            desc = _truncate(project.description, 75)
            repo_link = f"[GitHub]({project.repository})" if project.repository else "—"
            tags = ", ".join(project.tags) if project.tags else "—"
            lines.append(f"| **{name}** | {desc} | {repo_link} | `{tags}` |")
    else:
        lines.append("| _No projects synced yet._ | — | — | — |")

    lines.append("")
    lines.append("</details>")
    lines.append("")

    return "\n".join(lines)


def _generate_project_card(project: Project) -> list[str]:
    """Generate a clean, user-friendly markdown card for a single project."""
    lines: list[str] = []

    # Project Title
    lines.append(f"### 📦 {project.name}")
    lines.append("")

    # Categories / Tags
    if project.tags:
        tag_badges = " ".join(f"`#{t}`" for t in project.tags)
        lines.append(f"> **Categories:** {tag_badges}")
        lines.append("")

    # Description
    if project.description:
        lines.append(project.description)
        lines.append("")

    # Links & Metadata
    links_meta = []
    if project.repository:
        links_meta.append(f"- 🐙 **Source Code:** [{project.repository}]({project.repository})")
    if project.website:
        links_meta.append(f"- 🌐 **Official Website:** [{project.website}]({project.website})")
    if project.developer.name:
        clean_dev = project.developer.name.replace("[", "").replace("]", "").replace("(", "").replace(")", "").strip("*_`~ ")
        if clean_dev:
            dev_text = f"[{clean_dev}]({project.developer.url})" if project.developer.url else clean_dev
            links_meta.append(f"- 👤 **Developer:** {dev_text}")

    if links_meta:
        lines.extend(links_meta)
        lines.append("")

    # Collapsible Features List
    if project.features:
        lines.append("<details>")
        lines.append(f"<summary><b>✨ Key Features ({len(project.features)})</b> — <i>Click to expand</i></summary>")
        lines.append("")
        for feature in project.features:
            if feature.description:
                lines.append(f"- **{feature.title}** — {feature.description}")
            else:
                lines.append(f"- {feature.title}")
        lines.append("")
        lines.append("</details>")
        lines.append("")

    # Collapsible Screenshots & Images Gallery
    all_images: list[tuple[str, str]] = []
    if project.images.cover:
        all_images.append(("Cover / Preview", project.images.cover))
    for i, screenshot in enumerate(project.images.screenshots, 1):
        if screenshot != project.images.cover:
            all_images.append((f"Screenshot {i}", screenshot))

    if all_images:
        lines.append("<details>")
        lines.append(f"<summary><b>🖼️ Preview Screenshots & Media ({len(all_images)})</b> — <i>Click to view images & decide if you want to use this app</i></summary>")
        lines.append("")
        for title, img_path in all_images:
            lines.append(f"#### 📸 {title}")
            lines.append(f'<p align="center"><img src="{img_path}" alt="{title}" style="max-height: 480px; max-width: 100%; border-radius: 8px; margin: 8px auto;" /></p>')
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
