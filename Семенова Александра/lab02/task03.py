#!/usr/bin/env python3

TRUE_VALUES = ("True", "true", "1")
FALSE_VALUES = ("False", "false", "0")

DEMO_ARGUMENTS_1 = ("3", "hello", "5", "2.5", "True", "world", "4")
DEMO_ARGUMENTS_2 = ("3.14", "hello", "True", "2.5")
DEMO_ARGUMENTS_3 = ("2", "3", "4", "5")


def parse_value(text):
   
    text = text.strip()

    if text in TRUE_VALUES or text in FALSE_VALUES:
        if text in TRUE_VALUES:
            return True
        else:
            return False

    try:
        return int(text)
    except ValueError:
        pass

    try:
        return float(text)
    except ValueError:
        pass

    return text


def multiply_integers(*args):

    product = 1
    has_integer = False
    non_integers = []

    for arg in args:
        if type(arg) is int:
            product = product * arg
            has_integer = True
        else:
            non_integers.append((arg, type(arg)))

    if has_integer:
        return product
    else:
        return non_integers


def print_result(result):
  
    if type(result) is int:
        print("Произведение целочисленных аргументов:", result)
    else:
        print("Целочисленные аргументы не были поданы.")
        print("Нецелые значения и их типы:")
        for pair in result:
            value = pair[0]
            arg_type = pair[1]
            print(f"  Значение: {value} | Тип: {arg_type}")


def parse_arguments(raw_args):
    
    return tuple(parse_value(arg) for arg in raw_args)


if __name__ == "__main__":
    
    print("--- Тест 1: смешанные аргументы ---")
    parsed_args_1 = parse_arguments(DEMO_ARGUMENTS_1)
    print(f"Исходные аргументы: {parsed_args_1}")
    result_1 = multiply_integers(*parsed_args_1)
    print_result(result_1)
 

    print("--- Тест 2: только нецелые аргументы ---")
    parsed_args_2 = parse_arguments(DEMO_ARGUMENTS_2)
    print(f"Исходные аргументы: {parsed_args_2}")
    result_2 = multiply_integers(*parsed_args_2)
    print_result(result_2)
 

    print("--- Тест 3: только целые числа ---")
    parsed_args_3 = parse_arguments(DEMO_ARGUMENTS_3)
    print(f"Исходные аргументы: {parsed_args_3}")
    result_3 = multiply_integers(*parsed_args_3)
    print_result(result_3)
    

    print("--- Тест 4: аргументы разных типов напрямую ---")
    print("Аргументы: 10, 'text', 3, 2.7, False, 5")
    result_4 = multiply_integers(10, "text", 3, 2.7, False, 5)
    print_result(result_4)

