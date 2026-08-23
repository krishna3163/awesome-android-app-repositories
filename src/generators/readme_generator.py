"""Auto-generate README.md, Category Documentation Pages, and A-Z Directory Archive.

Prevents GitHub 512KB markdown rendering truncation by splitting the 1,600+
catalog into categorized pages while showcasing the latest discoveries on the main page.
"""

from __future__ import annotations

import logging
from collections import defaultdict
from datetime import UTC, datetime
from pathlib import Path

from src.config import Project

logger = logging.getLogger("telegram-sync")

ROOT = Path(__file__).resolve().parents[2]
README_PATH = ROOT / "README.md"
DOCS_DIR = ROOT / "docs"
CATEGORIES_DIR = DOCS_DIR / "categories"
ALL_APPS_PATH = DOCS_DIR / "all-apps.md"

START_MARKER = "<!-- AUTO-GENERATED-START -->"
END_MARKER = "<!-- AUTO-GENERATED-END -->"

# Definition of Categories: (slug, title, emoji, description)
CATEGORIES_CONFIG = [
    (
        "android",
        "Android Apps & Utilities",
        "📱",
        "Open-source Android applications, power tools, and clients.",
        lambda tags, text: any(k in tags for k in ["android", "apk"]) or "android" in text,
    ),
    (
        "tools-utilities",
        "Tools, Productivity & Utilities",
        "🛠️",
        "Productivity apps, file managers, system tweaks, notes, and utilities.",
        lambda tags, text: any(
            k in tags
            for k in [
                "tools",
                "utilities",
                "productivity",
                "tool",
                "utility",
                "security",
                "privacy",
                "notes",
                "files",
                "filemanager",
                "launcher",
            ]
        ),
    ),
    (
        "windows",
        "Windows Applications & Tweaks",
        "💻",
        "Open-source tools, desktop software, and customizers for Windows.",
        lambda tags, text: any(k in tags for k in ["windows", "pc"]) or "windows" in text,
    ),
    (
        "linux",
        "Linux Software & CLI Tools",
        "🐧",
        "Linux applications, command-line utilities, packages, and desktop tools.",
        lambda tags, text: any(k in tags for k in ["linux", "ubuntu", "debian", "arch"]) or "linux" in text,
    ),
    (
        "apple",
        "macOS & iOS Applications",
        "🍎",
        "Open-source tools and applications for macOS and iOS devices.",
        lambda tags, text: any(k in tags for k in ["macos", "ios", "mac", "apple"]) or "macos" in text,
    ),
    (
        "media-music",
        "Media, Video & Music Players",
        "🎵",
        "Music players, streaming frontends, audio equalizers, and video downloaders.",
        lambda tags, text: any(
            k in tags
            for k in [
                "music",
                "media",
                "player",
                "video",
                "audio",
                "streaming",
                "youtube",
                "stream",
                "flac",
                "podcast",
            ]
        )
        or "music" in text
        or "player" in text,
    ),
    (
        "web-ai",
        "Web, AI & Cloud Platforms",
        "🌐",
        "AI platforms, web applications, self-hosted services, and cloud tools.",
        lambda tags, text: any(
            k in tags
            for k in [
                "ai",
                "web",
                "website",
                "selfhosted",
                "docker",
                "cloud",
                "api",
                "server",
            ]
        )
        or "ai" in tags
        or "website" in tags,
    ),
    (
        "root-modules",
        "Root, Magisk & KernelSU Modules",
        "⚡",
        "Root utilities, Magisk/KernelSU/APatch modules, and Xposed enhancements.",
        lambda tags, text: any(
            k in tags
            for k in [
                "root",
                "magisk",
                "kernelsu",
                "xposed",
                "module",
                "modules",
                "shizuku",
                "apatch",
            ]
        )
        or "root" in text
        or "magisk" in text,
    ),
    (
        "extensions",
        "Browser Extensions & Add-ons",
        "🧩",
        "Extensions and scripts for Chrome, Firefox, Edge, and Chromium browsers.",
        lambda tags, text: any(k in tags for k in ["extension", "chrome", "firefox", "addon"]) or "extension" in text,
    ),
]


def classify_project(project: Project) -> list[str]:
    """Return a list of category slugs matching this project."""
    tags_lower = [t.lower() for t in project.tags]
    all_text = " ".join(tags_lower) + " " + project.name.lower() + " " + project.description.lower()

    matched_slugs = []
    for slug, _, _, _, match_fn in CATEGORIES_CONFIG:
        if match_fn(tags_lower, all_text):
            matched_slugs.append(slug)

    if not matched_slugs:
        matched_slugs.append("tools-utilities")

    return matched_slugs


def _generate_project_card(project: Project, repo_root_relative: str = "") -> list[str]:
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
        img_url = f"{repo_root_relative}{project.images.cover}" if repo_root_relative else project.images.cover
        all_images.append(("Cover / Preview", img_url))
    for i, screenshot in enumerate(project.images.screenshots, 1):
        if screenshot != project.images.cover:
            img_url = f"{repo_root_relative}{screenshot}" if repo_root_relative else screenshot
            all_images.append((f"Screenshot {i}", img_url))

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
    first_line = text.split("\n")[0].strip()
    if len(first_line) <= max_length:
        return first_line
    return first_line[: max_length - 1].rstrip() + "…"


def _select_trending_projects(projects: list[Project], limit: int = 8) -> list[Project]:
    """Select high-momentum, trending, and fast-rising repositories.

    Scored by presence of GitHub repository, feature richness, media assets,
    and trending keywords (AI, LLM, privacy, developer tools, automation).
    """
    trending_keywords = {"ai", "llm", "agent", "tool", "automation", "privacy", "flutter", "kotlin", "rust", "player"}

    def score_project(p: Project) -> float:
        score = 0.0
        if p.repository and "github.com" in p.repository.lower():
            score += 10.0
        if p.features:
            score += min(len(p.features), 10) * 1.5
        if p.images.cover or p.images.screenshots:
            score += 5.0
        tags_lower = {t.lower() for t in p.tags}
        desc_lower = p.description.lower()
        for kw in trending_keywords:
            if kw in tags_lower or kw in desc_lower:
                score += 3.0
        return score

    scored = sorted(projects, key=score_project, reverse=True)
    return scored[:limit]


def generate_main_content(projects: list[Project], category_counts: dict[str, int]) -> str:
    """Generate the auto-generated section for main README.md.

    Highlights trending projects, recent discoveries, and provides the Category Navigation Hub.
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
    lines.append(f"- 📦 **Total Discovered Apps & Projects:** `{len(projects)}`")
    lines.append(f"- 🏷️ **Unique Categories / Tags:** `{len(all_tags)}`")
    lines.append(f"- 🔄 **Last Automatically Synchronized:** `{now}`")
    lines.append("")
    lines.append("---")
    lines.append("")

    # --- Trending & Fast-Rising Projects ---
    trending = _select_trending_projects(projects, limit=6)
    if trending:
        lines.append("## 🔥 Trending & Fast-Rising Repositories")
        lines.append("")
        lines.append("> 🌟 **Curated Top List:** Outstanding open-source repositories and applications rapidly gaining community momentum:")
        lines.append("")
        for project in trending:
            lines.extend(_generate_project_card(project))
            lines.append("")
            lines.append("---")
            lines.append("")

    # --- Browse by Category Hub ---
    lines.append("## 📁 Browse by Platform & Category")
    lines.append("")
    lines.append("Explore our organized category directories to find the exact apps and tools you need:")
    lines.append("")
    lines.append("| Category | Focus & Description | Total Apps | Direct Link |")
    lines.append("|:---|:---|:---|:---|")

    for slug, title, emoji, desc, _ in CATEGORIES_CONFIG:
        count = category_counts.get(slug, 0)
        lines.append(f"| **{emoji} {title}** | {desc} | `{count} apps` | [**Explore →**](docs/categories/{slug}.md) |")

    lines.append(f"| **📚 Complete A–Z Index** | Full searchable table of all {len(projects)} cataloged applications | `{len(projects)} apps` | [**View Full Table →**](docs/all-apps.md) |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # --- Latest Discoveries (Top 25 Showcase) ---
    showcase_count = min(25, len(projects))
    if projects:
        lines.append(f"## 🆕 Latest Discovered Projects (Top {showcase_count})")
        lines.append("")
        lines.append(f"> Showing the newest **{showcase_count} additions**. To browse all **{len(projects)} apps**, visit the [Category Pages](#-browse-by-platform--category) or [Full Directory Index](docs/all-apps.md).")
        lines.append("")

        for project in projects[:showcase_count]:
            lines.extend(_generate_project_card(project))
            lines.append("")
            lines.append("---")
            lines.append("")

    return "\n".join(lines)


def generate_category_pages(projects: list[Project]) -> dict[str, int]:
    """Generate categorized markdown files in docs/categories/."""
    CATEGORIES_DIR.mkdir(parents=True, exist_ok=True)

    # Group projects into categories
    category_projects = defaultdict(list)
    for p in projects:
        for slug in classify_project(p):
            category_projects[slug].append(p)

    counts = {}

    for slug, title, emoji, desc, _ in CATEGORIES_CONFIG:
        cat_apps = category_projects.get(slug, [])
        counts[slug] = len(cat_apps)

        lines: list[str] = []
        lines.append(f"# {emoji} {title}")
        lines.append("")
        lines.append(f"### {desc}")
        lines.append("")
        lines.append("[⬅️ **Back to Main Catalog**](../../README.md) • [📚 **All Apps Index**](../all-apps.md)")
        lines.append("")
        lines.append(f"> **Total Apps in Category:** `{len(cat_apps)}`")
        lines.append("")
        lines.append("---")
        lines.append("")

        if cat_apps:
            for project in cat_apps:
                lines.extend(_generate_project_card(project, repo_root_relative="../../"))
                lines.append("")
                lines.append("---")
                lines.append("")
        else:
            lines.append("_No applications currently in this category._\n")

        cat_file = CATEGORIES_DIR / f"{slug}.md"
        cat_file.write_text("\n".join(lines), encoding="utf-8")

    return counts


def generate_all_apps_page(projects: list[Project]) -> None:
    """Generate a clean, searchable A-Z table of all projects in docs/all-apps.md."""
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    sorted_alpha = sorted(projects, key=lambda p: p.name.lower())

    lines: list[str] = []
    lines.append("# 📚 Complete Applications & Projects Index")
    lines.append("")
    lines.append("### Searchable A–Z directory of all cataloged open-source apps, tools, and repositories.")
    lines.append("")
    lines.append("[⬅️ **Back to Main Catalog**](../README.md)")
    lines.append("")
    lines.append(f"> **Total Cataloged Projects:** `{len(projects)}`")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("| App / Project | Description | Source Repository | Official Website | Categories |")
    lines.append("|:---|:---|:---|:---|:---|")

    for project in sorted_alpha:
        name = project.name
        desc = _truncate(project.description, 70)
        repo_link = f"[GitHub]({project.repository})" if project.repository else "—"
        web_link = f"[Website]({project.website})" if project.website else "—"
        tags = ", ".join(project.tags) if project.tags else "—"
        lines.append(f"| **{name}** | {desc} | {repo_link} | {web_link} | `{tags}` |")

    lines.append("")
    ALL_APPS_PATH.write_text("\n".join(lines), encoding="utf-8")


def update_readme(projects: list[Project]) -> bool:
    """Update README.md, Category documentation pages, and All-Apps index.

    Args:
        projects: List of Project objects.

    Returns:
        True if generation completed successfully.
    """
    # 1. Generate category pages and collect counts
    category_counts = generate_category_pages(projects)

    # 2. Generate A-Z index table
    generate_all_apps_page(projects)

    # 3. Update main README.md
    if not README_PATH.exists():
        logger.warning("[WARNING] README.md not found at %s", README_PATH)
        return False

    content = README_PATH.read_text(encoding="utf-8")

    if START_MARKER not in content or END_MARKER not in content:
        logger.warning("[WARNING] Auto-generation markers not found in README.md")
        return False

    start_idx = content.index(START_MARKER) + len(START_MARKER)
    end_idx = content.index(END_MARKER)

    generated = generate_main_content(projects, category_counts)
    new_content = content[:start_idx] + "\n" + generated + content[end_idx:]

    README_PATH.write_text(new_content, encoding="utf-8")
    logger.info("[INFO] README.md and all category documentation pages updated successfully")
    return True
