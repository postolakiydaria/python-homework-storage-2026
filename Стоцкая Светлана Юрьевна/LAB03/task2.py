PRODUCTS = [
{"name": "Laptop", "price": 89990, "discount": 10},
{"name": "Mouse", "price": 2490, "discount": 15},
{"name": "Keyboard", "price": 5490, "discount": 0},
{"name": "Monitor", "price": 27990, "discount": 25}]

def adding_price(products_list):
    '''
    Эта функция рассчитывает для каждого товара из списка финальную цену (с учётом скидок).
    :param products_list: Список словарей с информацией о товарах.
    :return: None: Ничего не возвращает, выводит на экран итоговый отсортированный список товаров.
    '''
    final_list = products_list
    add = lambda x: {"final_price": x["price"] * (100 - x["discount"])/100}
    new_list = list(map(add, products_list))
    numb = len(products_list)
    for item in range(numb):
        final_list[item].update(new_list[item])
    final_list.sort(key=lambda x: x["final_price"])
    print(f"Итоговый список товаров {final_list}")

def get_price_from_user():
    dicts_list = []
    while True:
        name = input("Введите наименование товара ")
        if name == "":
            break
        try:
            price = float(input("Введите стоимость товара "))
            discount = float(input("Введите скидку на товар "))
        except ValueError:
            print("Вы ввели вместо цены или скидки не число!")
            return None
        dicts_list.append({"name": name, "price": price, "discount": discount})
    return dicts_list

if __name__ == '__main__':
    adding_price(PRODUCTS)
    lst = get_price_from_user()
    if lst:
        adding_price(lst)
