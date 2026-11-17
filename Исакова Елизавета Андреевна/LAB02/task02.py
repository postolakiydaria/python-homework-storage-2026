DELIMITER = ' '

def increase(data):
    inc_sort = sorted(data)
    return tuple(inc_sort)

def decrease(data):
    dec_sort = sorted(data, reverse=True)
    return tuple(dec_sort)

if __name__ == "__main__":
    numbers_lst = []
    while True:
        numbers = input(f'Введите последовательность чисел для сортировки через {DELIMITER}:\n')

        if not numbers.strip():
            print('Вы ничего не ввели! Попробуйте еще раз')
            continue

        numbers = numbers.split(DELIMITER)
        numbers = [num for num in numbers if num]

        valid = True
        for number in numbers:
            try:
                float(number)
            except ValueError:
                valid = False
                print(f'{number} - это не число! Попробуйте еще раз')
                break

        if not valid:
            continue

        numbers_lst = [float(number) for number in numbers]
        break

    while True:
        incr_or_decr = input('Если вы хотите отсортировать по возрастанию, введите: +\n'
                             'Если вы хотите отсортировать по убыванию, введите: -\n')

        if not incr_or_decr:
            print('Вы ничего не ввели! Попробуйте еще раз')
            continue

        if incr_or_decr == '+':
            print(f'Ваша последовательность отсортирована по возрастанию: {increase(numbers_lst)}')
            break
        elif incr_or_decr == '-':
            print(f'Ваша последовательность отсортирована по убыванию: {decrease(numbers_lst)}')
            break
        else:
            print('Попробуйте еще раз, нужно ввести + или - !')
            continue
            
