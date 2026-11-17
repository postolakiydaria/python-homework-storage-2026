#!/usr/bin/env python3
GLASNYE_BUKVY = "аеёиоуыэюя"
POROG = 3


def otobrat_stroki(**kwargs):
    itog = {}
    for imya, znachenie in kwargs.items():
        if type(znachenie) is str:
            glasnyh = 0
            for s in znachenie.lower():
                if s in GLASNYE_BUKVY:
                    glasnyh = glasnyh + 1
            if glasnyh >= POROG:
                itog[imya] = znachenie
    return itog


if __name__ == "__main__":
    rezultat = otobrat_stroki(city="Санкт-Петербург", animal="носорог", )
    print(rezultat)
