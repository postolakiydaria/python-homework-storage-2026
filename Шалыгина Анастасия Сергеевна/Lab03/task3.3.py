#!/usr/bin/env python3


import random


def generate_and_filter_numbers():
    """
    Функция принимает список из случайно сгенерированных чисел в диапазоне от -100 до 100 и фильтрует по трем условиям

    :return: None (Функция только выводит результаты, но ничего не возвращает)
    """
    numbers = [random.randint(-100, 100) for i in range(20)]
    print(f'Исходный список ({len(numbers)}): {numbers}')
    filter_1 = list(filter(lambda x: x%3 == 0 and x % 9 != 0, numbers))
    filter_2 = list(filter(lambda x: abs(x)>20, numbers))
    filter_3 = list(filter(lambda x: (x%3 == 0 and x%9 != 0) and abs(x)> 20 , numbers))

    print(f'Делится на 3, но не на 9: \n Список: {filter_1}, \n Длина списка: {len(filter_1)}')
    print(f' Абсолютное значение > 20: \n Список: {filter_2}, \n Длина списка: {len(filter_2)}')
    print(f' Оба условия одновременно: \n Список: {filter_3}, \n Длина списка: {len(filter_3)}')

if __name__ == '__main__':
    generate_and_filter_numbers()
