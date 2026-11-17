
def filtr(**kwargs):
    vowels = set("аеёиоуыэюяaeiou")
    result = {}
    for key, value in kwargs.items():
        if not isinstance(value, str):
            continue
        count_v = 0
        for letter in value.lower():
            if letter in vowels:
                count_v += 1
        if count_v >= 3:
            result[key] = value
    return result

if __name__ == "__main__":
    print(filtr(name="Александра", city="Рязань", age=20, country="Египет"))




