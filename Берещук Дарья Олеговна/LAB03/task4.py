from functools import reduce
STANDARD_DELIMITER = " "


if __name__ == "__main__":
    raw = input(f"Введите строки через {STANDARD_DELIMITER}\n").split(STANDARD_DELIMITER)
    long_words = list(filter(lambda r: len(r) >= 7, raw))
    #оставляем только строки длиной 7 и более символов

    print(f"Слова строки из >=7 символов:\n{long_words}")

    pairs = dict(map(lambda w: (w, len(w)), long_words))
    print(f"Пары «строка — длина»:\n{pairs}")

    #делаю словарь пар строка и ее длина

    longest = max(pairs.items(), key=lambda x: x[1])
    print(f"Максимальная длина - {longest[1]}")

    total_len = reduce(lambda total, length: total + length, pairs.values(), 0)
    #суммирую все длины

    print(f"Суммарная длина = {total_len}")
