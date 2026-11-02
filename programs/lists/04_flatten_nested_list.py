"""
Arbitrarily Nested List Flattener.

Recursively flattens lists with irregular nesting levels.
"""

from typing import Any


def flatten(nested: list[Any]) -> list[Any]:
    """Flatten an arbitrarily nested list."""
    flat_list = []
    for item in nested:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list


if __name__ == "__main__":
    print("=== Nested List Flattener ===")
    nested_data = [1, [2, [3, 4], 5], [[6]], 7, [8, [9, [10]]]]
    flattened = flatten(nested_data)
    print(f"Nested   : {nested_data}")
    print(f"Flattened: {flattened}")
