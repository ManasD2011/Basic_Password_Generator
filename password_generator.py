
"""
A simple password generator python Program.
Python password_gen.py <length> [count]
"""
import secrets
import string
import sys

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True, exclude_similar=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ''
    digits = string.digits if use_digits else ''
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/|" if use_symbols else ''
    alphabet = lower + upper + digits + symbols
    if exclude_similar:
        similar = "Il1O0"
        alphabet = ''.join(ch for ch in alphabet if ch not in similar)
    if not alphabet:
        raise ValueError("Character set is empty. Enable at least one class of characters.")
    
    
    # Ensure at least one character from each enabled class (if length allows)
    pwd = []
    mandatory_sets = []
    if lower: mandatory_sets.append(lower)
    if upper: mandatory_sets.append(upper)
    if digits: mandatory_sets.append(digits)
    if symbols: mandatory_sets.append(symbols)
    for s in mandatory_sets[:length]:
        pwd.append(secrets.choice(s))
    while len(pwd) < length:
        pwd.append(secrets.choice(alphabet))
    secrets.SystemRandom().shuffle(pwd)
    return ''.join(pwd)



if __name__ == "__main__":
    try:
        length = int(sys.argv[1]) if len(sys.argv) > 1 else 12
        count = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    except Exception:
        print("Usage: python password_gen.py <length> [count]")
        sys.exit(1)

    for _ in range(count):
        print(generate_password(length=length))
