"""
Fibonacci Sequence Generator.

Generates Fibonacci numbers where each number is the sum of the
two preceding ones, usually starting with 0 and 1.

Sample Run:
    Input: 10
    Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
"""


def generate_fibonacci(terms: int) -> list[int]:
    """
    Generate the first N Fibonacci numbers iteratively.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if terms <= 0:
        return []
    if terms == 1:
        return [0]

    sequence = [0, 1]
    while len(sequence) < terms:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)

    return sequence


if __name__ == "__main__":
    print("=== Fibonacci Generator ===")
    count = 10
    fib_series = generate_fibonacci(count)
    print(f"First {count} terms of Fibonacci sequence:")
    print(fib_series)
