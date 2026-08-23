"""Configuration, settings, and Pydantic domain models."""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Literal

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings

# ---------------------------------------------------------------------------
# Settings (loaded from env / .env)
# ---------------------------------------------------------------------------


class ChannelConfig(BaseModel):
    """Configuration for a single Telegram channel to monitor."""

    username: str
    type: Literal["main_project", "features"]


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    telegram_api_id: int = 0
    telegram_api_hash: str = ""
    telegram_session_string: str = ""

    # Channel configuration
    main_channel: str = "popMODS"
    features_channel: str = "popCLOUDS"

    # Matching thresholds
    fuzzy_match_threshold: int = 85
    duplicate_threshold: int = 90
    review_threshold_low: int = 75

    # Validation
    min_description_length: int = 20

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8", "extra": "ignore"}

    @property
    def channels(self) -> list[ChannelConfig]:
        """Build channel list from individual settings."""
        return [
            ChannelConfig(username=self.main_channel, type="main_project"),
            ChannelConfig(username=self.features_channel, type="features"),
        ]


# ---------------------------------------------------------------------------
# Domain models
# ---------------------------------------------------------------------------


class Developer(BaseModel):
    """Developer information."""

    name: str = ""
    url: str = ""


class Feature(BaseModel):
    """A single project feature extracted from the features channel."""

    title: str
    description: str = ""


class ImageSet(BaseModel):
    """Image paths relative to the repository root."""

    cover: str = ""
    screenshots: list[str] = Field(default_factory=list)


class TelegramSource(BaseModel):
    """Telegram source message metadata."""

    main_channel: str = ""
    main_message_id: int | None = None
    features_channel: str = ""
    features_message_id: int | None = None


class Project(BaseModel):
    """A fully resolved project stored in apps.json."""

    id: str
    name: str
    description: str = ""
    website: str = ""
    repository: str = ""
    developer: Developer = Field(default_factory=Developer)
    features: list[Feature] = Field(default_factory=list)
    tags: list[str] = Field(default_factory=list)
    images: ImageSet = Field(default_factory=ImageSet)
    telegram: TelegramSource = Field(default_factory=TelegramSource)
    status: str = "active"
    created_at: str = Field(default_factory=lambda: datetime.now(UTC).isoformat())
    updated_at: str = Field(default_factory=lambda: datetime.now(UTC).isoformat())


class PendingFeature(BaseModel):
    """Unmatched feature post waiting for a corresponding project."""

    raw_title: str
    normalized_title: str = ""
    features: list[Feature] = Field(default_factory=list)
    image_paths: list[str] = Field(default_factory=list)
    channel: str = ""
    message_id: int | None = None
    received_at: str = Field(default_factory=lambda: datetime.now(UTC).isoformat())


class FailedPost(BaseModel):
    """A post that failed to parse."""

    channel: str
    message_id: int | None = None
    error: str = ""
    raw_text: str = ""
    timestamp: str = Field(default_factory=lambda: datetime.now(UTC).isoformat())


class ReviewMatch(BaseModel):
    """An uncertain fuzzy match requiring manual review."""

    incoming_name: str
    incoming_normalized: str = ""
    matched_project_id: str = ""
    matched_project_name: str = ""
    similarity_score: float = 0.0
    channel: str = ""
    message_id: int | None = None
    raw_text: str = ""
    timestamp: str = Field(default_factory=lambda: datetime.now(UTC).isoformat())


class ParsedProject(BaseModel):
    """Intermediate parsing result from a main channel post."""

    name: str
    description: str = ""
    website: str = ""
    source_code: str = ""
    developer_name: str = ""
    developer_url: str = ""
    features_message_url: str = ""
    tags: list[str] = Field(default_factory=list)
    telegram_source_message: str = ""
    telegram_message_id: int | None = None
    posted_at: str = ""


class ParsedFeatures(BaseModel):
    """Intermediate parsing result from a features channel post."""

    raw_title: str
    project_name_guess: str = ""
    features: list[Feature] = Field(default_factory=list)
    message_id: int | None = None
    channel: str = ""
