"""Structured logging setup with UTF-8 support."""

from __future__ import annotations

import io
import logging
import sys

LOGGER_NAME = "telegram-sync"


def setup_logging(level: int = logging.INFO) -> logging.Logger:
    """Configure and return the application logger.

    Uses a UTF-8 stream handler to stdout so emoji and special characters
    render correctly in both local terminals and GitHub Actions logs.
    """
    logger = logging.getLogger(LOGGER_NAME)

    if logger.handlers:
        return logger

    stream = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    handler = logging.StreamHandler(stream)
    handler.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(handler)
    logger.setLevel(level)
    return logger


def get_logger() -> logging.Logger:
    """Return the application logger (creates if needed)."""
    return logging.getLogger(LOGGER_NAME)
