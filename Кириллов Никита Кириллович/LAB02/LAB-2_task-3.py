#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce


def multi_ints(*args) -> int | dict:
    """
    Перемножить все целые числа среди аргументов.
    :param args: произвольные аргументы
    :return: произведение целых чисел или словарь {аргумент: тип},
             если целых чисел нет
    """
    only_ints = [x for x in args if type(x) is int]

    if not only_ints:
        return {arg: type(arg) for arg in args}

    product = reduce(lambda acc, x: acc * x, only_ints, 1)
    return product


def main() -> None:
    """
    Точка входа программы.
    :return: None
    """
    user_answer = input("Введите числа и слова через пробел: ").split()

    user_data = []
    for item in user_answer:
        try:
            user_data.append(int(item))
        except ValueError:
            try:
                user_data.append(float(item))
            except ValueError:
                user_data.append(item)

    result = multi_ints(*user_data)
    print(f"Результат: {result}")


if __name__ == '__main__':
    main()
    
