#!/usr/bin/env python3

DELIMITER = " "

def filter_texts(data: list[str]) -> list[str]:
    sizes = list(map(len, data))
    avg = sum(sizes) / len(sizes)

    return [s for s in data if len(s) > avg]


if __name__ == '__main__':
    raw = input("Введите слова через пробел: ")
    parts = raw.split(DELIMITER)

    if not parts:
        print("Ошибка: вы ввели пустую строку!")
    else:
        res = filter_texts(parts)
        print(f"Результат: {res}")
