#!/usr/bin/env python3

import random
from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")
"""Обобщенный тип, который позволяет сохранить тип результата funktsiy, obertka возвращает list[T] с тем же T, какой вернула бы сама funktsiya, а не list[Any]."""


def n_raz(n: int) -> Callable[[Callable[..., T]], Callable[..., list[T]]]:
    """Возвращает декоратор, вызывающий декорируемую функцию n раз подряд и собирающий список ее результатов."""

    def dekorator(funktsiya: Callable[..., T]) -> Callable[..., list[T]]:
        """Оборачивает funktsiya так, чтобы каждый ее вызов выполнялся n раз."""

        def obertka(*args: object, **kwargs: object) -> list[T]:
            """Вызывает funktsiya n раз подряд, печатая сообщение перед каждым запуском."""
            rezultaty: list[T] = []
            for nomer in range(1, n + 1):
                print(f"Запуск {nomer} из {n}")
                rezultaty.append(funktsiya(*args, **kwargs))
            return rezultaty

        return obertka

    return dekorator


@n_raz(3)
def sluchainoe_chislo(granitsa: int) -> int:
    """Возвращает случайное целое число от 0 до granitsa включительно."""
    return random.randint(0, granitsa)


if __name__ == "__main__":
    rezultaty = sluchainoe_chislo(10)
    print(rezultaty)
