"""
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
    print(f"=== Character Analysis for: \"{sample}\" ===")
    for category, count in analyze_characters(sample).items():
        print(f"{category.title():12s}: {count}")
