import random
import string

VERSION = "1.1"


def generate_password(length=12):
    """Генерирует пароль из букв и цифр."""
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))


def check_strength(password):
    """Оценивает надёжность пароля."""
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    return ["Очень слабый", "Слабый", "Средний", "Хороший", "Сильный"][score]


def generate_many(count, length=12):
    """Генерирует список из нескольких паролей."""
    return [generate_password(length) for _ in range(count)]

def generate_with_symbols(length=12):
    """Генерирует пароль с буквами, цифрами и спецсимволами."""
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

def filter_by_strength(passwords, level):
    """Оставляет только пароли с указанной надёжностью."""
    return [p for p in passwords if check_strength(p) == level]

def main():
    password = generate_password()
    print("Пароль:", password)
    print("Надёжность:", check_strength(password))


if __name__ == "__main__":
    main()
