#!/usr/bin/env python3

DELIMITER = ' '

def counter(var):
    var = var.replace(',', DELIMITER)
    var_split = var.split(DELIMITER)
    list_var = []
    for number in var_split:
        list_var.append(int(number))
    if len(list_var) == len(set(list_var)):
        print("условие соблюдено")
    else: 
        print("условие не соблюдено, замените")

if __name__ == '__main__':
     var = input('Введите числа через пробел:')
     counter(var)
 
