#!/usr/bin/env python3


import argparse

DEFAULT_PRECISION = 2

def calculate(x, y, operation):
    """
    Выполняет математическую операцию.
    :param x: Первое число.
    :param y: Второе число.
    :param operation: Строка с названием операции (add, sub, mul, div).
    :return: Результат операции.
    :raises ValueError: Если операция неизвестна или происходит деление на ноль.
    """
    if operation == "add":
        return x + y
    elif operation == "sub":
        return x - y
    elif operation == "mul":
        return x * y
    elif operation == "div":
        if y == 0:
            raise ValueError("Деление на ноль невозможно!")
        return x / y
    else:
        raise ValueError(f"Неизвестная операция: {operation}")

def save_result(filepath, result_text):
    """
    Сохраняет результат в файл (дописывает в конец, не стирая старое).
    :param filepath: Путь к файлу.
    :param result_text: Текст для сохранения.
    """
    with open(filepath, "a", encoding="utf-8") as file: # Режим "a" означает append. Если файла нет, он создастся.
        file.write(result_text + "\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="calculator_script",
                                     description="Скрипт-калькулятор с сохранением истории.",
                                     epilog="Удачных вычислений!")

    parser.add_argument("x", type=float, help="Первое число")
    parser.add_argument("y", type=float, help="Второе число")
    parser.add_argument("-o", "--operation", type=str, choices=["add", "sub", "mul", "div"], help="Операция: add, sub, mul, div")
    parser.add_argument("-p", "--precision", type=int, default=DEFAULT_PRECISION, help="Количество знаков после запятой")
    parser.add_argument("-f", "--file", type=str, help="Файл для сохранения результата")

    args = parser.parse_args()

    if not args.operation:
        print(f"x = {args.x}, y = {args.y}")
    else:
        try:
            result = calculate(args.x, args.y, args.operation)
            formatted_result = f"{result:.{args.precision}f}"
            print(formatted_result)
            if args.file:
                save_result(args.file, formatted_result)
                print(f"Результат сохранен в файл: {args.file}")
        except ValueError as e:
            print(f"Ошибка вычисления: {e}")
