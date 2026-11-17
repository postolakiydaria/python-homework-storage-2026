#!/usr/bin/env python3

def get_numbers():
    print("Введите числа")
    numbers = []

    while True:
        text = input("Число (чтобы выйти нажмите Enter): ")
        if text == "":
            break
        try:
            number = float(text)
            numbers.append(number)
        except ValueError:
            print("Ошибка: введите число! Попробуйте снова.\n")

    return numbers


def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


if __name__ == "__main__":
   numbers = get_numbers()
   if not numbers:
        print("Список чисел пуст!")
   else:
        result = merge_sort(numbers)
        formatted_result = [int(x) if x.is_integer() else x for x in result]
        print(f"\nЧисла по возрастанию: {formatted_result}")

