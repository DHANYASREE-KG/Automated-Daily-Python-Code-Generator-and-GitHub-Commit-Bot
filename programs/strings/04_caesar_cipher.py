"""
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
