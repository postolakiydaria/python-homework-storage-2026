#!/usr/bin/env python3


VOWELS = "уеёыаоэяию"


def count_vowels(text):
    text = text.lower()
    count = 0
    for char in text:
        if char in VOWELS:
            count += 1
    return count


def main(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if type(value) == str:
            vowels_count = count_vowels(value)
            if vowels_count >= 3:
                result[key] = value
    return result


if __name__ == "__main__":
    print ("Проверка 1: Разные типы данных")
    res = main(name="Валера", age=20, city="Москва", pet="Кот")
    print(f'Вот что вышло:{res}\n')
    print('--'*40)
    print("Проверка 2: Нет подходящего типа данных")
    res2=main(a="a", b=["Валера"], c=345, e=True)
    print(f'Вот что вышло:{res2}\n')
    print('--'*40)
    print("Проверка 3: Все подходит")
    res3 = main(name="Екатерина", pet='Попугай', city='Новосибирск')
    print(f'Вот что вышло:{res3}\n')
    print('--'*40)
    print("Проверка 4: Пустой словарь")
    res4 = main()
    print(f'Вот что вышло:{res4}\n')
