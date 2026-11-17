#!/usr/bin/env python3

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n-1)


def factorial_iterative(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


def number_from_user():
    user_input = input("Введите целое неотрицательное число: ")
    try:
        number = int(user_input)
    except ValueError:
        print(f"Ошибка: '{user_input} - не целое число.")
        return None
    if number < 0:
        print("Ошибка: факториал вычисляется только для неотрицательного числа.")
        return None
    return number


if __name__ == '__main__':
    number = number_from_user()
    if number is not None:
        result_recursive = factorial_recursive(number)
        result_iterative = factorial_iterative(number)

        print(f"Факториал числа {number}: ")
        print(f"реализация рекурсией: {number}!= {result_recursive}")
        print(f"реализация итерацией: {number}!= {result_iterative}")
