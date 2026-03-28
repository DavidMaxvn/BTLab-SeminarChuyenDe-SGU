"""Decorators for logging, validation, and monitoring."""

from __future__ import annotations

import logging
from functools import wraps
from pathlib import Path
from typing import Any, Callable

LOG_DIR = Path(__file__).resolve().parents[2] / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "app.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)
FIZZBUZZ_COUNTER = 0


def log_function_args(func: Callable[..., Any]) -> Callable[..., Any]:
    """Log function call arguments."""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        logger.info("Calling %s args=%s kwargs=%s", func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return wrapper


def validate_limit(func: Callable[..., Any]) -> Callable[..., Any]:
    """Validate the FizzBuzz limit input."""
    @wraps(func)
    def wrapper(limit: int, *args: Any, **kwargs: Any) -> Any:
        if not isinstance(limit, int):
            raise TypeError("limit must be an integer")
        if not (0 <= limit < 500):
            raise ValueError("limit must be in range [0, 500)")
        return func(limit, *args, **kwargs)
    return wrapper


def count_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    """Count how many times the decorated function is called."""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        global FIZZBUZZ_COUNTER
        result = func(*args, **kwargs)
        FIZZBUZZ_COUNTER += 1
        logger.info("FIZZBUZZ_COUNTER=%s", FIZZBUZZ_COUNTER)
        return result
    return wrapper
