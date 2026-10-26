"""
Second Largest Element Finder.

Finds the second distinct maximum value in a list in a single pass.
"""


def find_second_largest(numbers: list[int]) -> int | None:
    """Find the second largest unique number in numbers in O(n) time."""
    if len(numbers) < 2:
        return None

    first = second = float("-inf")
    for num in numbers:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    return int(second) if second != float("-inf") else None


if __name__ == "__main__":
    print("=== Second Largest Element Finder ===")
    data = [12, 35, 1, 10, 34, 35, 1]
    result = find_second_largest(data)
    print(f"List: {data}")
    print(f"Second largest element: {result}")
