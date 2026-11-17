#!/usr/bin/env python3

from collections.abc import Callable

klassifikatsiya: Callable[[int], str] = lambda znachenie: (
    ("positive even" if znachenie % 2 == 0 else "positive odd")
    if znachenie > 0
    else ("negative" if znachenie < 0 else "zero")
)

if __name__ == "__main__":
    while True:
        vvod: str = input("Введите целые числа через пробел: ")
        try:
            chisla: list[int] = [int(token) for token in vvod.split()]
            if not chisla:
                raise ValueError
            break
        except ValueError:
            print("Нужно ввести одно или несколько целых чисел.")

    rezultaty: list[str] = list(map(klassifikatsiya, chisla))

    for chislo, rezultat in zip(chisla, rezultaty):
        print(f"{chislo}: {rezultat}")
