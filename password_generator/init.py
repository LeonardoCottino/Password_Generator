from generator import *
from password_generator.strength import evaluate_strength

psw = generate_password()
print(psw)
print(evaluate_strength(psw))
