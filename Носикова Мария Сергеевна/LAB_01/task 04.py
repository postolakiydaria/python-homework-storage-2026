#!/usr/bin/env python3

DIGIT_TO_LETTER = {
    '0': 'a',
    '1': 'б',
    '2': 'в',
    '3': 'г',
    '4': 'д',
    '5': 'е',
    '6': 'ж',
    '7': 'з',
    '8': 'и',
    '9': 'к'
}

LETTER_TO_DIGIT = {
    'а': '0',
    'б': '1',
    'в': '2',
    'г': '3',
    'д': '4',
    'е': '5',
    'ж': '6',
    'з': '7',
    'и': '8',
    'к': '9'
}

def encode_text(numbers): # цифры -> буквы
    code = str.maketrans(DIGIT_TO_LETTER)
    result = numbers.translate(code)
    return result

def decode_numbers(text):
    scheme = str.maketrans(LETTER_TO_DIGIT)
    result = text.translate(scheme)
    return result

def what_want(choice, data):
    if choice == '1':
        result = encode_text(data)
        return f'Зашифрованный текст: {result}'
    elif choice == '2':
        result = decode_numbers(data)
        return f'Зашифрованные цифры: {result}'
    else: 
        return 'Ваш выбор неверен'
    
if __name__ == '__main__':
    print("Шифр: 0 = а, 1 = б, 2 = в, 3 = г, 4 = д, 5 = е, 6 = ж, 7 = з, 8 = и, 9 = к")
    print("Выберите действие:\n1 - Зашифровать числа в буквы\n2 - Расшифровать буквы в числа")
    choice = input('Ваш выбор: ')
    if choice == '1':
        data = input("Введите числовую последовательность (например, 12345): ")
    elif choice == '2':
        data = input("Введите буквенный текст (например, абвгде): ")
    else:
        data = ""
    result = what_want(choice, data)
    print(result)
