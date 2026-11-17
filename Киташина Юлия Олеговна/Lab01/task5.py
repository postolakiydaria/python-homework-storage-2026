#!/usr/bin/env python3

import math


def read_side(text):
    while True:
        try:
            value = float(input(text))
        except ValueError:
            print("Ошибка: введите число, например 3 или 2.5.")
            continue
        if value <= 0:
            print("Ошибка: сторона должна быть больше нуля.")
            continue
        return value


def main():
    mode = input("1 — известны два катета, 2 — гипотенуза и катет: ")

    if mode == "1":
        first = read_side("Введите первый катет: ")
        second = read_side("Введите второй катет: ")
        result = math.sqrt(first ** 2 + second ** 2)
        print("Длина неизвестной стороны:", round(result, 3))
    elif mode == "2":
        hypotenuse = read_side("Введите гипотенузу: ")
        leg = read_side("Введите известный катет: ")
        if hypotenuse > leg:
            result = math.sqrt(hypotenuse ** 2 - leg ** 2)
            print("Длина неизвестной стороны:", round(result, 3))
        else:
            print("Ошибка: гипотенуза должна быть больше катета.")
    else:
        print("Ошибка: нужно выбрать 1 или 2.")


if __name__ == "__main__":
    main()
