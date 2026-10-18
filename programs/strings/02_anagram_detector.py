"""
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
        print(f"\"{w1}\" and \"{w2}\" -> Anagrams? {are_anagrams(w1, w2)}")
