#!/usr/bin/env python3

def get_valid_number() -> int | None:

    while True:
            U_I: str = input("Введите целое число, факториал которого вы хотите найти (или Enter для выхода):\n")

            if not U_I:
               return None
    
            try:
                number = int(U_I)
                
                if number >= 0:
                    break  
                else:
                    print("Число должно быть неотрицательным. Попробуем ещё раз.\n")
                    
            except ValueError:
                has_let: bool = any(char.isalpha() for char in U_I)
                
                if has_let:
                    print("Вы ввели буквы. Написано же, только ЦИФРЫ.\n")
                else:
                    print("Это не целое число. Попробуем ещё раз.\n")
    return number

def recurs_factor(num) -> int:
    if num == 0 or num == 1:
        return 1
    return num * recurs_factor(num - 1)

def iterativ_factor(num) -> int:
    res = 1
    for x in range(1, (num+1)):
        res *= x
    return res

if __name__ == "__main__":
    number = get_valid_number()
    print(f'А вот и результат\n от рекурсивной функции :{recurs_factor(number)}\n  от итеративной: {iterativ_factor(number)} ') 
