def list_reduce(lst):
    avg_line = 0
    final_list = []
    for line in lst:
        avg_line += len(line)
    avg_line /= len(lst)
    for smth in lst:
        if len(smth) > avg_line:
            final_list.append(smth)
    return final_list

if __name__ == '__main__':
    strings_list = []
    condition = "fine"
    while condition:
        strings_list.append(input("Введите строку "))
        condition = input("Если строки закончились, нажмите Enter ")
    print(list_reduce(strings_list))
