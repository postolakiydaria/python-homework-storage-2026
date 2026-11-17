#!/usr/bin/env python3

ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
PUNCTUATION = ".,!?;:-–—…()[]{}«»„“”\"'‘’"
SYMBOLS = ALPHABET + PUNCTUATION
DELIMITER = " "


def main():
    mode = input("1 — текст в числа, 2 — числа в текст: ").strip()

    if mode == "1":
        text = input("Введите русский текст: ").lower()
        numbers = []
        valid = True

        for letter in text:
            if letter == " ":
                numbers.append("0")
            elif letter in SYMBOLS:
                numbers.append(str(SYMBOLS.index(letter) + 1))
            else:
                print("Недопустимый символ:", letter)
                valid = False
                break

        if valid:
            print("Шифр:", DELIMITER.join(numbers))
    elif mode == "2":
        numbers = input(f"Введите числа от 0 до {len(SYMBOLS)} через пробел: ").split(DELIMITER)
        text = ""
        valid = True

        for item in numbers:
            if item == "":
                continue
            try:
                number = int(item)
            except ValueError:
                print("Ошибка: каждое значение должно быть целым числом.")
                valid = False
                break

            if number < 0 or number > len(SYMBOLS):
                print(f"Ошибка: числа должны быть от 0 до {len(SYMBOLS)}.")
                valid = False
                break

            if number == 0:
                text += " "
            else:
                text += SYMBOLS[number - 1]

        if valid:
            print("Текст:", text)
    else:
        print("Ошибка: нужно выбрать 1 или 2.")


if __name__ == "__main__":
    main()
