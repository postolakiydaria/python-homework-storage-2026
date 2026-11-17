#Напишите функцию, которая принимает последовательность чисел от пользователя и определяет, все ли они различны.
#!/usr/bin/env python3

STANDARD_DELIMITED: str = ', '


if __name__ == '__main__':
    posl_chisel: str = input(f'Введите последовательность чисел. Используйте "{STANDARD_DELIMITED}"\n')
    number_list: list = posl_chisel.strip().split(STANDARD_DELIMITED)
    number_set: set = set(number_list)
    if len(number_set) == len(number_list):
        print('Отлично! Все числа различны!')
    else:
        print('Плохо!!! Есть повторы! Протри глаза и попробуй заново!')
