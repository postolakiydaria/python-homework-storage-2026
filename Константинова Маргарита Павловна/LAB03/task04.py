#!/usr/bin/env python3

from collections.abc import Callable
from functools import reduce

MINIMALNAYA_DLINA_SLOVA: int = 7

dlinnoe_slovo: Callable[[str], bool] = lambda slovo: (
    len(slovo) >= MINIMALNAYA_DLINA_SLOVA
)
slovo_i_dlina: Callable[[str], tuple[str, int]] = lambda slovo: (slovo, len(slovo))
vybrat_dlinneishee: Callable[[tuple[str, int], tuple[str, int]], tuple[str, int]] = (
    lambda luchshaya, sleduyushchaya: (
        luchshaya if luchshaya[1] >= sleduyushchaya[1] else sleduyushchaya
    )
)
pribavit_dlinu_slova: Callable[[int, str], int] = lambda summa, slovo: (
    summa + len(slovo)
)

if __name__ == "__main__":
    vvod: str = input("Введите слова через пробел: ")
    slova: list[str] = vvod.split()
    print(f"Введено слов: {len(slova)}")

    otfiltrovannye: list[str] = list(filter(dlinnoe_slovo, slova))
    pary: list[tuple[str, int]] = list(map(slovo_i_dlina, otfiltrovannye))
    samoe_dlinnoe: tuple[str, int] = (
        reduce(vybrat_dlinneishee, pary) if pary else ("", 0)
    )
    summa_bukv: int = reduce(pribavit_dlinu_slova, otfiltrovannye, 0)

    print(f"Слова длиной не менее {MINIMALNAYA_DLINA_SLOVA}: {otfiltrovannye}")
    print(f"Пары слово, длина: {pary}")
    print(f"Самое длинное слово: {samoe_dlinnoe}")
    print(f"Суммарное количество букв: {summa_bukv}")
