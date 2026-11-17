#!/usr/bin/env python3


exit_ = ""


def faktorial_rekursiya(n):
    if n <= 1:
        return 1
    return n * faktorial_rekursiya(n - 1)


def faktorial_tsikl(n):
    itog = 1
    for i in range(2, n + 1):
        itog = itog * i
    return itog


if __name__ == "__main__":
    while True:
        chislo = 0

        while True:
            vvod = input(
                "Введите целое неотрицательное число: "
            ).strip()

            if not vvod:
                print("Ошибка: пустой ввод. Попробуйте еще раз.")
                continue

            proverka = vvod[1:] if vvod.startswith("-") else vvod
            if not proverka.isdigit():
                print(
                    "Ошибка: нужно целое число. "
                    "Попробуйте еще раз."
                )
                continue

            chislo = int(vvod)
            if chislo < 0:
                print(
                    "Ошибка: число не может быть отрицательным. "
                    "Попробуйте еще раз."
                )
                continue

            break

        print(f"Рекурсивно: {faktorial_rekursiya(chislo)}")
        print(f"Итеративно: {faktorial_tsikl(chislo)}")

        prodolzhit = input("Нажмите Enter для выхода: ").strip()
        if prodolzhit == exit_:
            break
