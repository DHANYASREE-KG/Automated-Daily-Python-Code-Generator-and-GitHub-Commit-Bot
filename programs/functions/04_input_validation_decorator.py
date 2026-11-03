"""
Input Validator Decorator.

Enforces bounds and conditions on function inputs.
"""

from functools import wraps
from typing import Callable


def validate_positive_integers(func: Callable) -> Callable:
    """Ensure all positional arguments are strictly positive integers."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int) or arg <= 0:
                raise TypeError(f"Argument {arg} must be a positive integer.")
        return func(*args, **kwargs)
    return wrapper


@validate_positive_integers
def calculate_area(length: int, width: int) -> int:
    """Calculate rectangle area."""
    return length * width


if __name__ == "__main__":
    print("=== Input Validation Decorator ===")
    print(f"Valid call (5, 10): {calculate_area(5, 10)}")
    try:
        calculate_area(-3, 10)
    except TypeError as err:
        print(f"Caught expected error: {err}")
