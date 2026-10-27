"""
Execution Timer Decorator.

Measures elapsed execution time of functions with high precision.
"""

from functools import wraps
import time
from typing import Callable


def time_it(func: Callable) -> Callable:
    """Measure elapsed execution time of the decorated function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[{func.__name__}] Execution time: {elapsed * 1000:.3f} ms")
        return result
    return wrapper


@time_it
def compute_sum_of_squares(limit: int) -> int:
    """Calculate sum of squares up to limit."""
    return sum(i * i for i in range(limit))


if __name__ == "__main__":
    print("=== Execution Timer Decorator ===")
    res = compute_sum_of_squares(100_000)
    print(f"Result length: {len(str(res))} digits")
