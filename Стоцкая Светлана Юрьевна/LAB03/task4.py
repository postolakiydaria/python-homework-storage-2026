from functools import reduce

def reform_list(strings_list):
    '''
    Эта функция фильтрует список строк, удаляя неподходящие и изменяя способ записи.
    :param strings_list: Список строк, полученный от пользователя.
    :return: None: Ничего не возвращает, выводит на экран промежуточные и итоговые значения.
    '''
    cut = lambda x: len(x) >= 7
    cut_list = list(filter(cut, strings_list))
    pair = lambda x: (x, len(x))
    paired_dict = dict(map(pair, cut_list))
    maximum = reduce(lambda counter, x: x if paired_dict[counter] < paired_dict[x] else counter, paired_dict)
    fin_number = reduce(lambda counter, x: counter + paired_dict[x], paired_dict, 0)
    print(f"Список после убирания слов длиной менее 7 символов {cut_list}")
    print(f"Список после преобразований чисел в пары {paired_list}")
    print(f"Слово с максимальной длиной {maximum}")
    print(f"Суммарное количество символов во всех отфильтрованных словах {fin_number}")

if __name__ == '__main__':
    some_list = []
    while True:
        some_str = input("Введите строку ")
        if some_str == "":
            break
        some_list.append(some_str)
    reform_list(some_list)
