def int_or_not(*args):
    ints = [a for a in args if type(a) is int]
    if not ints:
        return None
    result = 1
    for a in ints:
        result *= a
    return result


if __name__ == "__main__":
    args = ("йоу", 3.5, True, "слово")
    result = int_or_not(*args)
    if result:
        print(f"Произведение целочисленных аргументов= {result}")
    else:
        print(f"целых чисел нет, зато есть:")
        print({a: type(a).__name__ for a in args})
