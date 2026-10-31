"""
Leap Year and Date Validator.

A year is a leap year if:
1. It is divisible by 4, AND
2. If divisible by 100, it must also be divisible by 400.
"""


def is_leap_year(year: int) -> bool:
    """Determine whether the specified year is a leap year."""
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def days_in_month(month: int, year: int) -> int:
    """Return the total number of days in a given month and year."""
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    if month in {4, 6, 9, 11}:
        return 30
    if month == 2:
        return 29 if is_leap_year(year) else 28
    raise ValueError(f"Invalid month: {month}. Must be between 1 and 12.")


if __name__ == "__main__":
    print("=== Leap Year and Calendar Validator ===")
    years_to_test = [1900, 2000, 2024, 2025, 2026]
    for yr in years_to_test:
        print(f"Year {yr}: Leap Year? {is_leap_year(yr)} (Feb has {days_in_month(2, yr)} days)")
