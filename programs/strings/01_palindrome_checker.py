"""
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
        print(f"\"{phrase}\" -> Palindrome? {is_palindrome(phrase)}")
