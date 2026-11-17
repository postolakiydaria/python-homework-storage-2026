#!/usr/bin/env python3


def umnozhit_tselye(*args):
    tselye = [z for z in args if type(z) is int]
    if not tselye:
        print("Ошибка: циферки пиши (инты)!")
        for z in args:
            print(f"  Значение: {z}, Тип: {type(z).__name__}")
        return None

    itog = 1
    for chislo in tselye:
        itog = itog * chislo
    return itog


if __name__ == "__main__":
    rezultat_1 = umnozhit_tselye(3.22, True, "аргумент")
    rezultat_2 = umnozhit_tselye(1, 2, 3)

    if rezultat_1 is not None:
        print("Результат 1:", rezultat_1)
    if rezultat_2 is not None:
        print("Результат 2:", rezultat_2)
