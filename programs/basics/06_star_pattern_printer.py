"""
Star and Pyramid Pattern Printer.

Demonstrates nested loop structures by generating geometric star patterns.
"""


def build_pyramid(height: int) -> list[str]:
    """Construct an upright symmetric pyramid of stars."""
    lines = []
    for i in range(height):
        spaces = " " * (height - i - 1)
        stars = "*" * (2 * i + 1)
        lines.append(f"{spaces}{stars}")
    return lines


def build_diamond(half_height: int) -> list[str]:
    """Construct a full diamond pattern."""
    top = build_pyramid(half_height)
    bottom = top[:-1][::-1]
    return top + bottom


if __name__ == "__main__":
    print("=== Star Pyramid ===")
    for row in build_pyramid(5):
        print(row)

    print("\n=== Star Diamond ===")
    for row in build_diamond(4):
        print(row)
