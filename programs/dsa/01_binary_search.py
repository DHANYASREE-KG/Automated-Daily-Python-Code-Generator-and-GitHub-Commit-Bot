"""
Binary Search Algorithm.

Finds target position within a sorted list in O(log n) time.
"""


def binary_search(sorted_arr: list[int], target: int) -> int:
    """Return index of target in sorted_arr, or -1 if not found."""
    left = 0
    right = len(sorted_arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_arr[mid] == target:
            return mid
        elif sorted_arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    print("=== Binary Search ===")
    data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    query = 23
    idx = binary_search(data, query)
    print(f"Array : {data}")
    print(f"Target: {query} found at index: {idx}")
