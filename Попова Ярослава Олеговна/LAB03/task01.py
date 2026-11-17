#!/usr/bin/env python3
DELIMITER = " "

def get_number_categories(numbers: list[int]) -> list[tuple[int, str]]:

    """
    Определяет категорию каждого числа (положительное/отрицательное, четное/нечетное).

    Параметры:
    numbers — список чисел для проверки.

    Возвращает:
    Список пар, где первый элемент — само число, а второй — строка с его категорией.
    """
    categorize = lambda x: "zero" if x == 0 else (
        "negative" if x < 0 else (
            "positive even" if x % 2 == 0 else "positive odd"
        )
    )

    return [(num, categorize(num)) for num in numbers]

if __name__ == '__main__':
    while True:
        raw = input("Введите целые числа через пробел: ")
        parts = raw.split(DELIMITER)
        clean_parts = list(filter(None, parts))

        if not parts:
            print("Ошибка! Вы ничего не ввели")
            continue

        try:
            nums = [int(x) for x in parts]
            break
        except ValueError:
            print("Ошибка! Нужно вводить только целые числа.")

    results = get_number_categories(nums)

    print("Результаты проверки:")
    for num, category in results:
        print(f"{num} — {category}")

