#!/usr/bin/env python3
SLOVAR_BUKV: dict = { 'б':'54','в':'38','г':'52','д':'94','е':'9', 'ё':'11','ж':'71','з':'48','и':'2','й':'95','к':'63','л':'75',
'м':'74','н':'64','о':'93','п':'18','р':'59','с':'72','т':'8','у':'3','ф':'88','х':'96','ц':'30','ч':'50','ш':'19','щ':'83',
'ъ':'86','ы':'57','ь':'45','э':'44','ю':'89','я':'77','а':'0'}
SLOVAR_CIRF = {
    '0': 'а', '54': 'б', '38': 'в', '52': 'г', '94': 'д', '9': 'е', '11': 'ё',
    '71': 'ж', '48': 'з', '2': 'и', '95': 'й', '63': 'к', '75': 'л', '74': 'м',
    '64': 'н', '93': 'о', '18': 'п', '59': 'р', '72': 'с', '8': 'т', '3': 'у',
    '88': 'ф', '96': 'х', '30': 'ц', '50': 'ч', '19': 'ш', '83': 'щ', '86': 'ъ',
    '57': 'ы', '45': 'ь', '44': 'э', '89': 'ю', '77': 'я'
}



if __name__ == '__main__':
    text: str = input('Введите любой текст на русском языке\n').lower()
    result_text = []

    for char in text:
        if char in SLOVAR_BUKV:
            result_text.append(SLOVAR_BUKV[char])
        elif char == ' ':
            result_text.append('/')
        else:
            result_text.append(char)

    print(' '.join(result_text))

    cifra: str = input('Введите зашифрованный текст (числа через пробел, слова через /)\n')
    result_cifra = []
    for chaar in cifra.split():
        if chaar in SLOVAR_CIRF:
            result_cifra.append(SLOVAR_CIRF[chaar])
        elif chaar == '/':
            result_cifra.append(' ')
        else:result_cifra.append(chaar)
    print(' '.join(result_cifra))
