#!/usr/bin/env python3
# -*- coding: utf-8 -*-

VOWELS = "аеёиоуыэюяaeiouy"


def filter_vowels(**kwargs) -> dict:
    """
    Фильтрует именованные аргументы, оставляя только те,
    чьи значения являются строками и содержат не менее трёх гласных букв.
    :param kwargs: произвольное количество именованных аргументов
    :return: словарь {аргумент: значение} с подходящими парами
    """
    result = {}

    for key, value in kwargs.items():
        if type(value) is str:
            vowels_count = len([char for char in value.lower() if char in VOWELS])
            if vowels_count >= 3:
                result[key] = value

    return result


def main() -> None:
    """
    Точка входа программы.
    :return: None
    """
    print("Введите аргументы через запятую в формате: ключ=значение")
    print("Пример: name=Екатерина, city=Москва")
    user_input = input("Ваш ввод: ")

    parsed_dict = {}
    # Разбиваем ввод по запятым
    pairs = user_input.split(",")
    for pair in pairs:
        if "=" in pair:
            key, value = pair.split("=", 1)
            parsed_dict[key.strip()] = value.strip()

    final_result = filter_vowels(**parsed_dict)

    if final_result:
        print(f"Подходящие аргументы (3+ гласных): {final_result}")
    else:
        print("Подходящих аргументов не найдено")


if __name__ == '__main__':
    main()
    
