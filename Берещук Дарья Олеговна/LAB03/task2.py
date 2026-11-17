
PRODUCTS = [
    {"name": "Laptop", "price": 89990, "discount": 10},
    {"name": "Mouse", "price": 2490, "discount": 15},
    {"name": "Keyboard", "price": 5490, "discount": 0},
    {"name": "Monitor", "price": 27990, "discount": 25},
]

def insertion_sort(items: list, key=lambda x: x):
    """
    Сортировка вставками по key
    :param items:список элементов для сортировки
    :param key: функция, возвращающая ключ сравнения (по умолчанию сам элемент)
    :return: новый отсортированный список, исходный items не изменяется
    """
    result = list(items)
    for i in range(1, len(result)):
        current = result[i]
        j = i - 1
        while j >= 0 and key(result[j]) > key(current):
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = current
    return result


if __name__ == "__main__":
    products_with_final = list(map(lambda p: {**p, "final_price": round(p["price"] * (1 - p["discount"] / 100), 2)}, PRODUCTS))
    #распаковываем словарь, получается равный предыдущему, но еще рассчитываю и добавляю туда финальную цену с учетом скидки

    sorted_products = insertion_sort(products_with_final, key=lambda p: p["final_price"])
    #сортитовка по финальной цене

    print("Отсортировано по final_price:\n")
    for p in sorted_products:
        print(p)


