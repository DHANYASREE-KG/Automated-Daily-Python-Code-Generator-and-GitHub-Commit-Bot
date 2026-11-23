"""
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
