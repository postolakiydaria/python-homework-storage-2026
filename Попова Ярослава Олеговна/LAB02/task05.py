#!/usr/bin/env python3

def factorial_iterative(n: int) -> int:
    result = 1
    for number in range(2, n + 1):
        result *= number
    return result

def factorial_recursive(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

if __name__ == '__main__':
    while True:
        raw = input("Введите целое неотрицательное число: ").strip()

        try:
            number = int(raw)
        except ValueError:
            print("Ошибка! Это не целое число. Попробуйте ещё раз.")
            continue

        if number < 0:
            print("Ошибка! Факториал отрицательного числа не существует.")
            continue
        break

    print(f"Итеративный метод: {factorial_iterative(number)}")
    print(f"Рекурсивный метод: {factorial_recursive(number)}")
