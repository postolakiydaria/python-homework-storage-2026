#!/usr/bin/env python3

import random
from collections.abc import Callable

delitsya_na_3_ne_na_9: Callable[[int], bool] = lambda chislo: (
    chislo % 3 == 0 and chislo % 9 != 0
)
bolshe_20_po_modulyu: Callable[[int], bool] = lambda chislo: abs(chislo) > 20

if __name__ == "__main__":
    chisla: list[int] = [random.randint(-100, 100) for _ in range(20)]
    print(f"Исходные числа: {chisla}")

    delyashchiesya: list[int] = list(filter(delitsya_na_3_ne_na_9, chisla))
    po_modulyu: list[int] = list(filter(bolshe_20_po_modulyu, chisla))
    oba_usloviya: list[int] = list(
        filter(
            lambda chislo: (
                delitsya_na_3_ne_na_9(chislo) and bolshe_20_po_modulyu(chislo)
            ),
            chisla,
        )
    )

    print(f"Делятся на 3, но не на 9: {delyashchiesya}, длина {len(delyashchiesya)}")
    print(f"Больше 20 по модулю: {po_modulyu}, длина {len(po_modulyu)}")
    print(f"Удовлетворяют обоим условиям: {oba_usloviya}, длина {len(oba_usloviya)}")
