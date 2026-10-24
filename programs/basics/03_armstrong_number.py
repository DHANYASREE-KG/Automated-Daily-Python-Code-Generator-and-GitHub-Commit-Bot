"""
Armstrong Number Checker.

An Armstrong number (narcissistic number) is a number that is the sum of
its own digits each raised to the power of the number of digits.
Example: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
"""


def is_armstrong_number(number: int) -> bool:
    """Return True if the number is an Armstrong number."""
    if number < 0:
        return False

    digits = [int(d) for d in str(number)]
    power = len(digits)
    total_sum = sum(digit**power for digit in digits)

    return total_sum == number


def find_armstrong_numbers(start: int, end: int) -> list[int]:
    """Find all Armstrong numbers in the inclusive range [start, end]."""
    return [num for num in range(start, end + 1) if is_armstrong_number(num)]


if __name__ == "__main__":
    print("=== Armstrong Number Checker ===")
    test_val = 153
    print(f"Is {test_val} an Armstrong number? {is_armstrong_number(test_val)}")
    print(f"Armstrong numbers between 1 and 1000: {find_armstrong_numbers(1, 1000)}")
