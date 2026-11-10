#!/usr/bin/env python3


import argparse
import random
import string

MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 64
LETTERS = string.ascii_letters
DIGITS = string.digits
SPECIAL_CHARS = "!@#$%^&*()-_=+[]{}|;:,.<>?"

def generate_password(length, use_digits, use_special):
    """
    Генерирует один пароль заданной длины.
    :param length: Длина пароля.
    :param use_digits: Использовать ли цифры (bool).
    :param use_special: Использовать ли спецсимволы (bool).
    :return: Сгенерированный пароль.
    :raises ValueError: Если невозможно составить пароль из выбранных символов.
    """
    characters = LETTERS
    if use_digits:
        characters += DIGITS
    if use_special:
        characters += SPECIAL_CHARS
    if not characters:
        raise ValueError("Ошибка: невозможно сгенерировать пароль (нет доступных символов).")
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def save_to_file(filepath, passwords_list):
    """
    Сохраняет список паролей в файл.
    :param filepath: Путь к файлу.
    :param passwords_list: Список паролей.
    """
    with open(filepath, "w", encoding="utf-8") as file:
        for password_item in passwords_list:
            file.write(password_item + "\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="password_generator",
                                     description="Скрипт для генерации надежных паролей.",
                                     epilog="Безопасность превыше всего!")

    parser.add_argument("-l", "--length", type=int, required=True, help=f"Длина пароля (от {MIN_PASSWORD_LENGTH} до {MAX_PASSWORD_LENGTH})")
    parser.add_argument("-c", "--count", type=int, required=True, help="Количество паролей для генерации")
    parser.add_argument("-d", "--no-digits", action="store_true", help="Исключить цифры из пароля")
    parser.add_argument("-s", "--no-special", action="store_true", help="Исключить спецсимволы из пароля")
    parser.add_argument("-f", "--file", type=str, help="Файл для сохранения паролей")

    args = parser.parse_args()

    if not (MIN_PASSWORD_LENGTH <= args.length <= MAX_PASSWORD_LENGTH):
        print(f"Ошибка: Длина пароля должна быть от {MIN_PASSWORD_LENGTH} до {MAX_PASSWORD_LENGTH}!")
    else:
        passwords = []
        try:
            for _ in range(args.count):
                pwd = generate_password(args.length, not args.no_digits, not args.no_special)
                passwords.append(pwd)
                print(pwd)
            if args.file:
                save_to_file(args.file, passwords)
                print(f"\nПароли сохранены в файл: {args.file}")
        except ValueError as e:
            print(e)
