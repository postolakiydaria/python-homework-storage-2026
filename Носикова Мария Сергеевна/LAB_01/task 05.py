#!/usr/bin/env python3

def find_hypotenuse(a,b):
    return (a ** 2 + b ** 2) ** 0.5

def find_cathetus(a,c):
    return (c ** 2 - a ** 2) ** 0.5

if __name__ == '__main__':
    print("1 - необходимо найти гипотенузу, 2 - необходимо найти катет")
    choice = input('Ваш выбор:')
    if choice == '1':
        try:
            a = float(input('Введите первый катет:'))
            b = float(input('Введите второй катет:'))
            result = find_hypotenuse(a, b)
            print(f'Гипотенуза трегольника равна = {result:.2f}')
        except ValueError:
            print('Ошибка: нужно ввести число!')
    elif choice == '2':
        try:
            a = float(input('Введите известный катет:'))
            c = float(input('Введите гипотенузу:'))
            if a >= c:
                print('Ошибка: катет должен быть меньше гипотенузы!')
            else:
                result = find_cathetus(a, c)
                print(f'Второй катет треугольника равен = {result:.2f}')
        except ValueError:
            print('Ошибка: нужно ввести число!')
    else:
        print('Неверный выбор!')
