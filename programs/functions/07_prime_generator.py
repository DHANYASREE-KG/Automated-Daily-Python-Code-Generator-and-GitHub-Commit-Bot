"""
Infinite Prime Number Generator.

Uses a Python generator (yield) to lazily compute prime numbers one by one.
"""

from typing import Iterator


def is_prime(n: int) -> bool:
    """Check primality."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_stream() -> Iterator[int]:
    """Infinite generator of prime numbers."""
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


if __name__ == "__main__":
    print("=== Lazy Prime Stream ===")
    stream = prime_stream()
    first_15 = [next(stream) for _ in range(15)]
    print(f"First 15 primes: {first_15}")
