A_SET = {'а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}      #Теперь вне функций
OMG_SET = {'.', ',', '!', '?', ':', ';', '-', '(', ')'}

def input_string():
    text = input('Введите слова(на русском языке): \n' )
    return text

def str_tuple(text):
    words_list = text.split( )
    words_tuple = tuple(words_list)
    return words_tuple

def count_words(words_tuple):
    unique_set = set(words_tuple)
    return len(unique_set)

def count_letters(text):
    a_let = 0
    b_let = 0
    omg = 0

    for symbol in text:
        sym_low = symbol.lower()

        if sym_low in A_SET:
            a_let += 1
        elif sym_low in OMG_SET:          
            omg += 1
        elif sym_low.isalpha():         
            b_let += 1
    return(a_let, b_let, omg)

    print('Кортеж слов: ', words_tuple)
    print('Количество уникальных слов: ', unique_set)
    print('Гласные: ', a_set)
    print('Согласные: ', b_set)
    print('Знаки препинания: ', omg)

if __name__ == "__main__":            #Все принты теперь в главном теле
    
    print('Кортеж слов: ', words_tuple)
    print('Количество уникальных слов: ', unique_set)
    print('Гласные: ', a_set)
    print('Согласные: ', b_set)
    print('Знаки препинания: ', omg)

    text = input_string()
    words_tuple = str_tuple(text)
    unique_count = count_words(words_tuple)
    (a_let, b_let, omg) = count_letters(text)
    res(words_tuple, unique_count, a_let, b_let, omg)

