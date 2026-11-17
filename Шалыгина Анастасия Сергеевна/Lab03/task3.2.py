#!/usr/bin/env python3


def bubble_sort(arr, key=None):
    """
    Сортирует список методом пузырька по возрастанию

    :param arr: Список для сортировки
    :param key: Функция для получения значения сравнения
    :return: Отсортированный список
    """
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            val1 = key(arr[j]) if key else arr[j]
            val2 = key(arr[j+1]) if key else arr[j+1]
            if val1 > val2:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def calculate_and_sort_products():
    """
    Вычисляет итоговую цену товаров с учётом скидки и сортирует их по возрастанию

    :return: None (функция только выводит результаты, но ничего не возвращает)
    """
    PRODUCTS: list =  [
        {"name": "Laptop", "price": 89990, "discount": 10},
        {"name": "Mouse", "price": 2490, "discount": 15},
        {"name": "Keyboard", "price": 5490, "discount": 0},
        {"name": "Monitor", "price": 27990, "discount": 25},
    ]
    final_price = lambda product:{**product, "final_price": product["price"] * (1-product["discount"]/100)}
    products_with_final_price = list(map(final_price, PRODUCTS))
    sorted_products = bubble_sort(products_with_final_price, key=lambda x: x["final_price"])
    print("Исходный список товаров:")
    for product in PRODUCTS:
        print(f' {product}')
    print('\n Отсортированный список продуктов:')
    for product in sorted_products:
        print(
            f"{product['name']},"
            f"цена = {product['price']}",
            f"скидка = {product['discount']}",
            f"итоговая цена = {product['final_price']}"
        )


if __name__ == '__main__':
    calculate_and_sort_products()
