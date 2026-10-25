"""
Word Frequency Counter.

Parses text into words, normalizes casing, and computes frequency counts.
"""

from collections import Counter
import re


def analyze_word_frequencies(text: str, top_n: int = 5) -> list[tuple[str, int]]:
    """Return the top N most frequent words in text."""
    words = re.findall(r"\b[a-zA-Z0-9_]+\b", text.lower())
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
