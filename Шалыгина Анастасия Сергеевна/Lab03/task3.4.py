#!/usr/bin/env python3


from functools import reduce


STANDARD_DELIMITED = ","


def get_words():
    """
    Запрашивает у пользователя список слов через разделитель и возвращает его.
    Повторяет запрос, пока пользователь не введёт корректные данные

    :return: Список введённых слов
    """
    while True:
        user_input = input(f"Введите слова, используя: '{STANDARD_DELIMITED}'\n")
        try:
            words = [word.strip() for word in user_input.split(STANDARD_DELIMITED)]
            if not words:
                print('Плохо!! Список не должен быть пустым!')
                continue
            return words
        except Exception:
            print("Плохо!! Что-то пошло не так! Протрите глазки и попробуйте еще раз!")

def analyze_words():
    """
    Главная функция программы: запускает обработку слов и выводит результаты.

    :return: None (Функция только выводит результаты, но ничего не возвращает)
    """
    words = get_words()
    print(f"Исходный список слов ({len(words)}): {words}\n")
    long_words = list(filter(lambda word: len(word)>= 7, words))
    print(f"\n Оставили слова, количество букв которых больше или равно 7.\n Список: {long_words}\n Количество слов: {len(long_words)}\n ")
    word_len_pairs = list(map(lambda word: (word, len(word)), long_words))
    print("Слово - длина:")
    for pair in word_len_pairs:
        print(f" {pair[0]} - {pair[1]}\n")
    if word_len_pairs:
        max_pair = reduce( lambda a,b:a if a[1] >= b[1] else b, word_len_pairs)
        print(f" Слово с максимальной длиной: {max_pair[0]} - {max_pair[1]}\n")
    else:
        print("Нема слов подходящей длины:(\n")
    if word_len_pairs:
        total_length = reduce(lambda sums, pair: sums + pair[1], word_len_pairs, 0)
        print(f"Суммарное количество букв: {total_length}\n")
    else:
        print("Нет слов!! Одни эмоции....\n")


if __name__ == '__main__':
    analyze_words()
