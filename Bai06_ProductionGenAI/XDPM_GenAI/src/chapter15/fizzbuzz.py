"""FizzBuzz example with logging, validation, and monitoring decorators."""

from __future__ import annotations

from .decorators import count_calls, log_function_args, validate_limit


@count_calls
@validate_limit
@log_function_args
def print_fizzbuzz(limit: int) -> None:
    """Print the FizzBuzz sequence up to `limit`."""
    for i in range(1, limit + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    print_fizzbuzz(20)
