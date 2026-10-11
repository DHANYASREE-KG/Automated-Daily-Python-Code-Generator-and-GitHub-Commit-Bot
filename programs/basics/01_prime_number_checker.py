"""
Prime Number Checker and Range Generator.

A prime number is a natural number greater than 1 that cannot be formed
by multiplying two smaller natural numbers.

Sample Run:
    Input: 29
    Output: Is Prime: True
    Primes up to 30: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
"""

import math


def is_prime(number: int) -> bool:
    """
    Check if a given number is prime using the square root trial division method.

    Time Complexity: O(sqrt(n))
    Space Complexity: O(1)
    """
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    # Check potential factors up to square root of number
    limit = int(math.isqrt(number))
    for factor in range(5, limit + 1, 6):
        if number % factor == 0 or number % (factor + 2) == 0:
            return False

    return True


def generate_primes_up_to(limit: int) -> list[int]:
    """Return a list of all prime numbers less than or equal to limit."""
    return [num for num in range(2, limit + 1) if is_prime(num)]


if __name__ == "__main__":
    print("=== Prime Number Checker ===")
    test_number = 29
    print(f"Testing number: {test_number}")
    print(f"Is {test_number} prime? -> {is_prime(test_number)}")

    test_range = 30
    print(f"Primes up to {test_range}: {generate_primes_up_to(test_range)}")
