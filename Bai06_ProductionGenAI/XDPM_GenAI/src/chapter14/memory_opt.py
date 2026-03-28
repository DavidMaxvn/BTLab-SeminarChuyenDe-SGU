"""Memory optimization example using CSV chunking."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def get_top_video(path: str | Path) -> str:
    """Load the whole CSV into memory and return the top video column."""
    interactions = pd.read_csv(path)
    avg_ratio = interactions.mean(axis=0, skipna=True)
    return str(avg_ratio.idxmax())


def get_top_video_chunked(path: str | Path, chunksize: int = 1000) -> str:
    """Read a CSV in chunks and return the video with the highest mean watch ratio."""
    cumulative_sum = None
    cumulative_count = None

    for chunk in pd.read_csv(path, chunksize=chunksize):
        chunk_sum = chunk.sum(skipna=True)
        chunk_count = chunk.count()
        if cumulative_sum is None:
            cumulative_sum = chunk_sum
            cumulative_count = chunk_count
        else:
            cumulative_sum += chunk_sum
            cumulative_count += chunk_count

    if cumulative_sum is None or cumulative_count is None:
        raise ValueError("CSV file is empty")

    average_ratio = cumulative_sum / cumulative_count
    return str(average_ratio.idxmax())


if __name__ == "__main__":
    sample_file = DATA_DIR / "interactions_100.csv"
    print("Full read top video:", get_top_video(sample_file))
    print("Chunked top video:", get_top_video_chunked(sample_file, chunksize=20))
