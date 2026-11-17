#!/usr/bin/env python3

from functools import reduce

DELIMITER = " "

def w_statistic(words: list[str]) -> dict:
    """
    Фильтрует слова, преобразует их в словари и вычисляет статистику.

    Параметры:
    words — исходный список строк, полученный от пользователя.

    Возвращает:
    Словарь с промежуточными (отфильтрованные слова, маппинг) 
    и итоговыми (самое длинное слово, сумма букв) результатами.
    """

    filtered = list(filter(lambda w: len(w) >= 7, words))

    if not filtered:
        return {
            "filtered": [],
            "mapped": [],
            "max_word": None,
            "total_letters": 0
        }

    mapped = list(map(lambda w: {"word": w, "length": len(w)}, filtered))

    max_word = reduce(lambda acc, x: acc if acc["length"] >= x["length"] else x, mapped)

    total_letters = reduce(lambda acc, x: acc + x["length"], mapped, 0)

    return {
        "filtered": filtered,
        "mapped": mapped,
	"max_word": max_word,
	"total_letters": total_letters
    }

if __name__ == '__main__':

    while True:
        raw = input("Введите список слов: ")
        parts = raw.split(DELIMITER)

        if not parts:
            print("Вы ничего не ввели! Попробуйте снова.")
            continue
        break

    results = w_statistic(parts)

    print(f"Отфильтрованные слова (>= 7 символов): {results['filtered']}")
    print(f"Преобразованные в пары (слово, длина): {results['mapped']}")

    if not results['filtered']:
        print("Нет слов, удовлетворяющих условию (длина >= 7).")
    else:
        print(f"Слово с максимальной длиной: '{results['max_word']['word']}' (длина {results['max_word']['length']})")
        print(f"Суммарное количество букв: {results['total_letters']}")

