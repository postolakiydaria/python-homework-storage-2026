#!/usr/bin/env python3

classify = lambda n: "positive even" if n > 0 and n % 2 == 0 else "positive odd" if n > 0 else "negative" if n < 0 else "zero"

def read_integers():
    """
    Считывает целые числа от пользователя до пустого ввода.

    :return: список целых чисел, успешно распознанных во вводе.
    """
    print("Введите целые числа через пробел.")
    print("Пустой ввод (Enter) — завершить.\n")
    
    numbers = []
    while True:
        raw = input("Числа: ").strip()
        if not raw:
            break
        for item in raw.split():
            try:
                numbers.append(int(item))
            except ValueError:
                print(f"'{item}' - не целое число, пропускаем.")
    return numbers


if __name__ == "__main__":

    numbers = read_integers()

    if not numbers:
        print("Вы не ввели ни одного корректного числа.")
    else:
        print("\nРезультат:")
        for n in numbers:
            print(f"{n:>6} : {classify(n)}")

    input("\nНажмите Enter для выхода.")

