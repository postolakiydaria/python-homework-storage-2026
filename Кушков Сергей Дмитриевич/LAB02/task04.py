#!/usr/bin/env python3

TARGET_LETTERS: tuple = 'а','и','е','у','ы','о','э','я','ю'

def letter_dict(**words):

    filtered_dict = {}
    for key, value in words.items():

        if isinstance(value, str):

            lower_value = value.lower()
            char_num = 0
            for char in lower_value:
                if char in TARGET_LETTERS:
                    char_num += 1

            if char_num >= 3:
                filtered_dict[key] = value

    return filtered_dict


if __name__ == '__main__':

    letters = letter_dict(
                author = "Тоби",
                type = "Сказка",
                name = "Подземелье",
                main_hero = "Фриск",
                num = 1,
                route = "Пацифизм"
                )
    print(letters)


