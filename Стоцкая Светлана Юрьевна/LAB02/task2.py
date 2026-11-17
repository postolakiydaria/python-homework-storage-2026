def increase(number_seq):
    temp_numbers = []
    for value in number_seq:
        try:
            temp_numbers.append(int(value))
        except ValueError:
            return "Список не был отсортирован, так как не все значения целые числа"
    decrease = input("Если хотите сортировку в порядке возрастания, введите 1,"
                     "если в порядке убывания, введите 0 ")
    if decrease == "1":
        temp_numbers.sort()
        return temp_numbers
    elif decrease == "0":
        temp_numbers.sort()
        temp_numbers.reverse()
        return temp_numbers
    else:
        return "Вы ввели неподходящее значение!"


if __name__ == '__main__':
    number_group = input("Введите набор чисел, разделённых пробелами ")
    numb_list = number_group.split()
    print(increase(numb_list))
