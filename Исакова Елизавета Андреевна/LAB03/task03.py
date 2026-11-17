import random

if __name__ == '__main__':
    random_list = [random.randint(-100, 100) for _ in range(20)]
    print(f'Список 20-ти рандомных чисел в диапазоне от -100 до 100: {random_list}')

    yes_3_no_9 = list(filter(lambda x: x % 3 == 0 and x % 9 != 0, random_list))
    more_than_20 = list(filter(lambda x: abs(x) > 20, random_list))
    both_conditions = list(filter(lambda x: x % 3 == 0 and x % 9 != 0 and abs(x) > 20, random_list))

    print(f'Числа, которые делятся на 3, но не делятся на 9: {yes_3_no_9} Длина списка: {len(yes_3_no_9)}')
    print(f'Числа, абсолютное значение которых больше 20: {more_than_20} Длина списка: {len(more_than_20)}')
    print(f'Числа, которые одновременно удовлетворяют обоим условиям: {both_conditions} Длина списка: {len(both_conditions)}')
