#!/usr/bin/env python3

STANDARD_DELIMITED: str = ' '
GLASNYE = ('у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю', 'ё')
ZNAKI = ('!', ';', ':', '?', ',', '.', '-', ' ')

if __name__ == '__main__':
    stroka: str = input(f"Введите строку слов. Используйте {STANDARD_DELIMITED}, как ' ' \n").lower()
    kortezh = tuple(stroka.split())
    kol_gl = 0
    kol_sogl = 0
    kol_punct = 0
    colichestvo_slov = len(set(kortezh))

    for sm in stroka:
        if sm in GLASNYE:
            kol_gl += 1
        elif sm in ZNAKI:
            kol_punct += 1
        else:
            kol_sogl += 1



        print(f'Количество уникальных слов: {colichestvo_slov}\n')
        print(f'Количество гласных букв: {kol_gl}\n')
        print(f'Количество согласных букв: {kol_sogl}\n')
        print(f'Количество пунктуационных символов: {kol_punct}\n')

