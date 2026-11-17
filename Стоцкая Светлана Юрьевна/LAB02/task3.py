def multiply(*args):
    result = 1
    for value in args:
        try:
            result *= int(value)
        except ValueError:
            print(value, type(value))
    print(result)

if __name__ == '__main__':
    numbers = [1, 23, "right"]
    multiply(*numbers)
