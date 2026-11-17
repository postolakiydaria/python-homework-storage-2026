import random

def sort_numbers(lst):
    '''
    Эта функция сортирует числа, выделяя из них 3 списка: список чисел, делящихся на 3 и
    не делящихся на 9, список чисел, превосходящих 20 по модулю и список, совмещающий оба условия.
    :param lst: Список чисел, на основе которого формируются 3 итоговых списка.
    :return: None: Ничего не возвращает, выводит на экран итоговые списки и их длину.
    '''
    three_division = lambda x: "fine" if x % 3 == 0 and x % 9 != 0 else ""
    more_than_twenty = lambda x: abs(x) > 20
    all_conditions = lambda x: three_division(x) and more_than_twenty(x)
    multiples_of_three = list(filter(three_division, lst))
    big_numbers = list(filter(more_than_twenty, lst))
    big_multiples = list(filter(all_conditions, lst))
    print(f"Список чисел, делящихся на 3 и не делящихся на 9: {multiples_of_three} длиной {len(multiples_of_three)}")
    print(f"Список чисел, превосходящих 20 по модулю: {big_numbers} длиной {len(big_numbers)}")
    print(f"Список чисел, делящихся на 3, не делящихся на 9 и превосходящих 20 по модулю: {big_multiples} длиной {len(big_multiples)}")

if __name__ == '__main__':
    random_list = [random.randint(-100, 100) for _ in range(20)]
    sort_numbers(random_list)
