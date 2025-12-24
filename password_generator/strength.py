import string
from collections import namedtuple

WEAK = "WEAK"
MEDIUM = "MEDIUM"
STRONG = "STRONG"

Strength = namedtuple("Strength", ["score", "label"])

def evaluate_strength(password):
    # criteri di valutazione
    has_uppercase = has_lowercase = has_digits = has_special = False
    password_length = len(password)
    for c in password:
        if c.isupper():
            has_uppercase = True
        elif c.islower():
            has_lowercase = True
        elif c.isdigit():
            has_digits = True
        elif c in string.punctuation:
            has_special = True
        
        if has_uppercase and has_lowercase and has_digits and has_special:
            break

    score = 0
    label = WEAK
    # length strenght
    if 8 <= password_length <= 12:
        score += 1
    elif password_length >=12:
        score += 2
    # chars type
    if has_uppercase:
        score += 1
    if has_lowercase:
        score += 1
    if has_digits:
        score += 1
    if has_special:
        score += 1
    
    if 2 < score < 5:
        label = MEDIUM
    elif score >= 5:
        label = STRONG 

    return Strength(score, label)
    