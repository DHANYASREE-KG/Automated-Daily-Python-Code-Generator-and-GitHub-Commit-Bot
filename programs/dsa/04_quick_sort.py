"""
Quick Sort Algorithm.

Divide-and-conquer sorting by choosing a pivot and partitioning elements.
"""


def quick_sort(arr: list[int]) -> list[int]:
    """Sort list using Quick Sort algorithm."""
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    print("=== Quick Sort ===")
    raw = [10, 7, 8, 9, 1, 5]
    print(f"Input : {raw}")
    print(f"Sorted: {quick_sort(raw)}")
