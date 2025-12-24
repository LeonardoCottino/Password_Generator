from password_generator.generator import generate_password
from password_generator.strength import evaluate_strength

def ask_yes_no(prompt, default=True):
    val = input(f"{prompt} [{'Y/n' if default else 'y/N'}]: ").strip().lower()
    if val == "" and default is not None:
        return default
    return val in ("y", "yes", "s", "si", "true", "1")

def run_generation():
    length_str = input("Lunghezza password (default 12): ").strip()
    length = int(length_str) if length_str else 12
    use_letters = ask_yes_no("Includere lettere?", default=True)
    use_numbers = ask_yes_no("Includere numeri?", default=True)
    use_symbols = ask_yes_no("Includere simboli?", default=True)
    pwd = generate_password(
        length=length,
        use_letters=use_letters,
        use_digits=use_numbers,
        use_symbols=use_symbols,
    )
    strength = evaluate_strength(pwd)
    print("\nPassword:", pwd)
    print("Strength:", strength)


def run_strength_check():
    pwd = input("Inserisci la password da valutare: ").strip()
    strength = evaluate_strength(pwd)
    print("Strength:", strength)


def main():
    while True:
        print("\n--- Password Generator ---")
        print("[1] Genera nuova password")
        print("[2] Valuta una password esistente")
        print("[q] Esci")
        choice = input("Scelta: ").strip().lower()
        if choice in ("q", "quit", "exit"):
            print("Ciao!")
            break
        if choice == "1":
            run_generation()
        elif choice == "2":
            run_strength_check()
        else:
            print("Scelta non valida.")


if __name__ == "__main__":
    main()