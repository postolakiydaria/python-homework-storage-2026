#!/usr/bin/env python3 

VOWELS = "аеёиоуыэюя"
MIN_VOWELS = 3

def count_vowels(arguments):
    count = 0
    for letter in arguments:
        if letter.lower() in VOWELS:
            count += 1
    return count


def filtered_words(**kwargs):
    result = {}

    for i, value in kwargs.items():
        if type(value) == str:
            vowels_count = count_vowels(value)
            if vowels_count >= MIN_VOWELS:
                result[i] = value
    return result


if __name__ == '__main__':
    result = filtered_words(
        name = "Акакий",
        age = "101",
        city = "спб",
        fruit = "помидор",
        hobby = "хоббихорсинг"
    )
    if result:
        print(f"Аргусенты больше, чем с {MIN_VOWELS} гласными: {result}")
    else: 
        print("Подходящих аргументов нет.")

