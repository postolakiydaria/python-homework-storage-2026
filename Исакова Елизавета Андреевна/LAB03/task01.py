PUNCTUATION = '.,!?;:()—«»"\'*/\\[]{}@#$%^&_+=<>|'

definition_of_numbers = lambda num: (
    "positive even" if num > 0 and num % 2 == 0 else
    "positive odd" if num > 0 else
    "negative" if num < 0 else
    "zero"
)

if __name__ == '__main__':
    while True:
        arguments = []
        data = input('Введите последовательность чисел:\n')

        if not data.strip():
            print('Вы ничего не ввели, попробуйте еще раз!')
            continue

        cleaned = None

        try:
            for x in data.split():
                cleaned = x.strip(PUNCTUATION)
                if cleaned:
                    number = int(cleaned)
                    arguments.append(number)
        except ValueError:
            print(f'{cleaned} не является целым числом, попробуйте еще раз!')
            continue

        if arguments:
            print(f'Список ваших целых чисел: {arguments}')
            break
        else:
            print('Вы не ввели ни одного числа, попробуйте еще раз!')

    for number in arguments:
        print(f'{number} — {definition_of_numbers(number)}')
        
