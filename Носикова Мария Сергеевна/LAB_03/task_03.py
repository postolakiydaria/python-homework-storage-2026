#!/usr/bin/env python3
import random

NUMBERS_COUNT = 20
MIN_VALUE = -100
MAX_VALUE = 100

def first_filter(numbers):
    """
    Фильтрует числа, которые делятся на 3, но не делятся на 9.

    :param numbers: Список целых чисел.
    :return: Список чисел, делящихся на 3, но не на 9.
    """
    return list(filter(lambda x: x % 3 == 0 and x % 9 != 0, numbers))


def second_filter(numbers):
    """
    Фильтрует числа, абсолютное значение которых больше 20.

    :param numbers: Список целых чисел.
    :return: Список чисел с абсолютным значением больше 20.
    """
    return list(filter(lambda x: abs(x) > 20, numbers))


def third_filter(numbers):
    """
    Фильтрует числа, которые одновременно удовлетворяют обоим условиям.
    :param numbers: Список целых чисел.
    :return: Список чисел, удовлетворяющие обоим условиям
    """
    return list(filter(lambda x: x % 3 == 0 and x % 9 != 0 and abs(x) > 20, numbers))


if __name__ == '__main__':
    numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(NUMBERS_COUNT)]

    print(f"Исходный список: {numbers}")
    result_1 = first_filter(numbers)
    result_2 = second_filter(numbers)
    result_3 = third_filter(numbers)

    print(
        f"Числа, которые делятся на 3, но не делятся на 9:\n {result_1}\n"
        f"Длина: {len(result_1)}"
    )

    print(
        f"Числа, абсолютное значение которых больше 20:\n {result_2}\n"
        f"Длина: {len(result_2)}"
    )

    print(
        f"Числа, которые одновременно удовлетворяют обоим условиям:\n {result_3}\n"
        f"Длина: {len(result_3)}"
    )
