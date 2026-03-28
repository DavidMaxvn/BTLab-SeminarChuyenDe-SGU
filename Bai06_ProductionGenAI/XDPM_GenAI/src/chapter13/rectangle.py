"""Rectangle intersection example for TDD."""

from __future__ import annotations

Rect = tuple[float, float, float, float]


def rect_intersection_area(rect1: Rect, rect2: Rect) -> float:
    """Calculate the area of intersection between two rectangles.

    Each rectangle is represented as a tuple `(x1, y1, x2, y2)`.
    """
    if rect1[0] >= rect1[2] or rect1[1] >= rect1[3]:
        raise ValueError(f"Invalid rectangle dimensions for rect1: {rect1}")
    if rect2[0] >= rect2[2] or rect2[1] >= rect2[3]:
        raise ValueError(f"Invalid rectangle dimensions for rect2: {rect2}")

    x_left = max(rect1[0], rect2[0])
    y_bottom = max(rect1[1], rect2[1])
    x_right = min(rect1[2], rect2[2])
    y_top = min(rect1[3], rect2[3])

    if x_left < x_right and y_bottom < y_top:
        return (x_right - x_left) * (y_top - y_bottom)
    return 0
