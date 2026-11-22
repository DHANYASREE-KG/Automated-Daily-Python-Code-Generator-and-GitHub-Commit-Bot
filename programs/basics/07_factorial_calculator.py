"""
Factorial and Combinations Calculator.

Computes n! and evaluates permutations nPr and combinations nCr.
"""


def factorial(n: int) -> int:
    """Calculate n! iteratively. Raises ValueError for negative numbers."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def combinations(n: int, r: int) -> int:
    """Calculate nCr (n choose r)."""
    if r < 0 or r > n:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))


if __name__ == "__main__":
    print("=== Factorials and Combinations ===")
    print(f"5! = {factorial(5)}")
    print(f"10! = {factorial(10)}")
    print(f"10 choose 3 = {combinations(10, 3)}")
