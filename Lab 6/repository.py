"""Repository abstractions and in-memory repository."""

from __future__ import annotations

from typing import List, Protocol

from .models import VideoInteraction


class VideoRepository(Protocol):
    """Protocol for retrieving video interactions."""

    def get_all_interactions(self) -> List[VideoInteraction]:
        """Return all interactions."""
        ...


class InMemoryVideoRepository:
    """Simple repository backed by an in-memory list."""

    def __init__(self, data: list[VideoInteraction]):
        self._data = data

    def get_all_interactions(self) -> list[VideoInteraction]:
        return self._data
