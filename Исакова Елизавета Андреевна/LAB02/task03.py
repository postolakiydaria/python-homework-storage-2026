def multiplication(*args):
    result = 1
    for x in args:
        result *= x
    return result

if __name__ == "__main__":
    data_lst = []
    
    while True:
        data = input('Введите любые значения через запятую:\n')

        if not data:
            print('Вы ничего не ввели!')
            continue

        if ',' not in data:
            print('Значения должны быть разделены запятыми!')
            continue

        data_lst = data.split(',')
        valid = True
        for x in data_lst:
            strip_x = x.strip()
            if not strip_x:
                valid = False
                print('Не пишите лишние запятые!')
                break
            if ' ' in strip_x:
                valid = False
                print(f'"{strip_x}" — это не одно значение, разделяйте запятыми!')
                break

        if not valid:
            continue

        break

    arguments = []
    for y in data_lst:
        y = y.strip()
        try:
            value = int(y)
        except ValueError:
            try:
                value = float(y)
            except ValueError:
                value = y
        arguments.append(value)

    print(multiplication(*arguments))
    
