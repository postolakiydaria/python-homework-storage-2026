#!/usr/bin/env python3

import random

def repeat_n_times(n: int):
    """
    Создает декоратор для многократного вызова функции.

    Параметры:
    n — количество повторений вызова функции.

    Возвращает:
    Функцию-декоратор.
    """
    def decorator(func):
        """
        Принимает функцию и оборачивает её логикой повторения.

        Параметры:
        func — исходная декорируемая функция.

        Возвращает:
        Функцию wrapper.
        """
        def wrapper(*args, **kwargs):
            """
            Выполняет вызов функции заданное количество раз и собирает результаты.

            Параметры:
            *args — позиционные аргументы для исходной функции.
            **kwargs — именованные аргументы для исходной функции.

            Возвращает:
            Список с результатами всех вызовов.
            """
            results = []

            for i in range(n):
                print(f"попытка {i + 1} из {n})")
                res = func(*args, **kwargs)
                results.append(res)
            return results

        return wrapper

    return decorator

@repeat_n_times(n=3)
def magic_ball(question: str) -> str:
    """
    Выдает случайное предсказание на заданный вопрос.

    Параметры:
    question — вопрос пользователя.

    Возвращает:
    Строку, содержащую исходный вопрос и случайный ответ.
    """
    answers = ["Да, точно!", "Спроси позже", "Шансы невелики", "Абсолютно!"]
    chosen = random.choice(answers)
    return f"Вопрос: {question} | Ответ: {chosen}"


if __name__ == '__main__':
    print("Магический шар:\n")
    final_results = magic_ball("я придумала 3 вопроса. Смогу ли я....")

    print("\nИтоговый список:")
    for item in final_results:
        print(item)

