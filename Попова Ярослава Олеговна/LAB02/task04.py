#!/usr/bin/env python3

VOWELS = "аеёиоуыэюяaeiouy"

def get_vowel_strings(**kwargs) -> dict[str, str]:
    matched = {}

    for key, value in kwargs.items():
        if type(value) is str:
            found_vowels = list(filter(lambda char: char in VOWELS, value.casefold()))

            if len(found_vowels) >= 3:
                matched[key] = value

    return matched

if __name__ == '__main__':
    print("Тест 1 (есть слова с 3 и более гласными):")
    res_1 = get_vowel_strings(
        first="яблокo",
        second="gross",
        third="электроника",
        number=10
    )
    print(f"Результат 1: {res_1}\n")

    print("Тест 2 (у всех строк меньше 3 гласных):")
    print("first=\"лес\",second=\"[fgh, 34]\", third=\"1.2\",is_active=True")

    res_2 = get_vowel_strings(
        first="лес",
        second="[fgh, 34]",
        third="1.2",
        is_active=True
    )

    print(f"Результат 2: {res_2}")
