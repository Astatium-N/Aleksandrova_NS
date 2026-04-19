import random
import string
from typing import Optional

def decor(text: str, symbol: str = "*") -> None:
    border = symbol * (len(text) + 4)
    print(border)
    print(f"{symbol} {text} {symbol}")
    print(border)

def validate_length(value: str) -> int:
    length = int(value)
    if length <= 5:
        raise ValueError("Длина должна быть больше 5")
    return length

def gen_pass(length: int, special: Optional[str] = None, use_digits: bool = True) -> str:
    letters = string.ascii_letters
    digits = string.digits if use_digits else ""
    base = letters + digits
    password = []

    if special:
        for char in special:
            password.append(char)

    if len(password) < length:
        password.append(random.choice(letters))

    if use_digits and len(password) < length:
        password.append(random.choice(digits))

    remaining = length - len(password)
    if remaining > 0:
        all_chars = base + (special if special else "")
        password.extend(random.choice(all_chars) for _ in range(remaining))

    random.shuffle(password)
    return ''.join(password)

def main_ans() -> None:
    welcome = "Добро пожаловать в Генератор паролей!"
    decor(welcome)

    while True:
        user_input = input("\nВведите длину пароля (целое число > 5): ").strip()
        try:
            pass_length = validate_length(user_input)
            break
        except ValueError as z:
            print(f"Ошибка: {z}. Попробуйте снова.")

    special_choice = input("По желанию введите специальные символы или оставьте поле пустым: ").strip()
    if not special_choice:
        special_choice = None
        print("Специальные символы не будут использоваться в пароле.")

    digits_choice = input("Использовать цифры в пароле? (да/нет): ").strip().lower()
    use_digits = digits_choice in ['да', 'д']
    if not use_digits:
        print("Цифры не будут использоваться в пароле.")

    password = gen_pass(pass_length, special_choice, use_digits)

    filename = input("Введите имя файла для сохранения пароля или оставьте поле пустым для вывода в консоль: ").strip()

    if filename:
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(password)
            print(f"✅ Пароль успешно сохранён в файл '{filename}'")
        except Exception as z:
            print(f"❌ Ошибка при записи в файл: {z}")
            print(f"Сгенерированный пароль: {password}")
    else:
        result = f"Ваш сгенерированный пароль: {password}"
        decor(result)

if __name__ == "__main__":
    main_ans()
