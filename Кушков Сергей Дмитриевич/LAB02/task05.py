#!/usr/bin/env python3

def recursive(n):

    if n in (0, 1):
        return 1

    return n*recursive(n-1)

def iterative(n):

    if n == 0:
        return 1

    for a in range(1,n):
        n = n * a
    return n

if __name__ == '__main__':

    true_num = 0

    while True:
        num = input("Введите челое число:\n")
        if num.isdigit():
            true_num: int = int(num)
            break

        else:
            print('Введите целое положительное число!')

    result_recursive = recursive(true_num)
    result_iterative = iterative(true_num)
    print(f"Факториал через функцию рекурсивным методом: {result_recursive}")
    print(f"Факториал через функцию итеративным способом: {result_iterative}")




