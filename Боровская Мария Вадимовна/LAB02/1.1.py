#!/usr/bin/env python3


exit_ = ""


def dlinnye_stroki(stroki):
    if not stroki:
        return []
    srednyaya = sum(len(s) for s in stroki) / len(stroki)
    return [s for s in stroki if len(s) > srednyaya]


if __name__ == "__main__":
    while True:
        spisok = []

        while True:
            vvod = input("Введите строки через пробел: ").strip()
            if not vvod:
                print("Ошибка: пустой ввод. Попробуйте еще раз.")
                continue
            spisok = vvod.split()
            if not(spisok):
                print("Ошибка: нужно хотя бы одно слово.")
                continue
            break

        print("Результат:", dlinnye_stroki(spisok))
        
        prodolzhit = input("Нажмите Enter для выхода: ").strip()
        if prodolzhit == exit_:
            break
