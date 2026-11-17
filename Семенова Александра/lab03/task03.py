#!/usr/bin/env python3

import random

LIST_SIZE = 20
MIN_VALUE = -100
MAX_VALUE = 100

def random_list(size, min_val, max_val):
    """
    Генерирует список случайных целых чисел.

    :param size: количество элементов в списке.
    :param min_val: минимальное значение.
    :param max_val: максимальное значение.
    :return: список случайных чисел.
    """
    return [random.randint(min_val, max_val) for _ in range(size)]

if __name__ == "__main__":

    numbers = random_list(LIST_SIZE, MIN_VALUE, MAX_VALUE)
    print(f"Исходный список ({len(numbers)} чисел): ")
    print(numbers)

    div_3 = list(filter(
        lambda x: x % 3 == 0 and x % 9 != 0,
        numbers
    ))
    print(f"Делятся на 3, но не на 9 ({len(div_3)} чисел):")
    print(div_3)

    abs_greater_20 = list(filter(
        lambda x: abs(x) > 20,
        numbers
    ))  
    print(f"Абсолютное значение > 20 ({len(abs_greater_20)} чисел):")
    print(abs_greater_20)

    both_conditions = list(filter(
        lambda x: (x % 3 == 0 and x % 9 != 0) and abs(x) > 20,
        numbers
    ))

    print(f"Оба условия ({len(both_conditions)} чисел):")
    print(both_conditions)

