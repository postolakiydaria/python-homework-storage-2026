ALL_VOWELS = ("a", "e", "i", "o", "u", "y",
              "а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я")

def many_vowels(**kwargs):
    vowel = 0
    new_dict = {}
    for key, value in kwargs.items():
        for symbol in value:
            if symbol.lower() in ALL_VOWELS:
                vowel += 1
        if vowel >= 3:
            new_dict[key] = value
            vowel = 0
    print(new_dict)


if __name__ == '__main__':
    input_dict = {"cat":"meow meow", "do": "many tasks", "hide": "ok"}
    many_vowels(**input_dict)
