#!/usr/bin/env python3

def repeat(n):
    """
    Декоратор, который вызывает функцию n количество раз.
    Перед каждым вызовом выводит сообщение, сколько раз была вызвана функция.
    Возвращает список результатов всех вызовов.

    :param n: Количество повторений
    :return: Декоратор
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for i in range (n):
                print(f"Вызов №{i+1} из {n} функции '{func.__name__}'")
                result = func(*args, **kwargs)
                results.append(result)
            print(f"Функция '{func.__name__}' выполнена {n} раз")
            return result
        return wrapper
    return decorator


@repeat(3)
def square(n):
    """
    Возвращает квадрат числа

    :param n: Аргумент, который необходимо возвести в квадрат
    :return: Квадрат числа
    """
    return n ** 2



if __name__ == '__main__':
    res = square(3)
    print(res)
