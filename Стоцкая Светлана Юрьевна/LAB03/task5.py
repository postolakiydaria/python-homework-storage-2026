def decorator_with_n(arg):
    '''
    Декоратор, декорирующий функцию и вызывающий её n раз. Перед каждым вызовом выводит сообщение.
    :param arg: Количество раз, которое функция будет вызвана.
    :return: Список результатов всех вызовов функции.
    '''
    def decorator(func):
        def inner_func(*args, **kwargs):
            final_list = []
            print("Вызываем глупенькую функцию для преобразования чисел...")
            for i in range(arg):
                final_list.append(func(*args, **kwargs))
            return final_list
        return inner_func
    return decorator

@decorator_with_n(5)
def useless_func(value):
    '''
    Эта функция умножает полученное число на 3 и прибавляет к значению 1.
    :param value: Какое-то число.
    :return: None: Ничего не возвращает, выводит на экран итоговое значение.
    '''
    try:
        return (value * 3) + 1
    except ValueError:
        return "Мне нужно число, а не другое значение!"

if __name__ == '__main__':
    result = useless_func(1)
    print(f"Список значений, полученный при вызове декорированной функции {result}")
