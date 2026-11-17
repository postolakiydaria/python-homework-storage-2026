def fact_iterative(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def fact_recursive(n):
    if n == 0:
        return 1
    else:
        return n * fact_recursive(n-1)

if __name__ == '__main__':
    while True:
        data = input('Введите одно целое число для вычисления факториала двумя способами:\n')
        try:
            data_int = int(data)
            if data_int < 0:
                print('Факториал отрицательных чисел не определён! Попробуйте ещё раз')
                continue
            break
        except ValueError:
            print('Это не целое число! Попробуйте ещё раз')
            continue

    print(f'{int(data)}! = {fact_iterative(int(data))} итеративным методом\n'
        f'{int(data)}! = {fact_recursive(int(data))} рекурсивным методом')
