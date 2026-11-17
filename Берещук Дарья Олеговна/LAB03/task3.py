import random
if __name__ == "__main__":
    numbers = [random.randint(-100, 100) for _ in range(20)]
    #20 рандомных чисел от -100 до 100

    #print(numbers)
    divisible_by_3_not_9 = list(filter(lambda x: x % 3 == 0 and x % 9 != 0, numbers))
    #фильтруем те, которые делятся на 3 но не на 9.
    #получается список с группой чисел, отфильтрованных по 1 признаку


    #print(divisible_by_3_not_9)
    abs_more_than_20 = list(filter(lambda x: abs(x) > 20, numbers))
    #фильтрую те модуль которых больше 20. группа по 2 признаку

    #print(abs_more_than_20)
    both = list(filter(lambda x: abs(x) > 20, divisible_by_3_not_9))
    #поиск чисел, которые соответствуют обоим условиям. для этого отфильтрованный по первому признаку список фильтрую по второму признаку"""

    print(f"Делятся на 3, но не на 9:\n {divisible_by_3_not_9}\n"
          f"Количество элементов {len(divisible_by_3_not_9)}\n"
          f"Модуль больше 20:\n{abs_more_than_20}\n"
          f"Количество элементов {len(abs_more_than_20)}\n"
          f"Попадают в обе перечисленные группы:\n{both}\n"
          f"Количество элементов {len(both)}\n")

