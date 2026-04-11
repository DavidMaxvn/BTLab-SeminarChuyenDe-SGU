"""Service layer for analytics logic."""

from __future__ import annotations

from .repository import VideoRepository


class VideoAnalyticsService:
    """Business logic for video analytics."""

    def __init__(self, repository: VideoRepository):
        self.repository = repository

    def get_top_video(self) -> str:
        """Return the video id with the highest average watch ratio."""
        interactions = self.repository.get_all_interactions()
        if not interactions:
            raise ValueError("No interaction data available")

        totals: dict[str, float] = {}
        counts: dict[str, int] = {}

        for item in interactions:
            totals[item.video_id] = totals.get(item.video_id, 0.0) + item.watch_ratio
            counts[item.video_id] = counts.get(item.video_id, 0) + 1

        averages = {video_id: totals[video_id] / counts[video_id] for video_id in totals}
        return max(averages, key=averages.get)
