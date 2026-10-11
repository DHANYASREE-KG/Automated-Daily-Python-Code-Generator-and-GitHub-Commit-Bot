"""
Curated Catalog of Fallback Python Programs.

Contains 70 beginner-friendly, production-ready Python programs across 7 distinct categories:
1. basics
2. strings
3. lists
4. functions
5. oop
6. dsa
7. utilities

Each program contains:
- Complete module docstring
- Educational comments explaining every step
- Self-contained demonstration runner with sample inputs and outputs
- Strict Python syntax compliance
"""

from typing import Any, Dict, List

TEMPLATES: List[Dict[str, Any]] = [
    # =========================================================================
    # 1. BASICS (10 Programs)
    # =========================================================================
    {
        "id": "basics_01",
        "category": "basics",
        "filename": "01_prime_number_checker.py",
        "title": "Prime Number Checker and Range Generator",
        "summary": "Determines whether a number is prime and finds all primes up to N",
        "code": '''"""
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
''',
    },
    {
        "id": "basics_02",
        "category": "basics",
        "filename": "02_fibonacci_generator.py",
        "title": "Fibonacci Sequence Generator",
        "summary": "Generates the Fibonacci sequence up to N terms using iteration",
        "code": '''"""
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
''',
    },
    {
        "id": "basics_03",
        "category": "basics",
        "filename": "03_armstrong_number.py",
        "title": "Armstrong (Narcissistic) Number Detector",
        "summary": "Checks if an integer equals the sum of its own digits each raised to power of digit count",
        "code": '''"""
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
''',
    },
    {
        "id": "basics_04",
        "category": "basics",
        "filename": "04_leap_year_validator.py",
        "title": "Leap Year and Calendar Date Validator",
        "summary": "Checks whether a year is a leap year and validates calendar dates",
        "code": '''"""
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
''',
    },
    {
        "id": "basics_05",
        "category": "basics",
        "filename": "05_multiplication_table.py",
        "title": "Multiplication Table Formatter",
        "summary": "Prints clean multiplication tables with customizable ranges",
        "code": '''"""
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
''',
    },
    {
        "id": "basics_06",
        "category": "basics",
        "filename": "06_star_pattern_printer.py",
        "title": "Star and Pyramid Pattern Printer",
        "summary": "Generates pyramid, inverted pyramid, and diamond star patterns",
        "code": '''"""
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

    print("\\n=== Star Diamond ===")
    for row in build_diamond(4):
        print(row)
''',
    },
    {
        "id": "basics_07",
        "category": "basics",
        "filename": "07_factorial_calculator.py",
        "title": "Factorial Calculator and Combinations",
        "summary": "Computes factorial using iteration and calculates permutations and combinations",
        "code": '''"""
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
''',
    },
    {
        "id": "basics_08",
        "category": "basics",
        "filename": "08_temperature_converter.py",
        "title": "Temperature Converter Unit Utility",
        "summary": "Converts temperatures between Celsius, Fahrenheit, and Kelvin",
        "code": '''"""
Temperature Unit Converter.

Converts temperatures between Celsius, Fahrenheit, and Kelvin scales.
"""


def celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5 / 9


def celsius_to_kelvin(c: float) -> float:
    """Convert Celsius to Kelvin."""
    return c + 273.15


def kelvin_to_celsius(k: float) -> float:
    """Convert Kelvin to Celsius."""
    if k < 0:
        raise ValueError("Absolute zero is 0 Kelvin; temperature cannot be negative.")
    return k - 273.15


if __name__ == "__main__":
    print("=== Temperature Converter ===")
    c = 25.0
    f = celsius_to_fahrenheit(c)
    k = celsius_to_kelvin(c)
    print(f"{c}°C = {f:.2f}°F = {k:.2f}K")
    print(f"Freezing Point: 32°F -> {fahrenheit_to_celsius(32):.1f}°C")
''',
    },
    {
        "id": "basics_09",
        "category": "basics",
        "filename": "09_bmi_calculator.py",
        "title": "Body Mass Index (BMI) Health Calculator",
        "summary": "Calculates BMI and classifies health category based on WHO guidelines",
        "code": '''"""
Body Mass Index (BMI) Calculator.

Formula: BMI = weight (kg) / [height (m)]^2
"""


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI given weight in kilograms and height in meters."""
    if height_m <= 0 or weight_kg <= 0:
        raise ValueError("Height and weight must be positive numbers.")
    return weight_kg / (height_m**2)


def classify_bmi(bmi: float) -> str:
    """Classify BMI into standard WHO categories."""
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25.0:
        return "Normal weight"
    if bmi < 30.0:
        return "Overweight"
    return "Obese"


if __name__ == "__main__":
    print("=== BMI Calculator ===")
    weight = 70.0  # kg
    height = 1.75  # meters
    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)
    print(f"Weight: {weight} kg, Height: {height} m")
    print(f"BMI: {bmi:.2f} ({category})")
''',
    },
    {
        "id": "basics_10",
        "category": "basics",
        "filename": "10_number_guessing_game.py",
        "title": "Deterministic Number Guessing Simulator",
        "summary": "Simulates a binary search number guessing game",
        "code": '''"""
Number Guessing Game Simulator.

Uses binary search strategy to guess a secret number between 1 and 100.
"""


def simulate_game(secret_number: int, low: int = 1, high: int = 100) -> list[dict]:
    """Simulate binary search guesses for a secret number."""
    history = []
    attempts = 0

    while low <= high:
        attempts += 1
        guess = (low + high) // 2
        if guess == secret_number:
            history.append({"attempt": attempts, "guess": guess, "result": "Correct!"})
            break
        elif guess < secret_number:
            history.append({"attempt": attempts, "guess": guess, "result": "Too low"})
            low = guess + 1
        else:
            history.append({"attempt": attempts, "guess": guess, "result": "Too high"})
            high = guess - 1

    return history


if __name__ == "__main__":
    print("=== Number Guessing Simulator ===")
    target = 73
    steps = simulate_game(target)
    for step in steps:
        print(f"Attempt #{step['attempt']}: Guessed {step['guess']} -> {step['result']}")
''',
    },

    # =========================================================================
    # 2. STRINGS (10 Programs)
    # =========================================================================
    {
        "id": "strings_01",
        "category": "strings",
        "filename": "01_palindrome_checker.py",
        "title": "Alphanumeric Palindrome Checker",
        "summary": "Validates if a sentence reads identically forwards and backwards, ignoring non-alphanumeric characters",
        "code": '''"""
Alphanumeric Palindrome Checker.

Ignores casing, punctuation, and whitespace when testing for palindrome properties.
"""

import re


def is_palindrome(text: str) -> bool:
    """Return True if text is a palindrome after stripping non-alphanumeric chars."""
    cleaned = re.sub(r"[^a-zA-Z0-9]", "", text).lower()
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    print("=== Palindrome Checker ===")
    test_phrases = [
        "A man, a plan, a canal: Panama",
        "Race a car",
        "Was it a car or a cat I saw?",
        "No 'x' in Nixon",
    ]
    for phrase in test_phrases:
        print(f"\\"{phrase}\\" -> Palindrome? {is_palindrome(phrase)}")
''',
    },
    {
        "id": "strings_02",
        "category": "strings",
        "filename": "02_anagram_detector.py",
        "title": "Anagram Detector and Frequency Matcher",
        "summary": "Determines whether two strings are anagrams of each other",
        "code": '''"""
Anagram Detector.

Two strings are anagrams if they contain the exact same characters
with the same frequencies, regardless of order.
"""

from collections import Counter


def are_anagrams(str1: str, str2: str) -> bool:
    """Check if str1 and str2 are anagrams, ignoring casing and spaces."""
    clean1 = "".join(str1.lower().split())
    clean2 = "".join(str2.lower().split())
    return Counter(clean1) == Counter(clean2)


if __name__ == "__main__":
    print("=== Anagram Detector ===")
    pairs = [
        ("listen", "silent"),
        ("Debit Card", "Bad Credit"),
        ("hello", "billion"),
    ]
    for w1, w2 in pairs:
        print(f"\\"{w1}\\" and \\"{w2}\\" -> Anagrams? {are_anagrams(w1, w2)}")
''',
    },
    {
        "id": "strings_03",
        "category": "strings",
        "filename": "03_word_frequency_counter.py",
        "title": "Word Frequency Counter and Top-N Analyzer",
        "summary": "Tokenizes text, strips punctuation, and finds the most frequent words",
        "code": '''"""
Word Frequency Counter.

Parses text into words, normalizes casing, and computes frequency counts.
"""

from collections import Counter
import re


def analyze_word_frequencies(text: str, top_n: int = 5) -> list[tuple[str, int]]:
    """Return the top N most frequent words in text."""
    words = re.findall(r"\\b[a-zA-Z0-9_]+\\b", text.lower())
    counter = Counter(words)
    return counter.most_common(top_n)


if __name__ == "__main__":
    sample = """
    Python is an easy to learn, powerful programming language.
    Python has efficient high-level data structures and a simple approach to object-oriented programming.
    """
    print("=== Word Frequency Counter ===")
    top_words = analyze_word_frequencies(sample, top_n=5)
    for word, count in top_words:
        print(f"{word:12s}: {count} occurrences")
''',
    },
    {
        "id": "strings_04",
        "category": "strings",
        "filename": "04_caesar_cipher.py",
        "title": "Caesar Cipher Encryption and Decryption",
        "summary": "Implements the classical Caesar substitution cipher with support for negative shifts",
        "code": '''"""
Caesar Cipher Implementation.

Shifts alphabetical characters by a designated integer key while preserving case.
"""


def caesar_cipher(text: str, shift: int, decrypt: bool = False) -> str:
    """Encrypt or decrypt text using Caesar Cipher."""
    if decrypt:
        shift = -shift

    result = []
    for char in text:
        if "a" <= char <= "z":
            shifted = chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
            result.append(shifted)
        elif "A" <= char <= "Z":
            shifted = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
            result.append(shifted)
        else:
            result.append(char)

    return "".join(result)


if __name__ == "__main__":
    print("=== Caesar Cipher ===")
    original = "Hello, Python Automation 2026!"
    key = 4
    encrypted = caesar_cipher(original, key)
    decrypted = caesar_cipher(encrypted, key, decrypt=True)

    print(f"Original : {original}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
''',
    },
    {
        "id": "strings_05",
        "category": "strings",
        "filename": "05_slug_converter.py",
        "title": "URL Slug and Title Case Converter",
        "summary": "Converts plain text titles into URL-safe slugs and clean title-case headers",
        "code": '''"""
URL Slug and Text Formatter.

Generates SEO-friendly URL slugs from arbitrary strings.
"""

import re
import unicodedata


def generate_slug(text: str) -> str:
    """Convert text into an SEO-friendly kebab-case URL slug."""
    # Normalize unicode characters
    normalized = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    # Replace non-alphanumeric with hyphen
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", normalized).strip("-").lower()
    return slug


if __name__ == "__main__":
    print("=== URL Slug Generator ===")
    titles = [
        "Learn Python 3.12: The Beginner's Guide!",
        "10 Tips & Tricks for GitHub Actions (2026)",
        "What is Data Structures & Algorithms?",
    ]
    for title in titles:
        print(f"Title: {title}")
        print(f"Slug : {generate_slug(title)}\\n")
''',
    },
    {
        "id": "strings_06",
        "category": "strings",
        "filename": "06_vowel_consonant_analyzer.py",
        "title": "Vowel and Consonant Density Analyzer",
        "summary": "Counts vowels, consonants, digits, and whitespace in any given sentence",
        "code": '''"""
Vowel and Consonant Analyzer.

Analyzes letter distribution across English text.
"""


def analyze_characters(text: str) -> dict[str, int]:
    """Count vowels, consonants, digits, and spaces."""
    vowels = set("aeiouAEIOU")
    stats = {"vowels": 0, "consonants": 0, "digits": 0, "spaces": 0, "others": 0}

    for char in text:
        if char in vowels:
            stats["vowels"] += 1
        elif char.isalpha():
            stats["consonants"] += 1
        elif char.isdigit():
            stats["digits"] += 1
        elif char.isspace():
            stats["spaces"] += 1
        else:
            stats["others"] += 1

    return stats


if __name__ == "__main__":
    sample = "Automated Python Bot v1.0 running successfully!"
    print(f"=== Character Analysis for: \\"{sample}\\" ===")
    for category, count in analyze_characters(sample).items():
        print(f"{category.title():12s}: {count}")
''',
    },
    {
        "id": "strings_07",
        "category": "strings",
        "filename": "07_run_length_compression.py",
        "title": "Run-Length String Compression and Decompression",
        "summary": "Compresses repeated characters using run-length encoding (RLE)",
        "code": '''"""
Run-Length Encoding (RLE).

A simple form of lossless data compression where runs of data are stored
as a single data value and count.
"""


def compress_rle(text: str) -> str:
    """Compress consecutive repeated characters (e.g. 'aaabb' -> 'a3b2')."""
    if not text:
        return ""

    encoded = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            encoded.append(f"{text[i - 1]}{count}")
            count = 1
    encoded.append(f"{text[-1]}{count}")
    return "".join(encoded)


if __name__ == "__main__":
    print("=== Run-Length Encoding ===")
    raw = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    compressed = compress_rle(raw)
    print(f"Original length  : {len(raw)} ({raw[:20]}...)")
    print(f"Compressed length: {len(compressed)} ({compressed})")
''',
    },
    {
        "id": "strings_08",
        "category": "strings",
        "filename": "08_sentence_word_reverser.py",
        "title": "Sentence Word Reverser",
        "summary": "Reverses the order of words in a sentence without changing individual letters",
        "code": '''"""
Sentence Word Reverser.

Reverses word sequence while cleaning multiple contiguous spaces.
"""


def reverse_words(sentence: str) -> str:
    """Reverse order of words in a string."""
    words = sentence.strip().split()
    return " ".join(reversed(words))


if __name__ == "__main__":
    print("=== Word Reverser ===")
    phrase = "The quick brown fox jumps over the lazy dog"
    print(f"Original: {phrase}")
    print(f"Reversed: {reverse_words(phrase)}")
''',
    },
    {
        "id": "strings_09",
        "category": "strings",
        "filename": "09_pangram_checker.py",
        "title": "Alphabetical Pangram Checker",
        "summary": "Determines if a sentence contains every letter of the English alphabet",
        "code": '''"""
Pangram Checker.

A pangram is a sentence containing every letter of the alphabet at least once.
"""

import string


def is_pangram(sentence: str) -> tuple[bool, set[str]]:
    """Return whether the string is a pangram and any missing letters."""
    alphabet = set(string.ascii_lowercase)
    present_letters = set(sentence.lower())
    missing = alphabet - present_letters
    return len(missing) == 0, missing


if __name__ == "__main__":
    print("=== Pangram Checker ===")
    s1 = "The quick brown fox jumps over the lazy dog"
    s2 = "Antigravity automated python runner"

    valid1, _ = is_pangram(s1)
    valid2, missing2 = is_pangram(s2)

    print(f"\\"{s1}\\" -> Pangram? {valid1}")
    print(f"\\"{s2}\\" -> Pangram? {valid2} (Missing: {sorted(missing2)})")
''',
    },
    {
        "id": "strings_10",
        "category": "strings",
        "filename": "10_roman_numeral_converter.py",
        "title": "Roman Numeral Converter (To and From)",
        "summary": "Converts integers to Roman numerals and Roman numerals back to integers",
        "code": '''"""
Roman Numeral Converter.

Converts standard integers (1 to 3999) to Roman numerals and parses them back.
"""

NUMERAL_MAP = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
]


def int_to_roman(number: int) -> str:
    """Convert integer to Roman numeral string."""
    if not 1 <= number <= 3999:
        raise ValueError("Number must be between 1 and 3999 inclusive.")
    roman = []
    for val, symbol in NUMERAL_MAP:
        while number >= val:
            roman.append(symbol)
            number -= val
    return "".join(roman)


if __name__ == "__main__":
    print("=== Roman Numeral Converter ===")
    samples = [4, 9, 58, 1994, 2026]
    for num in samples:
        print(f"{num:4d} -> {int_to_roman(num)}")
''',
    },

    # =========================================================================
    # 3. LISTS AND DATA STRUCTURES (10 Programs)
    # =========================================================================
    {
        "id": "lists_01",
        "category": "lists",
        "filename": "01_remove_duplicates.py",
        "title": "Order-Preserving List Deduplication",
        "summary": "Removes duplicate elements from a sequence while strictly preserving original order",
        "code": '''"""
Order-Preserving List Deduplication.

Removes duplicates from a list while keeping the original appearance order.
"""

from typing import Hashable, TypeVar

T = TypeVar("T", bound=Hashable)


def deduplicate_preserve_order(items: list[T]) -> list[T]:
    """Remove duplicates while preserving original order using set lookups."""
    seen: set[T] = set()
    result: list[T] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


if __name__ == "__main__":
    print("=== Order-Preserving Deduplication ===")
    raw_list = [4, 5, 2, 4, 1, 5, 9, 2, 8, 1]
    cleaned = deduplicate_preserve_order(raw_list)
    print(f"Original: {raw_list}")
    print(f"Cleaned : {cleaned}")
''',
    },
    {
        "id": "lists_02",
        "category": "lists",
        "filename": "02_two_sum_solver.py",
        "title": "Two-Sum Target Solver",
        "summary": "Finds indices of two elements in a list that sum to a given target using a hash map",
        "code": '''"""
Two Sum Solver.

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

Time Complexity: O(n)
Space Complexity: O(n)
"""


def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    """Find indices of two numbers that add up to target."""
    seen_map: dict[int, int] = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in seen_map:
            return seen_map[complement], idx
        seen_map[num] = idx
    return None


if __name__ == "__main__":
    print("=== Two Sum Solver ===")
    numbers = [2, 7, 11, 15]
    goal = 9
    indices = two_sum(numbers, goal)
    print(f"Array: {numbers}, Target: {goal}")
    if indices:
        i, j = indices
        print(f"Match found at indices ({i}, {j}): {numbers[i]} + {numbers[j]} = {goal}")
''',
    },
    {
        "id": "lists_03",
        "category": "lists",
        "filename": "03_second_largest_element.py",
        "title": "Second Largest Element Finder",
        "summary": "Finds the second largest distinct number in an array in O(n) single-pass time",
        "code": '''"""
Second Largest Element Finder.

Finds the second distinct maximum value in a list in a single pass.
"""


def find_second_largest(numbers: list[int]) -> int | None:
    """Find the second largest unique number in numbers in O(n) time."""
    if len(numbers) < 2:
        return None

    first = second = float("-inf")
    for num in numbers:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    return int(second) if second != float("-inf") else None


if __name__ == "__main__":
    print("=== Second Largest Element Finder ===")
    data = [12, 35, 1, 10, 34, 35, 1]
    result = find_second_largest(data)
    print(f"List: {data}")
    print(f"Second largest element: {result}")
''',
    },
    {
        "id": "lists_04",
        "category": "lists",
        "filename": "04_flatten_nested_list.py",
        "title": "Arbitrarily Nested List Flattener",
        "summary": "Flattens an arbitrarily deep nested list structure into a flat list",
        "code": '''"""
Arbitrarily Nested List Flattener.

Recursively flattens lists with irregular nesting levels.
"""

from typing import Any


def flatten(nested: list[Any]) -> list[Any]:
    """Flatten an arbitrarily nested list."""
    flat_list = []
    for item in nested:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list


if __name__ == "__main__":
    print("=== Nested List Flattener ===")
    nested_data = [1, [2, [3, 4], 5], [[6]], 7, [8, [9, [10]]]]
    flattened = flatten(nested_data)
    print(f"Nested   : {nested_data}")
    print(f"Flattened: {flattened}")
''',
    },
    {
        "id": "lists_05",
        "category": "lists",
        "filename": "05_matrix_operations.py",
        "title": "Matrix Transposition and 90-Degree Rotation",
        "summary": "Performs 2D matrix transposition and clockwise 90-degree rotation",
        "code": '''"""
Matrix Transposition and Rotation.

Provides matrix operations on 2D lists without external libraries.
"""


def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """Transpose a 2D matrix (swap rows and columns)."""
    if not matrix or not matrix[0]:
        return []
    return [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]


def rotate_matrix_90_clockwise(matrix: list[list[int]]) -> list[list[int]]:
    """Rotate an N x N matrix 90 degrees clockwise."""
    transposed = transpose_matrix(matrix)
    return [row[::-1] for row in transposed]


if __name__ == "__main__":
    print("=== Matrix Operations ===")
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Original:")
    for r in grid:
        print(r)

    print("\\n90° Clockwise Rotated:")
    for r in rotate_matrix_90_clockwise(grid):
        print(r)
''',
    },
    {
        "id": "lists_06",
        "category": "lists",
        "filename": "06_list_chunking.py",
        "title": "List Chunking and Batch Slicer",
        "summary": "Splits a large list into uniform fixed-size batch chunks",
        "code": '''"""
List Chunking Utility.

Partitions a sequence into equal-sized batches.
"""

from typing import TypeVar

T = TypeVar("T")


def chunk_list(items: list[T], chunk_size: int) -> list[list[T]]:
    """Split items into sublists of size chunk_size."""
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]


if __name__ == "__main__":
    print("=== List Chunking Utility ===")
    records = list(range(1, 21))
    batches = chunk_list(records, chunk_size=5)
    print(f"Total elements: {len(records)}")
    for idx, batch in enumerate(batches, start=1):
        print(f"Batch #{idx}: {batch}")
''',
    },
    {
        "id": "lists_07",
        "category": "lists",
        "filename": "07_list_set_operations.py",
        "title": "List Set Operations (Intersection, Union, Difference)",
        "summary": "Computes set intersections, unions, and symmetric differences preserving order",
        "code": '''"""
List Set Operations.

Calculates mathematical set relationships between two lists.
"""


def list_intersection(a: list, b: list) -> list:
    """Return common items in order of appearance in 'a'."""
    b_set = set(b)
    return [item for item in a if item in b_set]


def list_difference(a: list, b: list) -> list:
    """Return items in 'a' but not in 'b'."""
    b_set = set(b)
    return [item for item in a if item not in b_set]


if __name__ == "__main__":
    print("=== List Set Operations ===")
    list_a = [1, 2, 3, 4, 5, 6]
    list_b = [4, 5, 6, 7, 8, 9]

    print(f"A = {list_a}")
    print(f"B = {list_b}")
    print(f"Intersection (A ∩ B): {list_intersection(list_a, list_b)}")
    print(f"Difference (A - B)  : {list_difference(list_a, list_b)}")
''',
    },
    {
        "id": "lists_08",
        "category": "lists",
        "filename": "08_sliding_window_max.py",
        "title": "Sliding Window Maximum Finder",
        "summary": "Computes the maximum element within every sliding window of size K",
        "code": '''"""
Sliding Window Maximum.

Finds the maximum value in every window of size k moving across an array.
"""

from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    """Find maximum of each window of size k in O(n) time using monotonic deque."""
    if not nums or k <= 0:
        return []

    result = []
    window: deque[int] = deque()  # stores indices

    for i in range(len(nums)):
        # Remove elements outside current window
        while window and window[0] <= i - k:
            window.popleft()

        # Remove smaller elements as they are not useful
        while window and nums[window[-1]] < nums[i]:
            window.pop()

        window.append(i)

        if i >= k - 1:
            result.append(nums[window[0]])

    return result


if __name__ == "__main__":
    print("=== Sliding Window Maximum ===")
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    window_size = 3
    print(f"Array: {arr}")
    print(f"Window Size: {window_size}")
    print(f"Window Maxima: {max_sliding_window(arr, window_size)}")
''',
    },
    {
        "id": "lists_09",
        "category": "lists",
        "filename": "09_merge_sorted_lists.py",
        "title": "Merge Two Sorted Lists",
        "summary": "Combines two pre-sorted lists into a single sorted list in O(n+m) time",
        "code": '''"""
Merge Sorted Lists.

Merges two lists that are already sorted into a single sorted list.
"""


def merge_sorted(list1: list[int], list2: list[int]) -> list[int]:
    """Merge two sorted lists in O(n + m) time."""
    merged = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged


if __name__ == "__main__":
    print("=== Merge Two Sorted Lists ===")
    l1 = [1, 3, 7, 9, 15]
    l2 = [2, 4, 6, 8, 10, 12]
    print(f"List 1: {l1}")
    print(f"List 2: {l2}")
    print(f"Merged: {merge_sorted(l1, l2)}")
''',
    },
    {
        "id": "lists_10",
        "category": "lists",
        "filename": "10_dict_inverter.py",
        "title": "Dictionary Inverter with Multi-Value Grouping",
        "summary": "Inverts a key-value dictionary, grouping duplicate values into lists of keys",
        "code": '''"""
Dictionary Inverter with Multi-Value Grouping.

Swaps keys and values in a dictionary. When multiple keys share the same value,
groups them into a list.
"""

from collections import defaultdict


def invert_dict(source: dict[str, str]) -> dict[str, list[str]]:
    """Invert key-value mappings."""
    inverted = defaultdict(list)
    for key, value in source.items():
        inverted[value].append(key)
    return dict(inverted)


if __name__ == "__main__":
    print("=== Dictionary Inverter ===")
    student_grades = {
        "Alice": "A",
        "Bob": "B",
        "Charlie": "A",
        "David": "C",
        "Eve": "B",
    }
    print(f"Original: {student_grades}")
    print(f"Inverted: {invert_dict(student_grades)}")
''',
    },

    # =========================================================================
    # 4. FUNCTIONS AND FUNCTIONAL PROGRAMMING (10 Programs)
    # =========================================================================
    {
        "id": "functions_01",
        "category": "functions",
        "filename": "01_memoized_fibonacci.py",
        "title": "Memoized Fibonacci using Custom Decorator",
        "summary": "Demonstrates Python decorators and memoization caching for high-speed recursion",
        "code": '''"""
Memoized Fibonacci Decorator.

Demonstrates caching function results using a custom memoize decorator.
"""

from functools import wraps
from typing import Callable


def memoize(func: Callable) -> Callable:
    """Decorator to cache return values based on positional arguments."""
    cache: dict = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@memoize
def fibonacci(n: int) -> int:
    """Compute nth Fibonacci number recursively with O(n) memoized time."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print("=== Memoized Fibonacci ===")
    print("Computing fibonacci(50) instantaneously thanks to caching:")
    print(f"fibonacci(50) = {fibonacci(50)}")
''',
    },
    {
        "id": "functions_02",
        "category": "functions",
        "filename": "02_custom_map_filter_reduce.py",
        "title": "Custom Higher-Order Map, Filter, and Reduce",
        "summary": "Implements core functional programming primitives using pure Python loops",
        "code": '''"""
Custom Higher-Order Functions.

Builds custom map, filter, and reduce utilities to explore functional concepts.
"""

from typing import Callable, Iterable, TypeVar

T = TypeVar("T")
R = TypeVar("R")


def my_map(func: Callable[[T], R], items: Iterable[T]) -> list[R]:
    """Custom implementation of map()."""
    return [func(item) for item in items]


def my_filter(predicate: Callable[[T], bool], items: Iterable[T]) -> list[T]:
    """Custom implementation of filter()."""
    return [item for item in items if predicate(item)]


def my_reduce(func: Callable[[R, T], R], items: Iterable[T], initial: R) -> R:
    """Custom implementation of functools.reduce()."""
    accumulator = initial
    for item in items:
        accumulator = func(accumulator, item)
    return accumulator


if __name__ == "__main__":
    print("=== Custom Higher-Order Functions ===")
    numbers = [1, 2, 3, 4, 5, 6]

    doubled = my_map(lambda x: x * 2, numbers)
    evens = my_filter(lambda x: x % 2 == 0, numbers)
    total_sum = my_reduce(lambda acc, x: acc + x, numbers, 0)

    print(f"Original : {numbers}")
    print(f"Doubled  : {doubled}")
    print(f"Evens    : {evens}")
    print(f"Sum      : {total_sum}")
''',
    },
    {
        "id": "functions_03",
        "category": "functions",
        "filename": "03_execution_timer_decorator.py",
        "title": "Execution Timer and Performance Decorator",
        "summary": "Measures and logs function elapsed wall-clock execution time",
        "code": '''"""
Execution Timer Decorator.

Measures elapsed execution time of functions with high precision.
"""

from functools import wraps
import time
from typing import Callable


def time_it(func: Callable) -> Callable:
    """Measure elapsed execution time of the decorated function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[{func.__name__}] Execution time: {elapsed * 1000:.3f} ms")
        return result
    return wrapper


@time_it
def compute_sum_of_squares(limit: int) -> int:
    """Calculate sum of squares up to limit."""
    return sum(i * i for i in range(limit))


if __name__ == "__main__":
    print("=== Execution Timer Decorator ===")
    res = compute_sum_of_squares(100_000)
    print(f"Result length: {len(str(res))} digits")
''',
    },
    {
        "id": "functions_04",
        "category": "functions",
        "filename": "04_input_validation_decorator.py",
        "title": "Input Type and Range Validator Decorator",
        "summary": "Validates function argument types and bounds before execution",
        "code": '''"""
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
''',
    },
    {
        "id": "functions_05",
        "category": "functions",
        "filename": "05_tower_of_hanoi.py",
        "title": "Tower of Hanoi Recursive Solver",
        "summary": "Solves the classical Tower of Hanoi puzzle printing disk transfer movements",
        "code": '''"""
Tower of Hanoi Solver.

Classic recursion problem moving n disks from source peg to target peg using an auxiliary peg.
"""


def solve_hanoi(n: int, source: str, target: str, auxiliary: str) -> list[str]:
    """Generate sequence of disk movements to solve Tower of Hanoi."""
    moves = []

    def _hanoi(disks, src, tgt, aux):
        if disks == 1:
            moves.append(f"Move disk 1 from {src} to {tgt}")
            return
        _hanoi(disks - 1, src, aux, tgt)
        moves.append(f"Move disk {disks} from {src} to {tgt}")
        _hanoi(disks - 1, aux, tgt, src)

    _hanoi(n, source, target, auxiliary)
    return moves


if __name__ == "__main__":
    print("=== Tower of Hanoi (3 Disks) ===")
    steps = solve_hanoi(3, "A", "C", "B")
    for step in steps:
        print(step)
''',
    },
    {
        "id": "functions_06",
        "category": "functions",
        "filename": "06_fast_power_calculator.py",
        "title": "Fast Modular Exponentiation (Binary Power)",
        "summary": "Computes base^exp in O(log exp) time using divide-and-conquer binary exponentiation",
        "code": '''"""
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
''',
    },
    {
        "id": "functions_07",
        "category": "functions",
        "filename": "07_prime_generator.py",
        "title": "Infinite Prime Number Generator Stream",
        "summary": "Implements a Python generator function yielding primes on-demand with lazy evaluation",
        "code": '''"""
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
''',
    },
    {
        "id": "functions_08",
        "category": "functions",
        "filename": "08_currying_utility.py",
        "title": "Function Currying and Partial Application",
        "summary": "Transforms multi-argument functions into chains of single-argument functions",
        "code": '''"""
Function Currying Utility.

Currying transforms a function f(a, b, c) into f(a)(b)(c).
"""

from typing import Callable


def curry_2(func: Callable) -> Callable:
    """Curry a 2-argument function."""
    def curried(a):
        return lambda b: func(a, b)
    return curried


def multiply(x: int, y: int) -> int:
    return x * y


if __name__ == "__main__":
    print("=== Currying Utility ===")
    curried_mult = curry_2(multiply)
    double = curried_mult(2)
    triple = curried_mult(3)

    print(f"double(10): {double(10)}")
    print(f"triple(10): {triple(10)}")
''',
    },
    {
        "id": "functions_09",
        "category": "functions",
        "filename": "09_retry_decorator.py",
        "title": "Retry Decorator with Exponential Backoff",
        "summary": "Automatically retries failing operations with configurable attempts and exponential delay",
        "code": '''"""
Retry Decorator with Exponential Backoff.

Resilient execution wrapper for functions prone to intermittent failures.
"""

from functools import wraps
import time
from typing import Callable


def retry(max_attempts: int = 3, initial_delay: float = 0.05, backoff_factor: float = 2.0):
    """Decorator to retry a function upon exception."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            delay = initial_delay
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    if attempt == max_attempts:
                        raise err
                    time.sleep(delay)
                    delay *= backoff_factor
        return wrapper
    return decorator


if __name__ == "__main__":
    print("=== Retry Decorator Simulation ===")
    call_count = 0

    @retry(max_attempts=3, initial_delay=0.01)
    def flaky_operation():
        nonlocal call_count
        call_count += 1
        if call_count < 3:
            raise ConnectionError(f"Temporary network blip (attempt {call_count})")
        return "Success on attempt 3!"

    result = flaky_operation()
    print(f"Operation completed: {result}")
''',
    },
    {
        "id": "functions_10",
        "category": "functions",
        "filename": "10_pipeline_transformer.py",
        "title": "Functional Data Pipeline Transformer",
        "summary": "Composes functions sequentially into an executable data processing pipeline",
        "code": '''"""
Pipeline Transformer.

Composes multiple unary functions into a single pipeline.
"""

from typing import Any, Callable


class Pipeline:
    """A callable pipeline of functions."""

    def __init__(self, *steps: Callable[[Any], Any]):
        self.steps = steps

    def run(self, initial_value: Any) -> Any:
        value = initial_value
        for step in self.steps:
            value = step(value)
        return value


if __name__ == "__main__":
    print("=== Functional Pipeline ===")
    pipe = Pipeline(
        str.strip,
        str.lower,
        lambda s: s.replace(" ", "_"),
        lambda s: f"prefix_{s}_suffix"
    )

    test_input = "  Hello World Python  "
    print(f"Input : '{test_input}'")
    print(f"Output: '{pipe.run(test_input)}'")
''',
    },

    # =========================================================================
    # 5. OBJECT-ORIENTED PROGRAMMING (10 Programs)
    # =========================================================================
    {
        "id": "oop_01",
        "category": "oop",
        "filename": "01_bank_account_simulator.py",
        "title": "Bank Account Simulator with Transaction Ledger",
        "summary": "Encapsulates balance, deposits, withdrawals, and immutable transaction history",
        "code": '''"""
Bank Account Simulator.

Demonstrates OOP encapsulation, validation, and transaction tracking.
"""

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class Transaction:
    type: str
    amount: float
    timestamp: str


class BankAccount:
    """Represents a bank account with safety checks and ledger history."""

    def __init__(self, owner: str, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self._balance = initial_balance
        self._transactions: list[Transaction] = []

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        self._record_transaction("DEPOSIT", amount)

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError(f"Insufficient funds: available {self._balance:.2f}, requested {amount:.2f}")
        self._balance -= amount
        self._record_transaction("WITHDRAWAL", amount)

    def _record_transaction(self, tx_type: str, amount: float) -> None:
        tx = Transaction(type=tx_type, amount=amount, timestamp=datetime.now(timezone.utc).isoformat())
        self._transactions.append(tx)

    def print_statement(self) -> None:
        print(f"--- Statement for {self.owner} ---")
        for tx in self._transactions:
            print(f"[{tx.timestamp[:19]}] {tx.type:10s}: ${tx.amount:.2f}")
        print(f"Current Balance: ${self._balance:.2f}")


if __name__ == "__main__":
    print("=== Bank Account Simulation ===")
    acc = BankAccount("Dhanyasree", 500.0)
    acc.deposit(250.0)
    acc.withdraw(100.0)
    acc.print_statement()
''',
    },
    {
        "id": "oop_02",
        "category": "oop",
        "filename": "02_library_management_system.py",
        "title": "Library Book Management and Checkout System",
        "summary": "Manages book catalog, borrowing states, patrons, and due dates",
        "code": '''"""
Library Management System.

Demonstrates association between Book, Member, and Library classes.
"""


class Book:
    """Represents an individual book in catalog."""

    def __init__(self, isbn: str, title: str, author: str):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_checked_out = False

    def __repr__(self) -> str:
        return f"Book('{self.title}' by {self.author}, ISBN: {self.isbn})"


class Library:
    """Manages collection of books and checkout logic."""

    def __init__(self, name: str):
        self.name = name
        self.catalog: dict[str, Book] = {}

    def add_book(self, book: Book) -> None:
        self.catalog[book.isbn] = book

    def checkout_book(self, isbn: str) -> Book:
        book = self.catalog.get(isbn)
        if not book:
            raise KeyError(f"Book with ISBN {isbn} not found.")
        if book.is_checked_out:
            raise ValueError(f"'{book.title}' is currently checked out.")
        book.is_checked_out = True
        return book

    def return_book(self, isbn: str) -> None:
        book = self.catalog.get(isbn)
        if book:
            book.is_checked_out = False


if __name__ == "__main__":
    print("=== Library Management System ===")
    lib = Library("City Central Library")
    b1 = Book("978-0132350884", "Clean Code", "Robert C. Martin")
    b2 = Book("978-0134685991", "Effective Java", "Joshua Bloch")

    lib.add_book(b1)
    lib.add_book(b2)

    borrowed = lib.checkout_book("978-0132350884")
    print(f"Checked out: {borrowed.title}")
    lib.return_book("978-0132350884")
    print(f"Returned successfully. Is checked out? {b1.is_checked_out}")
''',
    },
    {
        "id": "oop_03",
        "category": "oop",
        "filename": "03_student_grading_system.py",
        "title": "Student Grading System and GPA Calculator",
        "summary": "Computes grades, GPAs, and class statistics with class encapsulation",
        "code": '''"""
Student Grading System.

Tracks grades across courses and computes overall GPA.
"""


class Student:
    """Represents a student with grades in multiple courses."""

    GRADE_POINTS = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}

    def __init__(self, student_id: str, name: str):
        self.student_id = student_id
        self.name = name
        self.courses: dict[str, str] = {}  # course_code -> letter_grade

    def add_grade(self, course: str, grade: str) -> None:
        grade = grade.upper()
        if grade not in self.GRADE_POINTS:
            raise ValueError(f"Invalid grade: {grade}")
        self.courses[course] = grade

    def calculate_gpa(self) -> float:
        if not self.courses:
            return 0.0
        total_pts = sum(self.GRADE_POINTS[g] for g in self.courses.values())
        return total_pts / len(self.courses)


if __name__ == "__main__":
    print("=== Student GPA Tracker ===")
    s = Student("STU101", "Alex")
    s.add_grade("CS101", "A")
    s.add_grade("MATH201", "B")
    s.add_grade("ENG102", "A")

    print(f"Student: {s.name}")
    print(f"Courses: {s.courses}")
    print(f"GPA    : {s.calculate_gpa():.2f}")
''',
    },
    {
        "id": "oop_04",
        "category": "oop",
        "filename": "04_inventory_manager.py",
        "title": "Inventory Item Stock Management",
        "summary": "Tracks product inventory, stock threshold reorders, and valuations",
        "code": '''"""
Inventory Stock Management.

Tracks warehouse products, pricing, stock levels, and automated reorder alerts.
"""


class Product:
    def __init__(self, sku: str, name: str, price: float, quantity: int, reorder_level: int = 10):
        self.sku = sku
        self.name = name
        self.price = price
        self.quantity = quantity
        self.reorder_level = reorder_level

    @property
    def total_value(self) -> float:
        return self.price * self.quantity

    def needs_reorder(self) -> bool:
        return self.quantity <= self.reorder_level


class Warehouse:
    def __init__(self):
        self.items: dict[str, Product] = {}

    def add_product(self, p: Product) -> None:
        self.items[p.sku] = p

    def total_valuation(self) -> float:
        return sum(p.total_value for p in self.items.values())

    def get_reorder_alerts(self) -> list[str]:
        return [p.name for p in self.items.values() if p.needs_reorder()]


if __name__ == "__main__":
    print("=== Warehouse Inventory ===")
    wh = Warehouse()
    wh.add_product(Product("SKU-1", "Wireless Keyboard", 45.0, 5, reorder_level=10))
    wh.add_product(Product("SKU-2", "USB-C Hub", 29.99, 40, reorder_level=15))

    print(f"Total Valuation: ${wh.total_valuation():.2f}")
    print(f"Items needing reorder: {wh.get_reorder_alerts()}")
''',
    },
    {
        "id": "oop_05",
        "category": "oop",
        "filename": "05_vehicle_inheritance.py",
        "title": "Vehicle Polymorphic Class Hierarchy",
        "summary": "Demonstrates inheritance, method overriding, and super() calls",
        "code": '''"""
Vehicle Inheritance Hierarchy.

Demonstrates OOP inheritance, polymorphism, and abstract method patterns.
"""


class Vehicle:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def describe(self) -> str:
        return f"{self.year} {self.brand} {self.model}"

    def fuel_type(self) -> str:
        return "Unknown"


class ElectricCar(Vehicle):
    def __init__(self, brand: str, model: str, year: int, battery_kwh: float):
        super().__init__(brand, model, year)
        self.battery_kwh = battery_kwh

    def fuel_type(self) -> str:
        return f"Electric ({self.battery_kwh} kWh)"


class GasolineCar(Vehicle):
    def fuel_type(self) -> str:
        return "Gasoline"


if __name__ == "__main__":
    print("=== Vehicle Polymorphic Hierarchy ===")
    fleet: list[Vehicle] = [
        ElectricCar("Tesla", "Model 3", 2024, 75.0),
        GasolineCar("Toyota", "Camry", 2023),
    ]
    for v in fleet:
        print(f"{v.describe()} -> Fuel: {v.fuel_type()}")
''',
    },
    {
        "id": "oop_06",
        "category": "oop",
        "filename": "06_shape_polymorphism.py",
        "title": "Geometric Shape Polymorphism and Calculations",
        "summary": "Uses abstract base classes (ABC) to calculate area and perimeter across shapes",
        "code": '''"""
Geometric Shape Polymorphism.

Demonstrates Abstract Base Classes (ABC) and method overrides.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Calculate shape area."""

    @abstractmethod
    def perimeter(self) -> float:
        """Calculate shape perimeter."""


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius * self.radius

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


if __name__ == "__main__":
    print("=== Shape Polymorphism ===")
    shapes: list[Shape] = [Circle(5.0), Rectangle(4.0, 6.0)]
    for s in shapes:
        print(f"{s.__class__.__name__:10s} -> Area: {s.area():.2f}, Perimeter: {s.perimeter():.2f}")
''',
    },
    {
        "id": "oop_07",
        "category": "oop",
        "filename": "07_shopping_cart.py",
        "title": "E-Commerce Shopping Cart with Discounts and Tax",
        "summary": "Models shopping cart items, promo codes, sales tax, and checkout totals",
        "code": '''"""
E-Commerce Shopping Cart.

Calculates subtotal, discounts, tax, and final checkout totals.
"""


class CartItem:
    def __init__(self, name: str, unit_price: float, quantity: int = 1):
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity

    @property
    def total_price(self) -> float:
        return self.unit_price * self.quantity


class ShoppingCart:
    def __init__(self, tax_rate: float = 0.08):
        self.items: list[CartItem] = []
        self.tax_rate = tax_rate

    def add_item(self, item: CartItem) -> None:
        self.items.append(item)

    @property
    def subtotal(self) -> float:
        return sum(item.total_price for item in self.items)

    def calculate_total(self, discount_percent: float = 0.0) -> dict[str, float]:
        sub = self.subtotal
        disc = sub * (discount_percent / 100)
        tax = (sub - disc) * self.tax_rate
        final = (sub - disc) + tax
        return {"subtotal": sub, "discount": disc, "tax": tax, "final": final}


if __name__ == "__main__":
    print("=== Shopping Cart ===")
    cart = ShoppingCart(tax_rate=0.07)
    cart.add_item(CartItem("Wireless Mouse", 25.0, 2))
    cart.add_item(CartItem("Mechanical Keyboard", 80.0, 1))

    receipt = cart.calculate_total(discount_percent=10.0)
    for k, v in receipt.items():
        print(f"{k.capitalize():10s}: ${v:.2f}")
''',
    },
    {
        "id": "oop_08",
        "category": "oop",
        "filename": "08_employee_payroll.py",
        "title": "Employee Payroll and Compensation Models",
        "summary": "Models salaried and hourly employees with custom paycheck computations",
        "code": '''"""
Employee Payroll Models.

Calculates net pay for Salaried and Hourly staff using polymorphism.
"""

from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, emp_id: str, name: str):
        self.emp_id = emp_id
        self.name = name

    @abstractmethod
    def calculate_paycheck(self) -> float:
        """Calculate gross pay for the pay period."""


class SalariedEmployee(Employee):
    def __init__(self, emp_id: str, name: str, annual_salary: float):
        super().__init__(emp_id, name)
        self.annual_salary = annual_salary

    def calculate_paycheck(self) -> float:
        # 26 bi-weekly pay periods per year
        return self.annual_salary / 26


class HourlyEmployee(Employee):
    def __init__(self, emp_id: str, name: str, hourly_rate: float, hours_worked: float):
        super().__init__(emp_id, name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_paycheck(self) -> float:
        regular_hours = min(40.0, self.hours_worked)
        overtime_hours = max(0.0, self.hours_worked - 40.0)
        return (regular_hours * self.hourly_rate) + (overtime_hours * self.hourly_rate * 1.5)


if __name__ == "__main__":
    print("=== Employee Payroll ===")
    staff: list[Employee] = [
        SalariedEmployee("E1", "Dana", 104_000.0),
        HourlyEmployee("E2", "Leo", 25.0, 45.0),
    ]
    for emp in staff:
        print(f"[{emp.emp_id}] {emp.name:10s} -> Paycheck: ${emp.calculate_paycheck():.2f}")
''',
    },
    {
        "id": "oop_09",
        "category": "oop",
        "filename": "09_coffee_machine.py",
        "title": "Stateful Coffee Machine Simulator",
        "summary": "Maintains water, milk, and coffee bean resource levels across brews",
        "code": '''"""
Stateful Coffee Machine Simulator.

Manages resource levels and drink orders.
"""


class CoffeeMachine:
    def __init__(self, water_ml: int = 1000, milk_ml: int = 500, beans_g: int = 200):
        self.water_ml = water_ml
        self.milk_ml = milk_ml
        self.beans_g = beans_g

    def brew_espresso(self) -> str:
        if self.water_ml < 50 or self.beans_g < 18:
            return "Refill needed: insufficient water or coffee beans for Espresso."
        self.water_ml -= 50
        self.beans_g -= 18
        return "Enjoy your rich Espresso!"

    def brew_latte(self) -> str:
        if self.water_ml < 50 or self.milk_ml < 150 or self.beans_g < 18:
            return "Refill needed: insufficient resources for Latte."
        self.water_ml -= 50
        self.milk_ml -= 150
        self.beans_g -= 18
        return "Enjoy your creamy Latte!"


if __name__ == "__main__":
    print("=== Coffee Machine Simulator ===")
    cm = CoffeeMachine()
    print(cm.brew_espresso())
    print(cm.brew_latte())
    print(f"Remaining resources: Water={cm.water_ml}ml, Milk={cm.milk_ml}ml, Beans={cm.beans_g}g")
''',
    },
    {
        "id": "oop_10",
        "category": "oop",
        "filename": "10_card_deck_simulator.py",
        "title": "Standard Card Deck and Shuffling Engine",
        "summary": "Models a 52-card playing deck with deterministic dealing and shuffling",
        "code": '''"""
Playing Card Deck Engine.

Models 52-card deck with suits, ranks, and dealing mechanics.
"""

import random


class Card:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = [Card(r, s) for s in Card.SUITS for r in Card.RANKS]

    def shuffle(self, seed: int = 42) -> None:
        random.seed(seed)
        random.shuffle(self.cards)

    def deal(self, count: int) -> list[Card]:
        if count > len(self.cards):
            raise ValueError("Not enough cards in deck.")
        dealt = self.cards[:count]
        self.cards = self.cards[count:]
        return dealt


if __name__ == "__main__":
    print("=== Card Deck Simulator ===")
    d = Deck()
    d.shuffle(seed=2026)
    hand = d.deal(5)
    print("Dealt 5-card poker hand:")
    for card in hand:
        print(f" - {card}")
''',
    },

    # =========================================================================
    # 6. DATA STRUCTURES AND ALGORITHMS (DSA) (10 Programs)
    # =========================================================================
    {
        "id": "dsa_01",
        "category": "dsa",
        "filename": "01_binary_search.py",
        "title": "Binary Search Algorithm",
        "summary": "Performs logarithmic search on a sorted list with iterative and recursive variants",
        "code": '''"""
Binary Search Algorithm.

Finds target position within a sorted list in O(log n) time.
"""


def binary_search(sorted_arr: list[int], target: int) -> int:
    """Return index of target in sorted_arr, or -1 if not found."""
    left = 0
    right = len(sorted_arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_arr[mid] == target:
            return mid
        elif sorted_arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    print("=== Binary Search ===")
    data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    query = 23
    idx = binary_search(data, query)
    print(f"Array : {data}")
    print(f"Target: {query} found at index: {idx}")
''',
    },
    {
        "id": "dsa_02",
        "category": "dsa",
        "filename": "02_bubble_and_selection_sort.py",
        "title": "Bubble Sort and Selection Sort Algorithms",
        "summary": "Implements classical O(n^2) comparison-based sorting algorithms for learning",
        "code": '''"""
Bubble Sort and Selection Sort.

Classical sorting algorithms comparing adjacent and minimum elements.
"""


def bubble_sort(arr: list[int]) -> list[int]:
    """In-place optimized Bubble Sort."""
    n = len(arr)
    data = arr.copy()
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break
    return data


def selection_sort(arr: list[int]) -> list[int]:
    """Selection Sort by repeatedly finding minimum element."""
    data = arr.copy()
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data


if __name__ == "__main__":
    print("=== Comparison Sorting Algorithms ===")
    sample = [64, 25, 12, 22, 11]
    print(f"Raw Array      : {sample}")
    print(f"Bubble Sorted   : {bubble_sort(sample)}")
    print(f"Selection Sorted: {selection_sort(sample)}")
''',
    },
    {
        "id": "dsa_03",
        "category": "dsa",
        "filename": "03_merge_sort.py",
        "title": "Merge Sort Algorithm",
        "summary": "Divides array recursively and merges sorted halves in O(n log n) stable time",
        "code": '''"""
Merge Sort Algorithm.

A divide-and-conquer algorithm that produces a stable sort in O(n log n) time.
"""


def merge_sort(arr: list[int]) -> list[int]:
    """Recursively sort array using Merge Sort."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)


def _merge(left: list[int], right: list[int]) -> list[int]:
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


if __name__ == "__main__":
    print("=== Merge Sort ===")
    items = [38, 27, 43, 3, 9, 82, 10]
    print(f"Unsorted: {items}")
    print(f"Sorted  : {merge_sort(items)}")
''',
    },
    {
        "id": "dsa_04",
        "category": "dsa",
        "filename": "04_quick_sort.py",
        "title": "Quick Sort Algorithm",
        "summary": "Partitions array around a pivot element in O(n log n) average time",
        "code": '''"""
Quick Sort Algorithm.

Divide-and-conquer sorting by choosing a pivot and partitioning elements.
"""


def quick_sort(arr: list[int]) -> list[int]:
    """Sort list using Quick Sort algorithm."""
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    print("=== Quick Sort ===")
    raw = [10, 7, 8, 9, 1, 5]
    print(f"Input : {raw}")
    print(f"Sorted: {quick_sort(raw)}")
''',
    },
    {
        "id": "dsa_05",
        "category": "dsa",
        "filename": "05_stack_data_structure.py",
        "title": "Stack Data Structure (LIFO)",
        "summary": "Implements Last-In-First-Out stack with push, pop, peek, and capacity limits",
        "code": '''"""
Stack Data Structure (LIFO).

Last-In, First-Out collection with constant O(1) operations.
"""

from typing import Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self):
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("peek at empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)


if __name__ == "__main__":
    print("=== Stack (LIFO) ===")
    s = Stack[int]()
    s.push(10)
    s.push(20)
    s.push(30)
    print(f"Top element (peek): {s.peek()}")
    print(f"Popped: {s.pop()}")
    print(f"Remaining size: {s.size()}")
''',
    },
    {
        "id": "dsa_06",
        "category": "dsa",
        "filename": "06_queue_data_structure.py",
        "title": "Queue Data Structure (FIFO)",
        "summary": "Implements First-In-First-Out queue using collections.deque with O(1) enqueue and dequeue",
        "code": '''"""
Queue Data Structure (FIFO).

First-In, First-Out collection with O(1) enqueue and dequeue operations.
"""

from collections import deque
from typing import Generic, TypeVar

T = TypeVar("T")


class Queue(Generic[T]):
    def __init__(self):
        self._items: deque[T] = deque()

    def enqueue(self, item: T) -> None:
        self._items.append(item)

    def dequeue(self) -> T:
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def front(self) -> T:
        if self.is_empty():
            raise IndexError("front of empty queue")
        return self._items[0]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)


if __name__ == "__main__":
    print("=== Queue (FIFO) ===")
    q = Queue[str]()
    q.enqueue("Alice")
    q.enqueue("Bob")
    q.enqueue("Charlie")
    print(f"Front: {q.front()}")
    print(f"Dequeued: {q.dequeue()}")
    print(f"Next front: {q.front()}")
''',
    },
    {
        "id": "dsa_07",
        "category": "dsa",
        "filename": "07_singly_linked_list.py",
        "title": "Singly Linked List with Reversal",
        "summary": "Implements linked list nodes, head/tail appends, and in-place pointer reversal",
        "code": '''"""
Singly Linked List.

Basic node pointer structure supporting traversal and in-place reversal.
"""

from typing import Any, Optional


class Node:
    def __init__(self, value: Any, next_node: Optional["Node"] = None):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def reverse(self) -> None:
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def to_list(self) -> list[Any]:
        result = []
        curr = self.head
        while curr:
            result.append(curr.value)
            curr = curr.next
        return result


if __name__ == "__main__":
    print("=== Singly Linked List ===")
    ll = LinkedList()
    for val in [10, 20, 30, 40]:
        ll.append(val)
    print(f"Original: {ll.to_list()}")
    ll.reverse()
    print(f"Reversed: {ll.to_list()}")
''',
    },
    {
        "id": "dsa_08",
        "category": "dsa",
        "filename": "08_valid_parentheses.py",
        "title": "Valid Parentheses and Bracket Validator",
        "summary": "Uses a stack to validate proper nesting of round, curly, and square brackets",
        "code": '''"""
Valid Parentheses Validator.

Given a string containing '(', ')', '{', '}', '[' and ']',
determines if the input string is valid.
"""


def is_valid_parentheses(s: str) -> bool:
    """Validate properly closed and nested brackets in O(n) time."""
    bracket_map = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()

    return len(stack) == 0


if __name__ == "__main__":
    print("=== Valid Parentheses Checker ===")
    test_cases = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    for exp in test_cases:
        print(f"Expression: {exp:8s} -> Valid? {is_valid_parentheses(exp)}")
''',
    },
    {
        "id": "dsa_09",
        "category": "dsa",
        "filename": "09_binary_search_tree.py",
        "title": "Binary Search Tree (BST) Insertion and Inorder Traversal",
        "summary": "Implements BST node insertion, search, and sorted inorder tree traversal",
        "code": '''"""
Binary Search Tree (BST).

Maintains sorted hierarchy where left node < root < right node.
"""

from typing import Optional


class TreeNode:
    def __init__(self, key: int):
        self.key = key
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class BinarySearchTree:
    def __init__(self):
        self.root: Optional[TreeNode] = None

    def insert(self, key: int) -> None:
        self.root = self._insert(self.root, key)

    def _insert(self, node: Optional[TreeNode], key: int) -> TreeNode:
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def inorder(self) -> list[int]:
        res: list[int] = []

        def _traverse(node):
            if node:
                _traverse(node.left)
                res.append(node.key)
                _traverse(node.right)

        _traverse(self.root)
        return res


if __name__ == "__main__":
    print("=== Binary Search Tree ===")
    bst = BinarySearchTree()
    for val in [50, 30, 20, 40, 70, 60, 80]:
        bst.insert(val)
    print(f"Inorder Traversal (Sorted): {bst.inorder()}")
''',
    },
    {
        "id": "dsa_10",
        "category": "dsa",
        "filename": "10_graph_bfs_traversal.py",
        "title": "Graph Representation and Breadth-First Search (BFS)",
        "summary": "Traverses an adjacency list graph level-by-level using a FIFO queue",
        "code": '''"""
Graph Breadth-First Search (BFS).

Traverses nodes level-by-level using a queue.
"""

from collections import deque


class Graph:
    def __init__(self):
        self.adj: dict[str, list[str]] = {}

    def add_edge(self, u: str, v: str) -> None:
        self.adj.setdefault(u, []).append(v)
        self.adj.setdefault(v, []).append(u)

    def bfs(self, start_node: str) -> list[str]:
        visited = set([start_node])
        queue = deque([start_node])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in self.adj.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order


if __name__ == "__main__":
    print("=== Graph BFS Traversal ===")
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "E")
    print(f"BFS Order from node 'A': {g.bfs('A')}")
''',
    },

    # =========================================================================
    # 7. UTILITIES AND REAL-WORLD TOOLS (10 Programs)
    # =========================================================================
    {
        "id": "utilities_01",
        "category": "utilities",
        "filename": "01_text_file_analyzer.py",
        "title": "Text File and Character Count Analyzer",
        "summary": "Analyzes text streams computing line counts, word counts, and average word lengths",
        "code": '''"""
Text Analyzer Utility.

Calculates lines, words, character density, and readability averages.
"""


def analyze_text(content: str) -> dict[str, float]:
    """Calculate core statistics of a given text block."""
    lines = content.splitlines()
    words = content.split()
    chars_no_spaces = len("".join(words))

    avg_word_len = (chars_no_spaces / len(words)) if words else 0.0

    return {
        "line_count": len(lines),
        "word_count": len(words),
        "char_count": len(content),
        "avg_word_length": round(avg_word_len, 2),
    }


if __name__ == "__main__":
    print("=== Text Analyzer ===")
    sample_text = """Automated GitHub commit bot.
Built with clean Python and GitHub Actions.
Supports scheduled daily runs with zero manual intervention."""

    stats = analyze_text(sample_text)
    for metric, value in stats.items():
        print(f"{metric.replace('_', ' ').title():20s}: {value}")
''',
    },
    {
        "id": "utilities_02",
        "category": "utilities",
        "filename": "02_csv_data_summary.py",
        "title": "CSV Data Summary and Aggregation Engine",
        "summary": "Parses CSV records without external libraries and computes min, max, mean, and sum",
        "code": '''"""
CSV Summary and Aggregation Utility.

Parses comma-separated text and aggregates numerical columns.
"""

import csv
import io


def summarize_csv_column(csv_data: str, column_name: str) -> dict[str, float]:
    """Calculate sum, mean, min, and max of a numerical CSV column."""
    reader = csv.DictReader(io.StringIO(csv_data.strip()))
    values = []

    for row in reader:
        if column_name in row and row[column_name]:
            try:
                values.append(float(row[column_name]))
            except ValueError:
                pass

    if not values:
        raise ValueError(f"No numeric data found for column: {column_name}")

    return {
        "count": len(values),
        "sum": round(sum(values), 2),
        "mean": round(sum(values) / len(values), 2),
        "min": min(values),
        "max": max(values),
    }


if __name__ == "__main__":
    print("=== CSV Data Summarizer ===")
    sample_csv = """product,price,units
Laptop,1200.50,5
Mouse,25.00,40
Monitor,299.99,12
Keyboard,79.99,25
"""
    results = summarize_csv_column(sample_csv, "price")
    for stat, val in results.items():
        print(f"{stat.title():8s}: {val}")
''',
    },
    {
        "id": "utilities_03",
        "category": "utilities",
        "filename": "03_password_generator.py",
        "title": "Secure Password Generator and Entropy Evaluator",
        "summary": "Generates cryptographically secure passwords and evaluates complexity",
        "code": '''"""
Secure Password Generator and Evaluator.

Generates passwords with balanced character types using the secrets module.
"""

import secrets
import string


def generate_password(length: int = 16, include_symbols: bool = True) -> str:
    """Generate a cryptographically secure random password."""
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")

    chars = string.ascii_letters + string.digits
    if include_symbols:
        chars += "!@#$%^&*()-_=+"

    # Ensure at least one character from each core pool
    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
    ]
    if include_symbols:
        password.append(secrets.choice("!@#$%^&*()-_=+"))

    while len(password) < length:
        password.append(secrets.choice(chars))

    # Shuffle deterministically using secrets
    secrets.SystemRandom().shuffle(password)
    return "".join(password)


if __name__ == "__main__":
    print("=== Secure Password Generator ===")
    pwd = generate_password(length=18)
    print(f"Generated Password (18 chars): {pwd}")
''',
    },
    {
        "id": "utilities_04",
        "category": "utilities",
        "filename": "04_json_config_manager.py",
        "title": "JSON Configuration Manager with Dot-Notation Access",
        "summary": "Loads and modifies nested configuration values using dot notation paths",
        "code": '''"""
JSON Configuration Manager.

Allows reading and writing nested JSON configurations using dot notation (e.g. 'server.port').
"""

import json
from typing import Any


class ConfigManager:
    def __init__(self, data: dict[str, Any]):
        self._data = data

    def get(self, path: str, default: Any = None) -> Any:
        keys = path.split(".")
        current = self._data
        for k in keys:
            if isinstance(current, dict) and k in current:
                current = current[k]
            else:
                return default
        return current

    def set(self, path: str, value: Any) -> None:
        keys = path.split(".")
        current = self._data
        for k in keys[:-1]:
            current = current.setdefault(k, {})
        current[keys[-1]] = value

    def to_json(self) -> str:
        return json.dumps(self._data, indent=2)


if __name__ == "__main__":
    print("=== Config Manager ===")
    cfg = ConfigManager({"database": {"host": "localhost", "port": 5432}})
    print(f"Port: {cfg.get('database.port')}")
    cfg.set("database.port", 5433)
    print(f"Updated JSON:\\n{cfg.to_json()}")
''',
    },
    {
        "id": "utilities_05",
        "category": "utilities",
        "filename": "05_expense_tracker.py",
        "title": "Command-Line Expense Tracker",
        "summary": "Tracks categorized expenditures and generates breakdown reports",
        "code": '''"""
Expense Tracker Utility.

Tracks categorized expenses and generates category percentage totals.
"""

from collections import defaultdict


class ExpenseTracker:
    def __init__(self):
        self.expenses: list[dict] = []

    def add_expense(self, category: str, amount: float, description: str) -> None:
        self.expenses.append({"category": category.lower(), "amount": amount, "description": description})

    def total_spending(self) -> float:
        return sum(e["amount"] for e in self.expenses)

    def category_breakdown(self) -> dict[str, float]:
        totals = defaultdict(float)
        for e in self.expenses:
            totals[e["category"]] += e["amount"]
        return dict(totals)


if __name__ == "__main__":
    print("=== Expense Tracker ===")
    tracker = ExpenseTracker()
    tracker.add_expense("Food", 24.50, "Lunch")
    tracker.add_expense("Transport", 15.00, "Bus Pass")
    tracker.add_expense("Food", 42.00, "Dinner")
    tracker.add_expense("Books", 35.00, "Python Book")

    print(f"Total: ${tracker.total_spending():.2f}")
    for cat, amt in tracker.category_breakdown().items():
        print(f" - {cat.title():10s}: ${amt:.2f}")
''',
    },
    {
        "id": "utilities_06",
        "category": "utilities",
        "filename": "06_custom_logger.py",
        "title": "Custom Timestamped Console and File Logger",
        "summary": "Provides colorized or formatted logs with levels INFO, WARNING, and ERROR",
        "code": '''"""
Custom Logger Utility.

Formats log events with ISO UTC timestamps and severity labels.
"""

from datetime import datetime, timezone


class SimpleLogger:
    LEVELS = {"DEBUG": 10, "INFO": 20, "WARNING": 30, "ERROR": 40}

    def __init__(self, min_level: str = "INFO"):
        self.min_level_val = self.LEVELS.get(min_level.upper(), 20)

    def _log(self, level: str, message: str) -> None:
        if self.LEVELS.get(level, 0) >= self.min_level_val:
            ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
            print(f"[{ts}] [{level:7s}] {message}")

    def info(self, msg: str) -> None:
        self._log("INFO", msg)

    def warning(self, msg: str) -> None:
        self._log("WARNING", msg)

    def error(self, msg: str) -> None:
        self._log("ERROR", msg)


if __name__ == "__main__":
    print("=== Simple Logger ===")
    logger = SimpleLogger(min_level="INFO")
    logger.info("Bot workflow started.")
    logger.warning("Network latency detected: retrying.")
    logger.error("Failed to fetch remote asset.")
''',
    },
    {
        "id": "utilities_07",
        "category": "utilities",
        "filename": "07_stopwatch_timer.py",
        "title": "Precision Stopwatch and Lap Tracker",
        "summary": "Tracks execution durations and records split lap timings",
        "code": '''"""
Precision Stopwatch and Lap Timer.

High precision timer using time.perf_counter().
"""

import time


class Stopwatch:
    def __init__(self):
        self._start_time: float | None = None
        self._laps: list[float] = []

    def start(self) -> None:
        self._start_time = time.perf_counter()
        self._laps.clear()

    def lap(self) -> float:
        if self._start_time is None:
            raise RuntimeError("Stopwatch has not been started.")
        current = time.perf_counter()
        elapsed = current - self._start_time
        self._laps.append(elapsed)
        return elapsed

    def get_laps(self) -> list[float]:
        return self._laps.copy()


if __name__ == "__main__":
    print("=== Stopwatch Simulation ===")
    sw = Stopwatch()
    sw.start()
    time.sleep(0.02)
    lap1 = sw.lap()
    time.sleep(0.03)
    lap2 = sw.lap()
    print(f"Lap 1: {lap1 * 1000:.2f} ms")
    print(f"Lap 2: {lap2 * 1000:.2f} ms")
''',
    },
    {
        "id": "utilities_08",
        "category": "utilities",
        "filename": "08_file_categorizer.py",
        "title": "File Extension Categorizer Utility",
        "summary": "Groups filenames into categories such as Code, Image, Document, or Audio",
        "code": '''"""
File Extension Categorizer.

Classifies a list of filenames into intuitive groups based on extension.
"""

from collections import defaultdict
import os

EXT_MAP = {
    "Code": {".py", ".js", ".ts", ".html", ".css", ".java", ".cpp"},
    "Document": {".pdf", ".docx", ".txt", ".md", ".xlsx"},
    "Image": {".png", ".jpg", ".jpeg", ".gif", ".svg"},
    "Archive": {".zip", ".tar", ".gz", ".7z"},
}


def categorize_files(filenames: list[str]) -> dict[str, list[str]]:
    """Group file names into high-level categories."""
    categories = defaultdict(list)
    for name in filenames:
        _, ext = os.path.splitext(name)
        matched = False
        for cat, ext_set in EXT_MAP.items():
            if ext.lower() in ext_set:
                categories[cat].append(name)
                matched = True
                break
        if not matched:
            categories["Other"].append(name)
    return dict(categories)


if __name__ == "__main__":
    print("=== File Categorizer ===")
    files = ["main.py", "styles.css", "report.pdf", "logo.png", "notes.txt", "archive.zip", "run.sh"]
    for group, items in categorize_files(files).items():
        print(f"{group:10s}: {items}")
''',
    },
    {
        "id": "utilities_09",
        "category": "utilities",
        "filename": "09_url_parser.py",
        "title": "URL Query Parameter Parser and Encoder",
        "summary": "Extracts, parses, and updates URL query parameters cleanly",
        "code": '''"""
URL Query Parameter Parser.

Parses URL components and query string parameters.
"""

from urllib.parse import parse_qs, urlencode, urlparse, urlunparse


def update_query_param(url: str, param: str, value: str) -> str:
    """Add or update a query parameter in a URL."""
    parsed = urlparse(url)
    query_dict = parse_qs(parsed.query)
    query_dict[param] = [value]
    new_query = urlencode(query_dict, doseq=True)
    return urlunparse(parsed._replace(query=new_query))


if __name__ == "__main__":
    print("=== URL Query Parameter Parser ===")
    base_url = "https://api.github.com/repos/owner/repo/commits?page=1&per_page=10"
    updated = update_query_param(base_url, "page", "2")
    print(f"Original: {base_url}")
    print(f"Updated : {updated}")
''',
    },
    {
        "id": "utilities_10",
        "category": "utilities",
        "filename": "10_markdown_table_generator.py",
        "title": "Markdown Table Generator Formatter",
        "summary": "Formats 2D lists or dictionaries into clean GitHub Flavored Markdown tables",
        "code": '''"""
Markdown Table Generator.

Transforms structured row/column data into clean GitHub-flavored markdown tables.
"""


def generate_markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    """Format headers and rows into an aligned markdown table."""
    col_widths = [len(h) for h in headers]
    for row in rows:
        for idx, cell in enumerate(row):
            if idx < len(col_widths):
                col_widths[idx] = max(col_widths[idx], len(str(cell)))

    header_line = "| " + " | ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers)) + " |"
    separator_line = "| " + " | ".join("-" * col_widths[i] for i in range(len(headers))) + " |"

    body_lines = []
    for row in rows:
        cells = [str(cell).ljust(col_widths[i]) for i, cell in enumerate(row)]
        body_lines.append("| " + " | ".join(cells) + " |")

    return "\\n".join([header_line, separator_line] + body_lines)


if __name__ == "__main__":
    print("=== Markdown Table Generator ===")
    headers = ["Category", "Topic", "Difficulty"]
    sample_rows = [
        ["Basics", "Prime Number Checker", "Beginner"],
        ["Strings", "Palindrome Detector", "Beginner"],
        ["DSA", "Binary Search", "Intermediate"],
    ]
    table = generate_markdown_table(headers, sample_rows)
    print(table)
''',
    },
]


def get_template_by_id(template_id: str) -> Dict[str, Any] | None:
    """Retrieve a template by its unique identifier."""
    for t in TEMPLATES:
        if t["id"] == template_id:
            return t
    return None


def get_templates_by_category(category: str) -> List[Dict[str, Any]]:
    """Retrieve all fallback templates for a specific category."""
    return [t for t in TEMPLATES if t["category"] == category]
