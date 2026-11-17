#!/usr/bin/env python3

from collections.abc import Callable
from typing import Any, Final

products: Final[list[dict[str, Any]]] = [
    {"name": "Laptop", "price": 89990, "discount": 10},
    {"name": "Mouse", "price": 2490, "discount": 15},
    {"name": "Keyboard", "price": 5490, "discount": 0},
    {"name": "Monitor", "price": 27990, "discount": 25},
]

dobavit_final_price: Callable[[dict[str, Any]], dict[str, Any]] = (
    lambda ishodnyi_tovar: {
        **ishodnyi_tovar,
        "final_price": ishodnyi_tovar["price"] * (1 - ishodnyi_tovar["discount"] / 100),
    }
)


def togda_budet_quicksort_ruchkami(
    elementy: list[dict[str, Any]], kluch: Callable[[dict[str, Any]], float]
) -> list[dict[str, Any]]:
    """Сортирует elementy по значению kluch(element) собственной реализацией быстрой сортировки."""
    if len(elementy) <= 1:
        return list(elementy)

    opornyi_kluch = kluch(elementy[len(elementy) // 2])
    menshe: list[dict[str, Any]] = [el for el in elementy if kluch(el) < opornyi_kluch]
    ravno: list[dict[str, Any]] = [el for el in elementy if kluch(el) == opornyi_kluch]
    bolshe: list[dict[str, Any]] = [el for el in elementy if kluch(el) > opornyi_kluch]

    return (
        togda_budet_quicksort_ruchkami(menshe, kluch)
        + ravno
        + togda_budet_quicksort_ruchkami(bolshe, kluch)
    )


if __name__ == "__main__":
    tovary_s_tsenoy: list[dict[str, Any]] = togda_budet_quicksort_ruchkami(
        list(map(dobavit_final_price, products)),
        kluch=lambda odin_tovar: odin_tovar["final_price"],
    )
    print(f"Обработано товаров: {len(tovary_s_tsenoy)}")

    for tovar in tovary_s_tsenoy:
        print(tovar)
