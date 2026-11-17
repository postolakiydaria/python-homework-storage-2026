#!/usr/bin/env python3

from functools import reduce

my_lambda = lambda x: (
    "positive even" if x > 0 and x % 2 == 0 else
    "positive odd" if x > 0 and x % 2 !=0 else
    "negative" if x < 0 else
    "zero"
)


def get_user_input(user_input):
    """"
    Получает целое число от пользователя с проверкой типа.

    :param user_input: текст запроса для пользователя
    :return: введеное целое число.
    """
    value = None
    while value is None:
        try:
            value = int(input(user_input))
        except ValueError:
            print("Ошибка. Необходимо ввести целое число.")
    return value


if __name__ == '__main__':
    count = get_user_input("Сколько чисел хотите ввести?\n")

    if count <= 0:
        print ("Количество чисел должно быть больше нуля.")
        exit(1)
    numbers = []
    for i in range(count):
        numbers.append(get_user_input(f"Введите число {i + 1}: "))
    result = list(map(my_lambda, numbers))
    total = reduce(lambda acc, x: acc + x, numbers, 0)

    print("Результат:\n")
    for i in range(len(numbers)):
        print(numbers[i], "-", result[i])
    print(f"Сумма всех чисел:\n {total}")
