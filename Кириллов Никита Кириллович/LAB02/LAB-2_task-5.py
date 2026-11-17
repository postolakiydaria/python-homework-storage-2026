#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def fact_iter(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def fact_recur(n):
    if n <= 1:
        return 1
    return n * fact_recur(n - 1)


if __name__ == '__main__':
    while True:
        user_answer = input("Введите целое положительное число: ")
        try:
            num = int(user_answer)

            if num < 0:
                print("Ошибка! Факториал отрицательного числа не существует.")
                continue
            break

        except ValueError:
            print("Ошибка! Пожалуйста, введите целое число.")

    print(f"Результат (итеративный метод): {fact_iter(num)}")
    print(f"Результат (рекурсивный метод): {fact_recur(num)}")
    
