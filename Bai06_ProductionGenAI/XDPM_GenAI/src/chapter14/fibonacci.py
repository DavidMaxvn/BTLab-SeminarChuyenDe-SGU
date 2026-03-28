"""Runtime profiling example using Fibonacci implementations."""

from __future__ import annotations

import time
from functools import lru_cache


def fibonacci_recursive(n: int) -> int:
    """Compute Fibonacci recursively with exponential time complexity."""
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


@lru_cache(maxsize=None)
def fibonacci_memoized(n: int) -> int:
    """Compute Fibonacci using memoization."""
    if n <= 1:
        return n
    return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)


def fib_pair(n: int) -> tuple[int, int]:
    """Return `(F(n), F(n+1))` using fast doubling."""
    if n == 0:
        return (0, 1)
    a, b = fib_pair(n // 2)
    c = a * ((2 * b) - a)
    d = a * a + b * b
    if n & 1:
        return (d, c + d)
    return (c, d)


def fibonacci_fast_doubling(n: int) -> int:
    """Compute Fibonacci using the fast-doubling method."""
    return fib_pair(n)[0]


def profile_function(func, n: int) -> tuple[int, float]:
    """Run a function and return result plus runtime in seconds."""
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    return result, end - start


if __name__ == "__main__":
    for fn, n in [(fibonacci_recursive, 30), (fibonacci_memoized, 35), (fibonacci_fast_doubling, 100)]:
        result, runtime = profile_function(fn, n)
        print(f"{fn.__name__}({n}) = {result}")
        print(f"Runtime: {runtime:.6f} seconds\n")
