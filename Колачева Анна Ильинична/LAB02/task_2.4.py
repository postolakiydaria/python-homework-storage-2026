#!/usr/bin/env python3

COUNT_VOWELS = 3
VOWELS = 'aeiouаеёиоуыэюя'

def user_input(text: str) -> str:
    znach: str = input(text).strip()
    return znach

def filter_v(**kwargs: str) -> dict[str, str]:
    res: dict[str, str] = {}

    for key, znach in kwargs.items():
        lower_znach: str = znach.lower()
        count: int = sum(1 for x in lower_znach if x in VOWELS)
        
        if count >= COUNT_VOWELS:
            res[key] = znach
                
    return res


if __name__ == "__main__":
    
    user_kwargs: dict[str, str] = {}
    
    print("Вводите аргументы по очереди.")
    print("Для завершения введите пустую строку вместо имени аргумента.\n")
    
    while True:

        key: str = user_input("Имя аргумента (или Enter для завершения): \n")
        
        if not key:
            break
            
        znach: str = user_input(f"Значение для '{key}': ")
        user_kwargs[key] = znach
    
    if user_kwargs:
        res: dict[str, str] = filter_v(**user_kwargs)
        print("\nРезультат:", res)
    else:
        print("\nВы не ввели ни одного аргумента.")
