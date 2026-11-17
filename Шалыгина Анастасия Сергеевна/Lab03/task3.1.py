#!/usr/bin/env python3


STANDARD_DELIMITED: str = ','


classify = lambda i:(
    "zero" if i == 0
    else "negative" if i < 0
    else "positive even" if i % 2 == 0
    else "positive odd" )


def input_int_list():
    """
    Запрашивает у пользователя список целых чисел и возвращает его.

    :return: Список целых чисел
    """
    while True:
        user_input = input(f'Введите целые числа, используя "{STANDARD_DELIMITED}": \n')
        try:
            numbers = [int(num.strip()) for num in user_input.split(STANDARD_DELIMITED) ]
            if not numbers:
                print ("Плохо!! Список не должен быть пустым!!")
                continue
            return numbers
        except ValueError:
            print("Плохо!! Вы должны ввести только целые числа! Попробуй еще раз!")


if __name__ == '__main__':
    numbers = input_int_list()
    print(f'Исходный список: {numbers}')
    print("Результат классификации:")
    for number in numbers:
        result = classify(number)
        print(f'{number}: {result}')
