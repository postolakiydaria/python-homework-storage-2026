from functools import reduce

long_words = lambda x: len(x) >= 7
word_length = lambda x: (x, len(x))

if __name__ == '__main__':
    words = []
    while True:
        word = input('Введите слово (или Enter для завершения):\n')
        cleaned = word.strip()

        if not cleaned:
            break

        if ' ' in cleaned:
            print('Пожалуйста, вводите только одно слово без пробелов!')
            continue

        words.append(cleaned)

    words_longer_than_seven = list(filter(long_words, words))
    print(f'Слова с длиной 7 и больше: {words_longer_than_seven}')

    the_remaining_pairs = list(map(word_length, words_longer_than_seven))
    print(f'Оставшиеся слова в паре со своей длиной: {the_remaining_pairs}')

    if the_remaining_pairs:
        find_longest = lambda max_pair, current_pair: (
            current_pair if current_pair[1] > max_pair[1] else max_pair
        )
        longest = reduce(find_longest, the_remaining_pairs)
        print(f'Слово с максимальной длиной: {longest[0]} - {longest[1]} символов')

        sum_lengths = lambda total, current_pair: total + current_pair[1]
        total_length = reduce(sum_lengths, the_remaining_pairs, 0)
        print(f'Суммарное количество букв во всех отфильтрованных словах: {total_length}')
    else:
        print('Нет слов длиной ≥ 7 символов')
