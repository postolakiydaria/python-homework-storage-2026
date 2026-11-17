#!/usr/bin/env python3

LIST_VOWELS = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
LIST_CONSONANTS = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
LIST_PUNCTUATION = ",./?:;-_!"

def count_signs(text):
    vowels = 0
    consonants = 0
    punctuation = 0
    for letter in text:
        if letter in LIST_VOWELS:
            vowels += 1
        elif letter in LIST_CONSONANTS:
            consonants += 1
        elif letter in LIST_PUNCTUATION:
            punctuation += 1
    return vowels, consonants, punctuation

def uniqueness(text):
    words = tuple(text.split())
    unique_words = set(words) # для удаления дубликатов
    unique_count = len(unique_words)
    vowels, consonants, punctuation = count_signs(text)
    return words, unique_count, vowels, consonants, punctuation

if __name__ == '__main__':
    text = input('Введите строку слов, разделенную пробелами:')
    text = text.strip()
    words, unique_count, vowels, consonants, punctuation = uniqueness(text)

    print(f'Исходная строка:{text}')
    print(f'Кортеж слов:{words}')
    print(f'Количество уникальных слов: {unique_count}')
    print(f'Гласные буквы: {vowels}')
    print(f'Согласные буквы: {consonants}')
    print(f'Знаки препинания: {punctuation}')
