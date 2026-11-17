
def factorial_rec(n):
    if n <=1:
        return 1
    return n*factorial_rec(n-1)

def factorial_iter(n):
    if n <= 1:
        return 1
    result = 1
    for i in range(1, n+1):
       result *= i
    return result

if __name__ == "__main__":
    while True:
        try:
            num = input("Введите число, факторил которого надо найти\n")
            true_num=int(num)
        except ValueError:
            print("это не число")
            continue
        break

    scenario = input("Введите 'р' если рекурсивно, 'и' если итеративно\n")
    if scenario.lower() == "р":
        print(f"Факториал числа {num} равен {factorial_rec(true_num)}")
    elif scenario.lower() == "и":
        print(f"Факториал числа {num} равен {factorial_iter(true_num)}")
    else:
        print("Режим не распознан. Используйте 'р' или 'и'.")

