#!/usr/bin/env python3

MIN_FACTORIAL = 0
ERROR_NEGATIVE = "Факториал может быть определен только для неотрицательных чисел! Попробуйте снова!"
ERROR_NOT_INT = "Введите целое число без точки!"
RESULT_MATCH = "Результаты совпадают!"
RESULT_MISMATCH = "Внимание: результаты различаются!"

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n-1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def get_non_negative_int():
    print("Введите неотрицательное целое число для вычисления факториала!")

    while True:
        text = input("Число: ")

        try:
            number = int(text)

            if number < MIN_FACTORIAL:
                print(ERROR_NEGATIVE)
                continue
            return number
        except ValueError:
            print(ERROR_NOT_INT)

def print_factorial_results(n, recursive_result, iterative_result):
    print("Число:", n)
    print("Факториал (рекурсивный метод):", recursive_result)
    print("Факториал (итеративный метод):", iterative_result)

    if recursive_result == iterative_result:
        print(RESULT_MATCH)
    else:
        print(RESULT_MISMATCH)

if __name__ == "__main__":
    try:
        n = get_non_negative_int()

        recursive_result = factorial_recursive(n)
        iterative_result = factorial_iterative(n)

        print_factorial_results(n, recursive_result, iterative_result)

