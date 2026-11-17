ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"   #Исправлено

def alphabet():
    
    char_to_num = {}
    num_to_char = {}

    for i in range(len(ALPHABET)+1):
        letter = ALPHABET[i-1]
        char_to_num[letter] = i + 1
        num_to_char[i + 1] = letter

    char_to_num[" "] = 0
    num_to_char[0] = " "

    return(char_to_num, num_to_char)

def get_user():
    print("1 - Зашифровать текст в числа")
    print("2 - Расшифровать числа из текста")
    print("3 - Выйти из программы")
    choice = input("Ваш выбор: ")

    while choice not in ("1", "2", "3"):
        print("Введите 1, 2 или 3")
        choice = input("Ваш выбор: ")
    return choice

def  get_input(choice):
    if choice == "1":
        return input("Введите текст: ")
    else:
        return (input("Введите числа через пробел(от 0 до 33): "))

def encrypt(text, char_to_num):
    result = []
    text_upper = text.upper()

    invalid_symbols = []
    for symbol in text_upper:
        if symbol not in char_to_num:
            invalid_symbols.append(symbol)
    
    if invalid_symbols:
        print(f" Ошибка: в тексте есть недопустимые символы: {set(invalid_symbols)}")
        print("Текст должен содержать только русские буквы и пробелы!")
        return                                                               #None больше нет

    for symbol in text_upper:
        if symbol in char_to_num:
            result.append(str(char_to_num[symbol]))
        else:
            print(f"Символ '{symbol}' не найден в алфавите, пропускаем")
    return " ".join(result)

def decrypt(numbers_str, num_to_char):
    result = []
    numbers_list = numbers_str.split(" ")

    for num_str in numbers_list:
        try:
            num = int(num_str)
            if num in num_to_char:
                result.append(num_to_char[num])
            else:
                print(f"Число {num} не найдено в алфавите")
        except ValueError:
            print(f"'{num_str}' не является числом")
    if not result:
        return

    return "".join(result)

def print_result(choice, result):
    if result is None:
        print("Операция не выполнена из-за ошибок ввода")
    if choice == "1":
        print(f"Зашифрованный текст: {result}")
    else:
        print(f"Расшифрованный текст: {result}")


if __name__ == "__main__":
    char_to_num, num_to_char = alphabet()
    
    while True:
        choice = get_user()
        
        if choice == "3":
            print("До свидания!")
            break
        
        data = get_input(choice)
        
        if choice == "1":
            result = encrypt(data, char_to_num)
        else:
            result = decrypt(data, num_to_char)
            
        print_result(choice, result)
        
