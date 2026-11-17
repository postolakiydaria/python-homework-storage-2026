def find_hypo(a, b):
    return (a**2 + b**2) ** 0.5

def find_kat(hypo, kat):
    if hypo <= kat:
        return "Гипотенуза должна быть больше катета!"
    return (hypo**2 - kat**2) ** 0.5
    
def get_two_sides():                   #вместо двух одинаковых функций с выводом -> одна общая
    while True:
        try:
            side1 = float(input("Введите первую сторону: "))
            side2 = float(input("Введите вторую сторону: "))
            return side1, side2
        except ValueError:
            print("Ошибка: введите число! Попробуйте снова.\n")

if __name__ == "__main__":
    while True:
        print("\n=== Прямоугольный треугольник ===")
        print("1 - Найти гипотенузу по двум катетам")
        print("2 - Найти катет по гипотенузе и другому катету")
        print("0 - Выйти")

        choice = input("Выберите режим (1, 2 или 0): ")

        if choice == '0':
            print("Программа завершена.")
            break
        elif choice == '1':                         #одна фцнкция 
            side1, side2 = get_two_sides()
            result = find_hypo(side1, side2)
            print(f"Гипотенуза = {result}")

        elif choice == '2':
            side1, side2 = get_two_sides()
            hyp = max(side1, side2)
            leg = min(side1, side2)
            result = find_kat(hyp, leg)
            print(f"Второй катет = {result}")

     
        else:
            print("Неверный выбор! Попробуйте снова.")
            continue

        while True:
            again = input("\nПродолжить? (да/нет): ").lower()
            if again in ('да', 'нет'):
                break
            print("Ошибка: введите 'да' или 'нет'!")

        if again == 'нет':
            print("Программа завершена.")
            break
    
