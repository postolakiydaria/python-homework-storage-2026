#!/usr/bin/env python3

from functools import reduce

def get_product(*args):
    ints = [x for x in args if type(x) is int]

    if not ints:
        return [(item, type(item)) for item in args]

    return reduce(lambda acc, x: acc * x, ints, 1)


if __name__ == '__main__':

    res_1 = get_product("текст", 2, 3.14, [1, 2], 3)
    print("\'текст\', 2, 3.14, [1, 2], 3")
    print("Тест 1 (есть целые числа):")
    print(f"Результат: {res_1}\n")

    res_2 = get_product("слово", 5.5, (1, 2))
    print("Тест 2 (нет целых чисел):")
    print(f"Результат: {res_2}")
