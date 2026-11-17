#!/usr/bin/env python3
# -*- coding: utf-8 -*-

DELIMITER = ' '


def sort_ascending(numbers: list) -> list:
    """
    Отсортировать список по возрастанию (пузырьковая сортировка).
    :param numbers: исходный список чисел
    :return: новый отсортированный список
    """
    result = numbers.copy()
    n = len(result)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def sort_descending(numbers: list) -> list:
    """
    Отсортировать список по убыванию.
    :param numbers: исходный список чисел
    :return: новый отсортированный список
    """
    return sort_ascending(numbers)[::-1]


def parse_numbers(raw: str) -> list | None:
    """
    Преобразовать строку в список чисел.
    Поддерживает точку и запятую в качестве десятичного разделителя.
    :param raw: строка с числами через пробел
    :return: список чисел или None при нечисловом вводе
    """
    result = []
    for item in raw.split(DELIMITER):
        if not item:
            continue
        item = item.replace(',', '.')  # запятая → точка
        try:
            result.append(int(item))
            continue
        except ValueError:
            pass
        try:
            result.append(float(item))
        except ValueError:
            return None
    return result


if __name__ == '__main__':
    nums = []
    while True:
        user_answer = input("Введите через пробел последовательность чисел: ")

        nums = parse_numbers(user_answer)
        if nums is None:
            print("Ошибка! Вы должны ввести последовательность чисел")
            continue
        if not nums:
            print("Вы ничего не ввели!")
            continue
        break

    print("1 - по возрастанию, 2 - по убыванию")
    user_choice = input("Ваш выбор: ")

    if user_choice == "1":
        result = sort_ascending(nums)
    elif user_choice == "2":
        result = sort_descending(nums)
    else:
        result = None
        print("Ошибка! Выберите 1 или 2")

    if result is not None:
        print(f"Ваш отсортированный список: {result}")
        
