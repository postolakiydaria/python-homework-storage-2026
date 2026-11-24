#!/usr/bin/env python3


import argparse
import re

def find_matches(input_path, regex_pattern):
    """
    Читает файл и находит все совпадения с регулярным выражением.
    :param input_path: Путь к входному файлу.
    :param regex_pattern: Строка с регулярным выражением.
    :return: Список найденных совпадений.
    :raises FileNotFoundError: Если входной файл не существует.
    :raises re.error: Если регулярное выражение некорректно.
    """
    try:
        pattern = re.compile(regex_pattern)
    except re.error:
        raise re.error("Некорректное регулярное выражение!")

    try:
        with open(input_path, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        raise FileNotFoundError("Входной файл не найден!")

    matches = pattern.findall(text)
    return matches

def save_matches(output_path, matches_list):
    """
    Сохраняет найденные совпадения в файл (по одному на строку).
    :param output_path: Путь к выходному файлу.
    :param matches_list: Список совпадений.
    """
    with open(output_path, "w", encoding="utf-8") as file:
        for match_item in matches_list:
            file.write(match_item + "\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="regex_finder",
                                     description="Скрипт для поиска совпадений с регулярным выражением в файле.",
                                     epilog="Удачного поиска!")
    parser.add_argument("pattern", type=str, help="Регулярное выражение для поиска")
    parser.add_argument("-i", "--input", type=str, required=True, help="Путь к входному файлу")
    parser.add_argument("-o", "--output", type=str, help="Путь к выходному файлу (если не указан, вывод в консоль)")
    args = parser.parse_args()

    try:
        found_matches = find_matches(args.input, args.pattern)
        if args.output:
            save_matches(args.output, found_matches)
            print(f"Найдено совпадений: {len(found_matches)}. Результат сохранен в {args.output}")
        else:
            print(f"Найдено совпадений: {len(found_matches)}")
            for match in found_matches:
                print(match)
    except (FileNotFoundError, re.error) as e:
        print(e)
