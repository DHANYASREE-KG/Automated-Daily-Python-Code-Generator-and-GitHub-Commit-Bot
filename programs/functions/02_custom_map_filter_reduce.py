"""
Custom Higher-Order Functions.

Builds custom map, filter, and reduce utilities to explore functional concepts.
"""

from typing import Callable, Iterable, TypeVar

T = TypeVar("T")
R = TypeVar("R")


def my_map(func: Callable[[T], R], items: Iterable[T]) -> list[R]:
    """Custom implementation of map()."""
    return [func(item) for item in items]


def my_filter(predicate: Callable[[T], bool], items: Iterable[T]) -> list[T]:
    """Custom implementation of filter()."""
    return [item for item in items if predicate(item)]


def my_reduce(func: Callable[[R, T], R], items: Iterable[T], initial: R) -> R:
    """Custom implementation of functools.reduce()."""
    accumulator = initial
    for item in items:
        accumulator = func(accumulator, item)
    return accumulator


if __name__ == "__main__":
    print("=== Custom Higher-Order Functions ===")
    numbers = [1, 2, 3, 4, 5, 6]

    doubled = my_map(lambda x: x * 2, numbers)
    evens = my_filter(lambda x: x % 2 == 0, numbers)
    total_sum = my_reduce(lambda acc, x: acc + x, numbers, 0)

    print(f"Original : {numbers}")
    print(f"Doubled  : {doubled}")
    print(f"Evens    : {evens}")
    print(f"Sum      : {total_sum}")
