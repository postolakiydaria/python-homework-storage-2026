#!/usr/bin/env python3


exit_ = ""


def merge(left, right):
    result = []
    i = 0
    j = 0
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


def merge_sort(chisla):
    if len(chisla) <= 1:
        return chisla
    middle = len(chisla) // 2
    return merge(
        merge_sort(chisla[:middle]),
        merge_sort(chisla[middle:])
    )
    
def uporyadochit(chisla, obratno):
    otvet = merge_sort(chisla)
    if obratno:
        otvet.reverse()
    return otvet


if __name__ == "__main__":
    while True:
        chisla = []

        while True:
            vvod = input("Введите числа через пробел: ").strip()
            if not vvod:
                print("Ошибка: пустой ввод. Попробуйте еще раз.")
                continue

            chisla = []
            slova = vvod.split()
            for slovo in slova:
                try:
                    chisla.append(float(slovo))
                except ValueError:
                    print(f"Ошибка: '{slovo}' не число. Попробуйте еще.")
                    chisla = []
                    break
                    
            if len(chisla) == len(slova):
                break

        while True:
            vibor = input(
                "1 - по возрастанию, 2 - по убыванию: "
            ).strip()
            if vibor == "1" or vibor == "2":
                break
            print("Ошибка: нужно ввести 1 или 2.")

        print("Результат:", uporyadochit(chisla, vibor == "2"))

        prodolzhit = input("Нажмите Enter для выхода: ").strip()
        if prodolzhit == exit_:
            break
            
