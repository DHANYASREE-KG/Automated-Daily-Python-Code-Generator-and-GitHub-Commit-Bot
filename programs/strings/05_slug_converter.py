"""
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
        print(f"Slug : {generate_slug(title)}\n")
