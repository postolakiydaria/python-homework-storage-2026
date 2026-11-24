#!/usr/bin/env python3


import argparse
import re

PATTERNS = {'digits': r'\b\d+\b',
            'phones': r'(\+7\d{10}|\+7\(\d{3}\)-\d{3}-\d{2}-\d{2}|\b\d{2}-\d{2}-\d{2}\b|\b\d{6}\b)',
            'domains': r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b',
            'urls': r'https?://[^\s]+'}

def find_matches(input_path, modes):
    """
    Читает файл и находит совпадения для каждого выбранного режима.
    :param input_path: Путь к входному файлу.
    :param modes: Список выбранных режимов (например, ['digits', 'phones']).
    :return: Словарь, где ключ - режим, значение - список найденных совпадений.
    :raises FileNotFoundError: Если входной файл не существует.
    """
    try:
        with open(input_path, "r", encoding="utf-8") as input_file:
            text = input_file.read()
    except FileNotFoundError:
        raise FileNotFoundError("Входной файл не найден!")

    results = {}
    for search_mode in modes:
        pattern = PATTERNS[search_mode]
        matches = re.findall(pattern, text)
        results[search_mode] = matches
    return results

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="data_extractor",
                                     description="Скрипт для поиска данных (чисел, телефонов, доменов, ссылок) в тексте.",
                                     epilog="Удачного поиска!")
    parser.add_argument("modes", nargs="+", type=str, choices=['digits', 'phones', 'domains', 'urls'], help="Режимы поиска: digits, phones, domains, urls")
    parser.add_argument("-i", "--input", type=str, required=True, help="Путь к входному файлу")
    parser.add_argument("-o", "--output", type=str, help="Путь к выходному файлу (если не указан, вывод в консоль)")
    args = parser.parse_args()

    try:
        found_data = find_matches(args.input, args.modes)

        output_lines = []
        for mode in args.modes:
            output_lines.append(f"{mode.upper()}:")
            if found_data[mode]:
                output_lines.extend(found_data[mode])
            else:
                output_lines.append("Ничего не найдено.")
            output_lines.append("")

        final_text = "\n".join(output_lines)

        if args.output:
            with open(args.output, "w", encoding="utf-8") as file:
                file.write(final_text)
            print(f"Результат сохранен в {args.output} \n")
        else:
            print(final_text)

        print("ИТОГО НАЙДЕНО")
        for mode in args.modes:
            count = len(found_data[mode])
            print(f"{mode}: {count}")

    except FileNotFoundError as e:
        print(e)
