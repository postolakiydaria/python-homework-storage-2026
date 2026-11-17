STANDARD_DELIMITER = " "

if __name__ == "__main__":
    raw = input(f"Введите целые числа через {STANDARD_DELIMITER}: \n").split(STANDARD_DELIMITER)
    numbers = []
    for rw in raw:
        try:
            numbers.append(int(rw))
        except ValueError:
            print(f"{rw} - Не целое число")
            continue
    print("оставляю только целые числа")
    classify = lambda n: "zero" if n==0 else ("negative" if n<0 else ("positive even" if n%2==0 else "positive odd"))
    print("классификация на одну из 4 групп")
    for n in numbers:
        print(f"{n} - {classify(n)}")
