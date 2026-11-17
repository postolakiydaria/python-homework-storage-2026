def replay(n):
    """
    Декоратор, который вызывает функцию n раз и возвращает список результатов.

    :param n: количество повторных вызовов функции
    :return: декоратор
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for i in range(1, n+1):
                print(f'Запуск {i} функции {func.__name__}')
                result = func(*args, **kwargs)
                results.append(result)
                print(f'Функция {func.__name__} завершилась')
            return results
        return wrapper
    return decorator

@replay(5)
def name():
    """
    Запрашивает у пользователя любое имя

    :return: введённое пользователем имя
    """
    user_name = input('Введите любое имя:\n')
    return user_name

if __name__ == '__main__':
    names = name()
    print(f'Список имен: {names}')
