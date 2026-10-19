"""
Two Sum Solver.

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

Time Complexity: O(n)
Space Complexity: O(n)
"""


def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    """Find indices of two numbers that add up to target."""
    seen_map: dict[int, int] = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in seen_map:
            return seen_map[complement], idx
        seen_map[num] = idx
    return None


if __name__ == "__main__":
    print("=== Two Sum Solver ===")
    numbers = [2, 7, 11, 15]
    goal = 9
    indices = two_sum(numbers, goal)
    print(f"Array: {numbers}, Target: {goal}")
    if indices:
        i, j = indices
        print(f"Match found at indices ({i}, {j}): {numbers[i]} + {numbers[j]} = {goal}")
