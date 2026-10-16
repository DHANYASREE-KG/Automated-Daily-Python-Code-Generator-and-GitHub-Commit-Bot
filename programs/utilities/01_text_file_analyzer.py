"""
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
