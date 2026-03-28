"""Domain models for the architecture example."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class VideoInteraction:
    """A single user's watch interaction with a video."""
    user_id: str
    video_id: str
    watch_ratio: float
