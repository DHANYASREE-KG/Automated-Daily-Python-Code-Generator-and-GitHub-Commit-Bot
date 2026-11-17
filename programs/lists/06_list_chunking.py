"""
List Chunking Utility.

Partitions a sequence into equal-sized batches.
"""

from typing import TypeVar

T = TypeVar("T")


def chunk_list(items: list[T], chunk_size: int) -> list[list[T]]:
    """Split items into sublists of size chunk_size."""
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]


if __name__ == "__main__":
    print("=== List Chunking Utility ===")
    records = list(range(1, 21))
    batches = chunk_list(records, chunk_size=5)
    print(f"Total elements: {len(records)}")
    for idx, batch in enumerate(batches, start=1):
        print(f"Batch #{idx}: {batch}")
