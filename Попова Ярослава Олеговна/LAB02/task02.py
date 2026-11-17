#!/usr/bin/env python3

DELIMITER = " "

def sort_asc(numbers: list[float]):
    n = len(numbers)
    for i in range(n):
        for j in range(n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

def sort_desc(numbers: list[float]):
    n = len(numbers)
    for i in range(n):
        for j in range(n - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

if __name__ == '__main__':
    while True:
        raw = input("Введите через пробел последовательность чисел: ")
        parts = raw.split(DELIMITER)

        if not parts:
            print("Вы ничего не ввели! Попробуйте снова.")
            continue

        try:
            nums = [float(x) for x in parts]
            break
        except ValueError:
            print("Ошибка! Вы должны ввести числа. Попробуйте снова.")

    while True:
        print("1 - по возрастанию")
        print("2 - по убыванию")
        choice = input("Что Вы желаете сделать? ").strip()

        if choice == "1" or choice == "2":
            break
        print("Ошибка! Выберите 1 или 2.")

    if choice == "1":
        sort_asc(nums)
    else:
        sort_desc(nums)

    print(f"Ваш отсортированный список: {nums}")
