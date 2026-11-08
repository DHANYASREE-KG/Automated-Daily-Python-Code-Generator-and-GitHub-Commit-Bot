"""
Multiplication Table Formatter.

Generates a formatted multiplication table for a given integer up to a specified limit.
"""


def generate_table(number: int, limit: int = 10) -> list[str]:
    """Generate multiplication table rows as formatted strings."""
    rows = []
    for i in range(1, limit + 1):
        product = number * i
        rows.append(f"{number:2d} x {i:2d} = {product:3d}")
    return rows


if __name__ == "__main__":
    print("=== Multiplication Table ===")
    target = 7
    lines = generate_table(target, 10)
    for line in lines:
        print(line)
