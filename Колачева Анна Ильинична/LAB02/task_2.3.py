#!/usr/bin/env python3


def types_int(*args: object) -> int | str:
    int_el: list[int] = [arg for arg in args if type(arg) is int and not isinstance(arg, bool)]

    if not int_el:
        if not args:
            return "Аргументы не были переданы."
            
        other_types = []
        for arg in args:
            other_types.append(f"'{arg}' ({type(arg).__name__})")
            
        return f"Целые числа не найдены. Получены следующие значения:\n  {', '.join(other_types)}"

    result = 1
    for num in int_el:
        result *= num
        
    return result


    
if __name__ == '__main__':
    print("Проверка 1: есть целые числа")
    res1 = types_int(2, "привет", 3, 4.5, True, 5)
    print(f"Результат: {res1}\n")
    
    print("*" * 40)
    
    print("Проверка 2: целых чисел нет")
    res2 = types_int("кот", 3.14, [1, 2], True)
    print(f"Результат: {res2}\n")
    
    print("*" * 40)
    
    print("Проверка 3: только одно целое число")
    res3 = types_int(7, "a", 2.0)
    print(f"Результат: {res3}\n")
    
    print("*" * 40)
    
    print("Проверка 4: пустой вызов")
    res4 = types_int()
    print(f"Результат: {res4}")
