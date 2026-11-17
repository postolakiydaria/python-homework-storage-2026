#!/usr/bin/env python3

def repeat_function(n):
    """
    Декоратор, вызывающий функцию n раз.
    Перед вызовом каждого запуска выводит сообщение.
    Возвращает список результатов всех вызовов.

    :param n: Количество повторных вызовов функции
    :return: Декоратор
    """
    def decorator(my_func):
        def wrapper(*args, **kwargs):
            result = []
            for i in range(n):
                print(f"Вызов {i + 1} из {n}")
                result.append(my_func(*args, **kwargs))
            return result
        return wrapper
    return decorator


def my_sum(a, b):
    """
    Складывает целых два числа.

    :param a: int -  Первое значение
    :param b: int - Второе значение
    :return: int - Сумма этих значений
    """
    return a + b


if __name__ == '__main__':
    decorated_sum = repeat_function(3)(my_sum)
    result = decorated_sum(4, 5)
    print(f" Результаты всех вызовов: {result}")
