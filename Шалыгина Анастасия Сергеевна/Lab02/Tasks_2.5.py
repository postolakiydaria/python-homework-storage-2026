#!/usr/bin/env python3


def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i

    return result


if __name__ == '__main__':
    number = 0
    while True:
        user_input = input("Введите целое неотрицательное число:\n")
        try:
            number = int(user_input)
            if number < 0:
                print('Извините, математика не придумала факториал для отрицательных чисел....')
                continue
            break
        except ValueError:
            print("Плохо!! Вы ввели не целое число! Попробуйте снова!!")
    result_rec = factorial_recursive(number)
    result_iter = factorial_iterative(number)

    print(f"Факториал числа: {number}\n")
    print(f"Рекурсивный метод: {result_rec}\n")
    print(f"Иттеративный метод: {result_iter}\n")

