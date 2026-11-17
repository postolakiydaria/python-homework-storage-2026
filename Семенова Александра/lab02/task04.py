#!/usr/bin/env python3
VOWELS = ('а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'a', 'e', 'i', 'o', 'u')
MIN_VOWELS = 3

# Псевдоконстанты — тестовые наборы аргументов
DEMO_KWARGS_1 = {"имя": "Александра", "город": "Москва", "хобби": "чтение"}
DEMO_KWARGS_2 = {"a": "нет", "b": "да", "c": "привет"}
DEMO_KWARGS_3 = {"x": "ок", "y": "hi", "z": "go"}


def count_vowels(text):

    count = 0
    text_lower = text.lower()
    for char in text_lower:
        if char in VOWELS:
            count += 1
    return count


def filter_kwargs(**kwargs):
 
    result = {}

    for (key, value) in kwargs.items():
        if type(value) == str:
            vowels_count = count_vowels(value)
            if vowels_count >= MIN_VOWELS:
                result[key] = value
    return result


def print_result(result):
   
    if not result:
        print("Аргументы со строками, содержащими 3 и более гласных, не найдены.")
    else:
        print("Найденные аргументы:")
        for key, value in result.items():
            print(f"{key} = {value}")


if __name__ == "__main__":
    print("--- Тест 1: смешанные строки ---")
    print(f"Аргументы: {DEMO_KWARGS_1}")
    result_1 = filter_kwargs(**DEMO_KWARGS_1)
    print_result(result_1)
    

    print("--- Тест 2: короткие строки ---")
    print(f"Аргументы: {DEMO_KWARGS_2}")
    result_2 = filter_kwargs(**DEMO_KWARGS_2)
    print_result(result_2)
   

    print("--- Тест 3: строки с малым количеством гласных ---")
    print(f"Аргументы: {DEMO_KWARGS_3}")
    result_3 = filter_kwargs(**DEMO_KWARGS_3)
    print_result(result_3)

