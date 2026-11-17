VOWELS = "аеёиоуыэюяaeiouy"

def lines_3(**kwargs):
    result = {}
    for key, value in kwargs.items():
        count = 0
        if isinstance(value, str):
            for letter in value:
                if letter.lower() in VOWELS:
                    count += 1

            if count >= 3:
                result[key] = value

    return result

if __name__ == '__main__':
    data_dict = {}
    while True:
        data_key = input('Введите значение ключа (или Enter для выхода):\n')

        if not data_key.strip():
            print('Программа завершена')
            break

        while True:
            data_val = input('Введите значение для этого ключа:\n')

            if data_val.strip():
                data_dict[data_key] = data_val.strip()
                break

            else:
                print('Вы ничего не ввели! Попробуйте еще раз\n')

    if data_dict:
        print(f'Словарь, где у значений больше 3-ех гласных: {lines_3(**data_dict)}')
    else:
        print('Вы не ввели ни одной пары ключ-значение')
