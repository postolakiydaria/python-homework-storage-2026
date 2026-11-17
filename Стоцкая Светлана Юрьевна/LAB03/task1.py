def determine_numbers(some_list):
    '''
    Эта функция проверяет, какое введённое число: отрицательное, положительное (чётное/нечётное) или ноль и выводит результат.
    :param some_list: Список чисел, полученный от пользователя.
    :return: None: Ничего не возвращает, выводит на экран пары "число - значение функции".
    '''
    func = lambda x: "zero" if x == 0 else ("negative" if x < 0 else
                        ("positive even" if x % 2 == 0 else "positive odd"))
    for value in some_list:
        try:
            final_val = int(value)
            print(final_val, "-", func(final_val))
        except ValueError:
            print("Вы ввели не целое число!")

if __name__ == '__main__':
    number_group = input("Введите набор чисел через пробел ")
    value_list = number_group.split()
    determine_numbers(value_list)
