#!/usr/bin/env python3


import argparse
import re

EMAIL_PATTERN = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

def find_emails(input_path):
    """
    Читает файл и извлекает все email-адреса.
    :param input_path: Путь к входному файлу.
    :return: Список найденных email-адресов.
    :raises FileNotFoundError: Если входной файл не существует.
    """
    try:
        with open(input_path, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        raise FileNotFoundError("Входной файл не найден!")
    emails = re.findall(EMAIL_PATTERN, text)
    return emails

def save_emails(output_path, emails_list):
    """
    Сохраняет список email-адресов в файл (по одному на строку).
    :param output_path: Путь к выходному файлу.
    :param emails_list: Список email-адресов.
    """
    with open(output_path, "a", encoding="utf-8") as file:
        for email_item in emails_list:
            file.write(email_item + "\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="email_extractor",
                                     description="Скрипт для поиска email-адресов в текстовом файле.",
                                     epilog="Удачного поиска!")
    parser.add_argument("-i", "--input", type=str, required=True, help="Путь к входному файлу")
    parser.add_argument("-o", "--output", type=str, help="Путь к выходному файлу (если не указан, вывод в консоль)")
    args = parser.parse_args()

    try:
        found_emails = find_emails(args.input)
        if args.output:
            save_emails(args.output, found_emails)
            print(f"Найдено email-адресов: {len(found_emails)}. Результат сохранен в {args.output}")
        else:
            print(f"Найдено email-адресов: {len(found_emails)}")
            for email in found_emails:
                print(email)
    except FileNotFoundError as e:
        print(e)
