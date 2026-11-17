#!/usr/bin/env python3


STANDARD_DELIMITED: str = ";"

def partition (a, l, r):
    if l>=r:
        return l, a
    x = a[l]
    j = l
    for i in range(l+1, r+1):
        if a[i]<=x:
            j+=1
            a[j], a[i] = a[i], a[j]
    a[l], a[j] = a[j], a[l]
    return j, a

def quicksort(a, l, r, ascending=True):
    if l < r:
        j, a = partition(a, l, r)
        a = quicksort(a, l, j - 1, ascending)
        a = quicksort(a, j + 1, r, ascending)
    return a


def number():
    while True:
        user_number: str = input(f'Введите числа, используя "{STANDARD_DELIMITED}"\n')
        try:
            numbers = [float(num.strip().replace(',','.')) for num in user_number.split(STANDARD_DELIMITED) if num.strip()]

            if not numbers:
                print("Плохо! Вы ничего не ввели!")
                continue
            return numbers
        except ValueError:
            print('Плохо!! Введите числа, разделенными точкой с запятой!')


def sort_numbers(numberses, increasing=True):
    if not increasing:
        result = quicksort(numberses, 0, len(numberses) - 1)
        result.reverse()
    else:
        result = quicksort(numberses, 0, len(numberses) - 1)

    return result

if __name__ == '__main__':
    numbers = number()
    print(f'Исходный список: {numbers}')
    while True:
        choice = input("Выберите тип сортировки: \n 1 - по возрастанию \n 2 - по убыванию \n")
        if choice == '1':
            result = sort_numbers(numbers, increasing=True)
            print(f'Поздравляю! Список чисел отсортирован по возрастанию: {result}')
            break
        elif choice == '2':
            result = sort_numbers(numbers, increasing=False)
            print(f'Поздравляю! Список чисел отсортирован по убыванию: {result}')
            break
        else:
            print("Плохо!! Выбор был ошибочным! Необходимо выбрать 1 или 2!")
