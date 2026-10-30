"""
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
