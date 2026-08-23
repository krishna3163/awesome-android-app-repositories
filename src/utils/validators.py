"""Validation helpers for URLs, names, descriptions, and images."""

from __future__ import annotations

import os
import re
from urllib.parse import urlparse

_GITHUB_REPO_RE = re.compile(
    r"^https?://github\.com/(?P<owner>[A-Za-z0-9\-_.]+)/(?P<repo>[A-Za-z0-9\-_.]+)/?$"
)


def normalize_github_url(url: str) -> str:
    """Normalize a GitHub repository URL to a canonical form.

    Strips trailing slashes, '.git' suffix, and lowercases owner/repo.

    Examples:
        >>> normalize_github_url("https://github.com/User/Repo.git")
        'https://github.com/User/Repo'
        >>> normalize_github_url("https://github.com/user/repo/")
        'https://github.com/user/repo'
    """
    url = url.strip()
    # Remove trailing .git
    if url.endswith(".git"):
        url = url[:-4]
    # Remove trailing slashes
    url = url.rstrip("/")
    # Remove extra path segments beyond owner/repo
    parsed = urlparse(url)
    if parsed.hostname in ("github.com", "www.github.com"):
        parts = parsed.path.strip("/").split("/")
        if len(parts) >= 2:
            url = f"https://github.com/{parts[0]}/{parts[1]}"
    return url


def validate_github_url(url: str) -> bool:
    """Check if the URL is a valid GitHub repository URL.

    Args:
        url: URL string to validate.

    Returns:
        True if the URL matches https://github.com/{owner}/{repo} format.
    """
    normalized = normalize_github_url(url)
    return bool(_GITHUB_REPO_RE.match(normalized))


def validate_website_url(url: str) -> bool:
    """Check if the URL uses http or https scheme.

    Args:
        url: URL string to validate.

    Returns:
        True if the URL starts with http:// or https://.
    """
    if not url:
        return False
    parsed = urlparse(url.strip())
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)


def validate_project_name(name: str) -> bool:
    """Check that a project name is non-empty and meaningful.

    Args:
        name: Project name to validate.

    Returns:
        True if the name is non-empty after stripping whitespace.
    """
    return bool(name and name.strip())


def validate_description(description: str, min_length: int = 20) -> bool:
    """Check that a description meets minimum length requirements.

    Args:
        description: Description text to validate.
        min_length: Minimum character count (default 20).

    Returns:
        True if the description is at least min_length characters.
    """
    return bool(description) and len(description.strip()) >= min_length


def validate_image_exists(path: str) -> bool:
    """Check that an image file exists on disk.

    Args:
        path: File path to check.

    Returns:
        True if the file exists and is a regular file.
    """
    return os.path.isfile(path)
