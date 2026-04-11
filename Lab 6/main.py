"""Entry point for the layered architecture example."""

from __future__ import annotations

from .models import VideoInteraction
from .repository import InMemoryVideoRepository
from .service import VideoAnalyticsService


def build_sample_service() -> VideoAnalyticsService:
    """Build a demo service with sample data."""
    sample_data = [
        VideoInteraction("u1", "video_1", 0.7),
        VideoInteraction("u2", "video_1", 0.9),
        VideoInteraction("u3", "video_2", 0.5),
        VideoInteraction("u4", "video_2", 0.6),
    ]
    repo = InMemoryVideoRepository(sample_data)
    return VideoAnalyticsService(repo)


if __name__ == "__main__":
    service = build_sample_service()
    print("Top video:", service.get_top_video())
