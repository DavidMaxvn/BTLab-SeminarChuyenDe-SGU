"""Utilities for demonstrating documentation-friendly refactoring."""

from __future__ import annotations

import numpy as np


def parse_request_parameters(payload: dict) -> tuple[np.ndarray, np.ndarray, str]:
    """Parse and validate a distance request payload.

    Args:
        payload: Dictionary containing `df1`, `df2`, and `distance` keys.

    Returns:
        A tuple containing the first array, second array, and distance type.

    Raises:
        ValueError: If required keys are missing or arrays have different shapes.
    """
    if not isinstance(payload, dict):
        raise ValueError("payload must be a dictionary")

    a = np.asarray(payload.get("df1"))
    b = np.asarray(payload.get("df2"))
    dist_type = payload.get("distance")

    if a.size == 0 or b.size == 0:
        raise ValueError("df1 and df2 must be provided")
    if a.shape != b.shape:
        raise ValueError("Matrices must have the same shape")
    if dist_type not in {"L1", "L2"}:
        raise ValueError("distance must be either 'L1' or 'L2'")

    return a, b, dist_type


def get_manhattan_dist(a: np.ndarray, b: np.ndarray) -> float:
    """Calculate the Manhattan distance between two arrays."""
    return float(np.sum(np.abs(a - b)))


def get_euclidean_dist(a: np.ndarray, b: np.ndarray) -> float:
    """Calculate the Euclidean distance between two arrays."""
    return float(np.sqrt(np.sum((a - b) ** 2)))


def calculate_distance_from_payload(payload: dict) -> float:
    """Calculate a distance value from a JSON-like payload."""
    a, b, dist_type = parse_request_parameters(payload)
    dist_func = {"L1": get_manhattan_dist, "L2": get_euclidean_dist}[dist_type]
    return dist_func(a, b)


if __name__ == "__main__":
    example = {
        "distance": "L2",
        "df1": [1, 2, 3],
        "df2": [4, 5, 6],
    }
    print("Distance:", calculate_distance_from_payload(example))
