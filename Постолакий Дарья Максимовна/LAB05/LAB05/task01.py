#!/usr/bin/env python3


import argparse

MIN_AGE = 0
MAX_AGE = 120

def age_check(value):
    """
    Проверяет, что возраст является целым числом в диапазоне от MIN_AGE до MAX_AGE.
    :param value: Строка, введенная пользователем.
    :return: Целое число (возраст).
    :raises argparse.ArgumentTypeError: Если число не целое или вне диапазона.
    """
    try:
        age = int(value)
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"'{value}' не является целым числом.") from e
    if not (MIN_AGE <= age <= MAX_AGE):
        raise argparse.ArgumentTypeError(f"Возраст должен быть от {MIN_AGE} до {MAX_AGE} лет.")
    return age

def generate_greeting(name, age=None, formal_greeting=False):
    """
    Формирует строку приветствия.
    :param name: Имя пользователя.
    :param age: Возраст пользователя (может быть не передан).
    :param formal_greeting: Флаг, использовать ли формальное приветствие.
    :return: Строка приветствия.
    """
    if formal_greeting:
        greeting = f"Уважаемый(ая) {name}"
    else:
        greeting = f"Привет, {name}"
    if age is not None:
        greeting += f", ваш возраст: {age} лет."
    else:
        greeting += "!"
    return greeting

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="greeting_script",
                                     description="Скрипт для приветствия пользователя.",
                                     epilog="Всего хорошего и приятного вам!")

    parser.add_argument("name", type=str, help="Имя пользователя")
    parser.add_argument("-a", "--age", type=age_check, help="Возраст")
    parser.add_argument("-g", "--greeting", action="store_true", help="Формальное приветствие")

    args = parser.parse_args()

    result = generate_greeting(args.name, args.age, args.greeting)
    print(result)
