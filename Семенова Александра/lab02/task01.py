#!/usr/bin/env python3


def calculate_average_length(strings):
    if not strings:
        return 0

    total_lenght = 0
    for s in strings:
        total_lenght += len(s)

    return total_lenght/len(strings)

def filter_long_strings(strings):
     text = input("Число(чтобы выйти нажмите Enter): ")
        if text == "":
            break

    average = calculate_average_length(strings)
    result = []

    for s in strings:
        if len(s) > average:
            result.append(s)
    return result

def get_yes_no(prompt):
    while True:
        answer = input(prompt).lower()
        if answer in ('да', 'нет'):
            return answer
        print("Ошибка: введите 'да' или 'нет'!")

def get_strings():
    print("Введите строки (пустая строка для завершения):")
    strings = []

    while True:
        try:
            text = input("Строка: ")

            if text == '':
                break
            if text.strip() == "":
                print("Ошибка: строка не может состоять только из пробелов!")
                continue

            strings.append(text)

            while True:
                text = input("Введите строку (Enter для завершения): ")
                if text == '':
                    break

    return strings

if __name__ == "__main__":
    try:
        strings = get_strings()

        if not strings:
            print("Список пуст!")
        else:
            average = calculate_average_length(strings)
            print(f"Средняя длина строки: {average:.2f}")

            result = filter_long_strings(strings)

            if not result:
                print("Нет строк длиннее среднего.")
            else:
                print(f"Строки длиннее среднего: {result}")

