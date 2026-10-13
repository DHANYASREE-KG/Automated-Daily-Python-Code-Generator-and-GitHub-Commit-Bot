"""
Memoized Fibonacci Decorator.

Demonstrates caching function results using a custom memoize decorator.
"""

from functools import wraps
from typing import Callable


def memoize(func: Callable) -> Callable:
    """Decorator to cache return values based on positional arguments."""
    cache: dict = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@memoize
def fibonacci(n: int) -> int:
    """Compute nth Fibonacci number recursively with O(n) memoized time."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print("=== Memoized Fibonacci ===")
    print("Computing fibonacci(50) instantaneously thanks to caching:")
    print(f"fibonacci(50) = {fibonacci(50)}")
