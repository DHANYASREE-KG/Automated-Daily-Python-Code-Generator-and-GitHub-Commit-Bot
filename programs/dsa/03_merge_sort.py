"""
Merge Sort Algorithm.

A divide-and-conquer algorithm that produces a stable sort in O(n log n) time.
"""


def merge_sort(arr: list[int]) -> list[int]:
    """Recursively sort array using Merge Sort."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)


def _merge(left: list[int], right: list[int]) -> list[int]:
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


if __name__ == "__main__":
    print("=== Merge Sort ===")
    items = [38, 27, 43, 3, 9, 82, 10]
    print(f"Unsorted: {items}")
    print(f"Sorted  : {merge_sort(items)}")
