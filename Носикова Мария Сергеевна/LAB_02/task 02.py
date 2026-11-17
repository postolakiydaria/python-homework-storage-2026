#!/usr/bin/env python3

def sort_numbers(numbers, choice):
    if choice == "1":
        return sorted(numbers)
    elif choice == "2":
        return sorted(numbers, reverse = True)
    else:
        print("Неверный выбор. По умолчанию совершается сортировка по возрастанию.")
        return sorted(numbers)


if __name__ == '__main__':
    users_input = input("Введите числа через пробел:\n")
    users_input = users_input.replace(",", " ")
    list_str = users_input.split() 

    numbers = []
    for number in list_str:
        try:
            numbers.append(int(number))
        except ValueError:
            continue

    if numbers:
        print("Сортировка по возрастанию - 1, по убыванию - 2")
        choice = input("Ваш выбор:\n")
        result = sort_numbers(numbers, choice)

        print(f"Исходный список: {numbers}")
        print(f"Отсортированный список: {result}")
    else: 
        print("Числа не введены")
