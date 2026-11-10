#!/usr/bin/env python3


import argparse

def filter_strings(strings, unique, min_length):
    """
    Фильтрует список строк: удаляет дубликаты и короткие строки.
    :param strings: Исходный список строк.
    :param unique: Флаг, нужно ли удалять дубликаты.
    :param min_length: Минимальная длина строки.
    :return: Отфильтрованный список строк.
    """
    result = strings.copy()
    if unique:
        result = list(set(result))
    if min_length is not None:
        result = [string for string in result if len(string) >= min_length]
    return result

def sort_strings(strings, sort_order):
    """
    Сортирует список строк.
    :param strings: Список строк.
    :param sort_order: Порядок сортировки ("asc", "desc" или "none").
    :return: Отсортированный список строк.
    """
    if sort_order == "asc":
        strings.sort(key=str)
    elif sort_order == "desc":
        strings.sort(key=str, reverse=True)
    return strings

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="string_processor",
                                     description="Скрипт для обработки и фильтрации строк.",
                                     epilog="Работа со строками завершена!")

    parser.add_argument("strings", nargs="*", type=str, help="Строки для обработки")

    parser.add_argument("-c", "--count", action="store_true", help="Вывести только количество строк")
    parser.add_argument("-u", "--unique", action="store_true", help="Вывести только уникальные строки")
    parser.add_argument("-l", "--min-length", type=int, help="Минимальная длина строки")
    parser.add_argument("-s", "--sort", type=str, choices=["asc", "desc", "none"], default="none", help="Сортировка: asc, desc или none")

    args = parser.parse_args()

    if not args.strings:
        print("Вы не передали ни одной строки для обработки!")
    else:
        filtered_strings = filter_strings(args.strings, args.unique, args.min_length)
        final_strings = sort_strings(filtered_strings, args.sort)
        if args.count:
            print(f"Количество строк после фильтрации: {len(final_strings)}")
        else:
            for s in final_strings:
                print(s)
