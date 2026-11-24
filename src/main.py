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

def validate_length(value):
    """Проверяет введённую длину пароля: целое число от 4 до 64."""
    if not value.isdigit():
        return None
    length = int(value)
    if length < 4 or length > 64:
        return None
    return length

def main():
    print("Генератор паролей PassGen — добро пожаловать!")
    print("1 - Сгенерировать пароль")
    print("2 - Пароль со спецсимволами")
    print("3 - Несколько паролей и поиск")
    choice = input("Выберите пункт: ")
    length = validate_length(input("Длина пароля (4-64): "))
    if length is None:
        print("Ошибка: введите целое число от 4 до 64")
        return
    if choice == "1":
        password = generate_password(length)
        print("Пароль:", password, "| Надёжность:", check_strength(password))
    elif choice == "2":
        password = generate_with_symbols(length)
        print("Пароль:", password, "| Надёжность:", check_strength(password))
    elif choice == "3":
        passwords = generate_many(5, length)
        print("Пароли:", ", ".join(passwords))
        text = input("Найти пароли, содержащие: ")
        found = search_passwords(passwords, text)
        print("Найдено:", ", ".join(found) if found else "ничего")
    else:
        print("Неизвестный пункт меню")

if __name__ == "__main__":
    main()