#!/usr/bin/env python3


import argparse
import re
from datetime import datetime

def validate_date(date_string):
    """
    Проверяет, что строка является датой в формате YYYY-MM-DD.
    :param date_string: Строка с датой.
    :return: True, если дата корректна, иначе False.
    """
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', date_string):
        return False
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def find_lines_by_date(input_path, date_str):
    """
    Читает файл и находит строки, содержащие указанную дату.
    :param input_path: Путь к входному файлу.
    :param date_str: Дата в формате YYYY-MM-DD.
    :return: Список строк, содержащих дату.
    :raises FileNotFoundError: Если входной файл не существует.
    """
    try:
        with open(input_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        raise FileNotFoundError("Входной файл не найден!")

    result_lines = []
    for text_line in lines:
        if re.search(date_str, text_line):
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
    parser = argparse.ArgumentParser(prog="log_date_finder",
                                     description="Утилита для поиска строк с определенной датой в лог-файле.",
                                     epilog="Удачного поиска!")
    parser.add_argument("date", type=str, help="Дата в формате YYYY-MM-DD")
    parser.add_argument("-i", "--input", type=str, required=True, help="Путь к входному лог-файлу")
    parser.add_argument("-o", "--output", type=str, help="Путь к выходному файлу (если не указан, вывод в консоль)")
    args = parser.parse_args()

    if not validate_date(args.date):
        print("Дата должна быть в формате YYYY-MM-DD и быть реальной датой.")
    else:
        try:
            found_lines = find_lines_by_date(args.input, args.date)
            if args.output:
                save_lines(args.output, found_lines)
                print(f"Найдено строк: {len(found_lines)}. Результат сохранен в {args.output}")
            else:
                print(f"Найдено строк: {len(found_lines)}")
                for line in found_lines:
                    print(line, end="")
        except FileNotFoundError as e:
            print(e)
