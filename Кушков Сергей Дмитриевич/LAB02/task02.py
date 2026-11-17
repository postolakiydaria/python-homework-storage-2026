#!/usr/bin/env python3

STANDARD_DELIMITED = " "
CONSTRUCTOR_ELEMENT = "; "

def header():
        while True:
            try:
                numbers_list = []
                user_input = input(f"Введите числа через пробел:\n").split()

                for value in user_input:

                    if value.isdigit():
                        numbers_list.append(int(value))
                    else:
                        raise ValueError
                break

            except ValueError:
                print(f"Ошибка! Допускаются только целые числа!")

        while True:
            user_input = input(f"Выберите способ сортировки:\n\n{STANDARD_DELIMITED}0. по возрасстанию\n{STANDARD_DELIMITED}1. по убыванию"
                                    f"\n\nВведите индекс:\n")

            if user_input in ('1','0'):
                if user_input == '0':
                    sorted_numbers = CONSTRUCTOR_ELEMENT.join(str(x) for x in sorted(numbers_list))
                    print(f'Результат  сортировки по возрастанию: \n{sorted_numbers}')
                    return sorted_numbers

                else:
                    sorted_numbers = CONSTRUCTOR_ELEMENT.join(str(x) for x in sorted(numbers_list, reverse=True))
                    print(f'Результат сортировки по убыванию \n{sorted_numbers}')
                    return sorted_numbers
            else:
                print('Индекс вне диапазона')

if __name__ == '__main__':
    header()




