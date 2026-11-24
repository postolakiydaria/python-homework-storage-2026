#!/usr/bin/env python3


import argparse
import re

def find_lines_with_word(input_path, search_word):
    """
    Читает файл и находит строки, содержащие искомое слово (без учета регистра).
    :param input_path: Путь к входному файлу.
    :param search_word: Слово для поиска.
    :return: Список строк, содержащих слово.
    :raises FileNotFoundError: Если входной файл не существует.
    """
    try:
        with open(input_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        raise FileNotFoundError("Входной файл не найден!")

    pattern = re.compile(rf'\b{re.escape(search_word)}\b', re.IGNORECASE) # \b - граница слова; re.escape() - экранирует спецсимволы

    result_lines = []
    for text_line in lines:
        if pattern.search(text_line):
            result_lines.append(text_line)
    return result_lines

def save_lines(output_path, lines_list):
    """
    Сохраняет найденные строки в файл.
    :param output_path: Путь к выходному файлу.
    :param lines_list: Список строк.
    """
    with open(output_path, "w", encoding="utf-8") as file:
        for line_to_save in lines_list:
            file.write(line_to_save)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="word_finder",
                                     description="Скрипт для поиска строк с указанным словом.",
                                     epilog="Удачного поиска!")
    parser.add_argument("word", type=str, help="Слово для поиска")
    parser.add_argument("-i", "--input", type=str, required=True, help="Путь к входному файлу")
    parser.add_argument("-o", "--output", type=str, help="Путь к выходному файлу (если не указан, вывод в консоль)")
    args = parser.parse_args()

    try:
        found_lines = find_lines_with_word(args.input, args.word)
        if args.output:
            save_lines(args.output, found_lines)
            print(f"Найдено строк: {len(found_lines)}. Результат сохранен в {args.output}")
        else:
            print(f"Найдено строк: {len(found_lines)}")
            for line in found_lines:
                print(line, end="") # end="" - отменяет автоматический перенос строки от print
    except FileNotFoundError as e:
        print(e)
