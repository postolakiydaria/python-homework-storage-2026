#!/usr/bin/env python3
#-*- coding: utf-8 -*-

DELIMITER = ' '

def long_strings(words: list[str]) -> list[str]:
    """
    Возвращает список строк, длина которых превышает среднюю.

    :param words: исходный список строк
    :return: отфильтрованный список
    """
    if not words:
        return []
    lengths = [len(word) for word in words]
    average_len = sum(lengths) / len(lengths)
    return [word for word in words if len(word) > average_len]


def main() -> None:
    """
    Точка входа программы.
    :return: None
    """
    user_answer = input("Введите слова через пробел: ").split(DELIMITER)
    user_answer = [word for word in user_answer if word]

    if not user_answer:
        print("Ошибка! Введите список строк!")
    else:
        result = long_strings(user_answer)
        print(f"Список со строками длиннее среднего значения: {result}")


if __name__ == '__main__':
    main()
    
