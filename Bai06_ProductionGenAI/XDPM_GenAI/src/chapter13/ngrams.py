"""Text-cleaning and n-gram utilities used for testing examples."""

from __future__ import annotations

import re


def lowercase_remove_punct_numbers(text: str) -> str:
    """Lowercase text and remove punctuation and digits, preserving whitespace."""
    return re.sub(r"[^a-z\s]", "", text.lower())


def multiple_to_single_spaces(text: str) -> str:
    """Collapse all repeated whitespace into a single space."""
    return re.sub(r"\s+", " ", text)


def create_ngrams(text: str, n: int) -> list[str]:
    """Create a list of character n-grams from normalized text.

    Args:
        text: Input string.
        n: Length of each n-gram.

    Returns:
        A list of contiguous n-grams.

    Raises:
        ValueError: If `n` is not positive.
    """
    if n <= 0:
        raise ValueError("n must be positive")

    processed_text = lowercase_remove_punct_numbers(text)
    single_space_processed = multiple_to_single_spaces(processed_text)

    if len(single_space_processed) < n:
        return []

    return [single_space_processed[i : i + n] for i in range(len(single_space_processed) - n + 1)]


if __name__ == "__main__":
    sample = "This is a sample text $ABC% for creating n-grams."
    print(create_ngrams(sample, 3))
