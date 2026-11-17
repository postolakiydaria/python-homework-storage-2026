#!/usr/bin/env python3

def user_input(text: str) -> list[str]:
    znach = input(text).replace(",", ".").split()
    return znach

def proverka_c() -> list[tuple[float, str]] | None:
    
    while True:
        u_input = user_input("Введите последовательность чисел через пробел (или Enter для выхода):\n")
        
        if not u_input: 
            return None
        result: list[tuple[float, str]] = []
        
        for part in u_input:
            try:
                result.append((float(part), part))
            except ValueError:
                print(f"Ошибка: '{part}' не является числом. Попробуйте снова.\n")
                break
        else:
            return result


def quick_sort(arr: list[tuple[float, str]]) -> list[tuple[float, str]]:
    
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  
    
    left = [x for x in arr if x[0] < pivot[0]]      
    mid = [x for x in arr if x[0] == pivot[0]]    
    right = [x for x in arr if x[0] > pivot[0]]      
    
    return quick_sort(left) + mid + quick_sort(right)


if __name__ == "__main__":
    
    data = proverka_c()
    if data is None:
        print("Ввод отменен. Завершение работы.")
    else:
        sort_tuples = quick_sort(data)

        while True:
            
            who_input = user_input(
                "Выберите порядок сортировки:\n"
                "1 - от меньшего к большему\n"
                "2 - от большего к меньшему\n"
                "Ваш выбор: "
            )
           
            if len(who_input) != 1 or who_input[0] not in ("1", "2"):
                    print("Нужно ввести ровно одно число: 1 или 2.\n")
                    continue
            break
        order = int(who_input[0])
            
        items = sort_tuples if order == 1 else reversed(sort_tuples)
        output = " ".join(x[1] for x in items)
        
        print(f"Результат: {output}")
