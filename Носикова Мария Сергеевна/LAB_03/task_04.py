#!/usr/bin/env python3

from functools import reduce

MIN_WORDS_LENGTH = 7

def get_users_input(users_input):
    """
    Получает целое число от пользователя и проверяет его на тип.

    :param users_input: Запрос для пользователя 
    :return: Введенное пользователем целое число
    """
    value = None
    while value is None:
        try:
            value = int(input(users_input))
        except ValueError:
            print("Ошибка! Введите целое число")
    return value


def get_users_words():
    """
    Получает список слов от пользователя.

    :return: Список строк, введенные пользователем
    """
    words = []
    count = get_users_input("Какое количество слов хотите ввести?\n")
    for i in range(count):
        one_word = input(f"Введите слово { i + 1}: ")
        words.append(one_word)
    return words


def filter_words(words):
    """
    Оставляет только те слова, у которых длина не меньше 7 символов.

    :param words: Список слов
    :return: Список слов длиной не менее 7 символов
    """
    return list(filter(lambda x: len(x) >= MIN_WORDS_LENGTH, words))


def make_pairs(words):
    """
    Преобразует каждое слово в пару (слово, его длина).

    :param words: Список строк
    :return: Список кортежей (слово, его длина)
    """
    return list(map(lambda x: (x, len(x)), words))


def find_longest_word(pairs):
    """
    Находит слово с максимальной длиной.

    :param pairs: Список кортежей (слово, его длина)
    :return: Кортеж (слово, его длина) с максимальной длиной
    """
    return reduce(lambda a, b: a if a[1] > b[1] else b, pairs)


def final_count(pairs):
    """
    Считает суммарное количество букв во всех отфильтрованных словах.

    :param pairs: Список кортежей (слово, его длина)
    :return: Суммарное количество букв в отфильтрованных словах
    """
    return reduce(lambda acc, x: acc + x[1], pairs, 0)


if __name__ == '__main__':
    words = get_users_words()

    if not words:
        print("Список слов пуст.")
        exit(1)

    print(f"Исходный список слов:\n {words}")

    filtered = filter_words(words)
    print(f"Слова, не меньше чем с {MIN_WORDS_LENGTH} символов: {filtered}")

    if not filtered:
        print(f"Нет ни одного слова больше чем с {MIN_WORDS_LENGTH} символами")
        exit(1)
    
    pairs = make_pairs(filtered)
    print(f"Пары (слово, его длина):\n{pairs}")

    longest_words = find_longest_word(pairs)
    print(f"Слово с максимальной длиной:\n{longest_words[0]} ({longest_words[1]} букв)")

    total_count = final_count(pairs)
    print(f"Суммарное количество букв: {total_count}")
