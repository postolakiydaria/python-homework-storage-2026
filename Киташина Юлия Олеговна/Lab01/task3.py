#!/usr/bin/env python3

DELIMITER = " "
PUNCTUATION = ".,!?;:-–—…()[]{}«»„“”\"'‘’"
VOWELS = "аеёиоуыэюяaeiou"
CONSONANTS = "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz"


def main():
    text = input("Введите строку: ")
    words = []
    for word in text.split(DELIMITER):
        if word != "":
            words.append(word)
    words = tuple(words)

    unique_words = set()
    for word in words:
        clean_word = word.lower().strip(PUNCTUATION)
        if clean_word != "":
            unique_words.add(clean_word)

    vowel_count = 0
    consonant_count = 0
    punctuation_count = 0

    for char in text.lower():
        if char in VOWELS:
            vowel_count += 1
        elif char in CONSONANTS:
            consonant_count += 1
        elif char in PUNCTUATION:
            punctuation_count += 1

    print("Кортеж слов:", words)
    print("Количество уникальных слов:", len(unique_words))
    print("Количество гласных:", vowel_count)
    print("Количество согласных:", consonant_count)
    print("Количество знаков препинания:", punctuation_count)


if __name__ == "__main__":
    main()

