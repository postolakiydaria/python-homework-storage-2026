#!/usr/bin/env python3

def different_arguments(*args):
    integer = []
    not_integer = []

    for argument in args:
        if type(argument) == int:
            integer.append(argument)
        else:
            not_integer.append(argument)

    if integer:
        result = 1
        for num in integer:
            result *= num
        return ("product", result)
    elif not_integer:
        return ("not_integers", not_integer)
    else:
        return ("empty", None)


def print_result(result):
    result_type, result_value = result 
    if result_type == "product":
       print(f"Произведение целых чисел равняется: {result_value}") 
    elif result_type == "empty":
       print("Список пуст.")
    else:
       print("В спсике отсутствуют целые числа.")


if __name__ == '__main__':
    result = different_arguments(4, "привет-привет", 3.14, False, "5489", 67)
    print_result(result)

