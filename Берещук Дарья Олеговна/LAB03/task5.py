REPEAT_TIMES = 9

def repeat(n):
    def deco(func):
        def wrapper():
            results = []
            for i in range(1, n + 1):
                print(f"Вызов №{i} из {n}")
                results.append(func())
            return results

        return wrapper

    return deco


@repeat(REPEAT_TIMES)
def hi():
    return "Привет"

if __name__ == "__main__":
    print(f"Вызываю hi, декоратор repeat запустит её {REPEAT_TIMES} раз:\n")
    result = hi()
    print(f"hi вернула список из {len(result)} результатов:")
    print(result)