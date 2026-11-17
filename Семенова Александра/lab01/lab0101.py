def user_list(numbers):
    sorted_nums = sorted(numbers)
    for i in range(len(sorted_nums) - 1):
        if sorted_nums[i] == sorted_nums[i + 1]:
            return False
    return True

def list_of_numbers():
    while True:
        try:
            user = input('Введите ваши числа через пробел: ')
            numbers = [float(x) for x in user.split()]
            if not numbers:
                print('Вы ничего не ввели. Попробуйте снова.\n')
            return numbers
        except ValueError:
            print('Ну нет, добавьте ЧИСЛА\n')

if __name__ == "__main__":
    numbers = list_of_numbers()
    
    if user_list(numbers):
        print("\nВсе числа различны!")
    else:
        print("\nЕсть повторяющиеся числа!")

