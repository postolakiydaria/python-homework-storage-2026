#!/usr/bin/env python3

from functools import wraps
import random


DEFAULT_REPEAT_COUNT = 3
MIN_RANDOM_VALUE = 0
MAX_RANDOM_VALUE = 50


def factorial(n):
    """
    Вычисляет факториал числа n.

    :param n: неотрицательное целое число.
    :return: факториал числа n.
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def repeat(n):
    """
    Декоратор, который вызывает декорируемую функцию n раз.

    Перед каждым вызовом выводится сообщение с номером попытки.
    Возвращает список результатов всех вызовов.

    :param n: количество повторных вызовов функции.
    :return: декоратор, оборачивающий исходную функцию.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for i in range(1, n + 1):
                print(f"[Попытка {i} из {n}] Вызываю '{func.__name__}'...")
                result = func(*args, **kwargs)
                results.append(result)
            print(f"Функция '{func.__name__}' выполнена {n} раз.\n")
            return results
        return wrapper
    return decorator


@repeat(DEFAULT_REPEAT_COUNT)
def square(x):
    """
    Возвращает квадрат числа.

    :param x: число.
    :return: квадрат числа x.
    """
    return x ** 2


@repeat(5)
def random_square():
    """
    Генерирует случайное целое число от 0 до 100 и возвращает его квадрат.

    :return: кортеж (число, квадрат числа).
    """
    n = random.randint(0, 100)
    return n, n ** 2


@repeat(4)
def random_factorial():
    """
    Генерирует случайное целое число от 0 до 50 и возвращает его факториал.

    :return: кортеж (число, факториал числа).
    """
    n = random.randint(MIN_RANDOM_VALUE, MAX_RANDOM_VALUE)
    return n, factorial(n)


if __name__ == "__main__":

    print("1. Вызов функции square(4):")
    result1 = square(4)
    print(f"Результаты: {result1}\n")

    print("2. Вызов функции random_square() (диапазон 0–100):")
    result2 = random_square()
    print("Результаты:")
    for number, sq in result2:
        print(f"Квадрат {number} = {sq}\n")

    print("3. Вызов функции random_factorial() (диапазон 0–50):")
    result3 = random_factorial()
    print("Результаты:")
    for number, fact in result3:
        print(f"{number}! = {fact}")
