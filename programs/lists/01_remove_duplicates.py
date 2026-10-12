"""
Order-Preserving List Deduplication.

Removes duplicates from a list while keeping the original appearance order.
"""

from typing import Hashable, TypeVar

T = TypeVar("T", bound=Hashable)


def deduplicate_preserve_order(items: list[T]) -> list[T]:
    """Remove duplicates while preserving original order using set lookups."""
    seen: set[T] = set()
    result: list[T] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


if __name__ == "__main__":
    print("=== Order-Preserving Deduplication ===")
    raw_list = [4, 5, 2, 4, 1, 5, 9, 2, 8, 1]
    cleaned = deduplicate_preserve_order(raw_list)
    print(f"Original: {raw_list}")
    print(f"Cleaned : {cleaned}")
