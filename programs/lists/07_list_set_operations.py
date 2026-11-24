"""
List Set Operations.

Calculates mathematical set relationships between two lists.
"""


def list_intersection(a: list, b: list) -> list:
    """Return common items in order of appearance in 'a'."""
    b_set = set(b)
    return [item for item in a if item in b_set]


def list_difference(a: list, b: list) -> list:
    """Return items in 'a' but not in 'b'."""
    b_set = set(b)
    return [item for item in a if item not in b_set]


if __name__ == "__main__":
    print("=== List Set Operations ===")
    list_a = [1, 2, 3, 4, 5, 6]
    list_b = [4, 5, 6, 7, 8, 9]

    print(f"A = {list_a}")
    print(f"B = {list_b}")
    print(f"Intersection (A ∩ B): {list_intersection(list_a, list_b)}")
    print(f"Difference (A - B)  : {list_difference(list_a, list_b)}")
