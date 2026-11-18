"""
Fast Exponentiation (Binary Exponentiation).

Calculates (base^exp) % mod in O(log exp) time.
"""


def fast_power(base: int, exponent: int, modulus: int | None = None) -> int:
    """Compute (base ** exponent) % modulus in logarithmic time."""
    if exponent < 0:
        raise ValueError("Exponent must be non-negative.")

    result = 1
    base = base if modulus is None else base % modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = result * base
            if modulus:
                result %= modulus
        base = base * base
        if modulus:
            base %= modulus
        exponent //= 2

    return result


if __name__ == "__main__":
    print("=== Fast Power Calculator ===")
    print(f"2^10 = {fast_power(2, 10)}")
    print(f"3^13 = {fast_power(3, 13)}")
    print(f"(7^100) % 13 = {fast_power(7, 100, 13)}")
