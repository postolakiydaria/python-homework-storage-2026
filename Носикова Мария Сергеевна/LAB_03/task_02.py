#!/usr/bin/env python3

PRODUCTS = [
    {"name": "Laptop", "price": 89990, "discount": 10},
    {"name": "Mouse", "price": 2490, "discount": 15},
    {"name": "Keyboard", "price": 5490, "discount": 0},
    {"name": "Monitor", "price": 27990, "discount": 25},
]


def quicksort(products):
    """
    Сортирует список товаров по возрастанию с помощью алгоритма быстрой сортировки.

    :param products: Список словарей с информацией о товарах.
    :return: Отсортированный список товаров 
    """
    if len(products) <= 1:
        return products

    pivot = products[len(products) // 2]
    pivot_vot = pivot["final_price"]
    left = [x for x in products if x["final_price"] < pivot_vot]
    middle = [x for x in products if x["final_price"] == pivot_vot]
    right = [x for x in products if x["final_price"] > pivot_vot]
    return quicksort(left) + middle + quicksort(right)


def print_products(products):
    """
    Выводит список товаров в удобном формате.

    :param products: Список словарей с информацией о товарах.
    """
    for value in products:
        print(value["name"], "-", value["final_price"], "рублей")


if __name__ == '__main__':
    products_with_price = list(map(
        lambda value: {**value, "final_price": value["price"] * (1 - value["discount"] / 100)}, 
        PRODUCTS
    ))
    sorted_products = quicksort(products_with_price)

    print("Отсортированные по возрастанию товары final_price: ")
    print_products(sorted_products)
