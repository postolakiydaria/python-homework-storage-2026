#!/usr/bin/env python3

def main(*args):
    integers = []
    for arg in args:
        if type(arg) == int:
            integers.append(arg)
    if integers:
        result = 1
        for number in integers:
            result *= number
        return result
    else:
        print('Введены были не целые числа')
        print('Типы данных, которые Вы ввели:')
        for arg in args:
            print(f"{arg} - тип: {type(arg).__name__}")
        return

    
if __name__ == '__main__':
    print("Проверка 1: есть целые числа:")
    res = main(2, "привет", 3, 4.5, True, 5)
    print(f"Результат: {res}\n")
    print("--"*40)
    print("Проверка 2: целых чисел нет:")
    resu = main("кот", 3.14, [1,2], True)
    print(f"Результат: {resu}\n")
    print("--" * 40)
    print("Проверка 3: только одно целое число:")
    resul = main(7, "a", 2.0)
    print(f"Результат: {resul}\n")
