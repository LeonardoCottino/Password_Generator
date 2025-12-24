import string
import secrets

LETTERS = string.ascii_letters
DIGITS = string.digits
SYMBOLS = string.punctuation

def generate_password(length=12, use_letters=True, use_digits=True, use_symbols=True, shuffle=True):
     # input validation
    if length <= 0:
        raise ValueError("Length must be greater than 0")
    if not use_letters and not use_digits and not use_symbols:
        raise ValueError("At least one character type must be selected")

    chars = ""
    if use_letters:
        chars += LETTERS
    if use_digits:
        chars += DIGITS
    if use_symbols:
        chars += SYMBOLS

    # Scelgo casualmente n elementi
    password_chars = [secrets.choice(chars) for i in range(length)]

    if shuffle:
        secrets.SystemRandom().shuffle(password_chars);

    return "".join(password_chars)
