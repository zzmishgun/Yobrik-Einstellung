import random
dictionary_of_symbols = ["A", "B", "C", "D", 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X' ,'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', " ",'Я', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч','ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я' ] #Скинь мне словарь или корректно задай сам.
value = [] #Не изменять
def new_dict_create():
    i = 1
    while i < 121:
        x = random.randint(1,121)
        if not x in value:
                value.append(x)
        else: i += 1
new_dict_create()
dict_main = {
        'a' : dictionary_of_symbols[value[0]],
        'b' : dictionary_of_symbols[value[1]],
        'c' : dictionary_of_symbols[value[2]],
        'd' : dictionary_of_symbols[value[3]],
        'e' : dictionary_of_symbols[value[4]],
        'f' : dictionary_of_symbols[value[5]],
        'g' : dictionary_of_symbols[value[6]],
        'h' : dictionary_of_symbols[value[7]],
        'i' : dictionary_of_symbols[value[8]],
        'j' : dictionary_of_symbols[value[9]],
        'k' : dictionary_of_symbols[value[10]],
        'l' : dictionary_of_symbols[value[11]],
        'm' : dictionary_of_symbols[value[12]],
        'n' : dictionary_of_symbols[value[13]],
        'o' : dictionary_of_symbols[value[14]],
        'p' : dictionary_of_symbols[value[15]],
        'q' : dictionary_of_symbols[value[16]],
        'r' : dictionary_of_symbols[value[17]],
        's' : dictionary_of_symbols[value[18]],
        't' : dictionary_of_symbols[value[19]],
        'u' : dictionary_of_symbols[value[20]],
        'v' : dictionary_of_symbols[value[21]],
        'w' : dictionary_of_symbols[value[22]],
        'x' : dictionary_of_symbols[value[23]],
        'y' : dictionary_of_symbols[value[24]],
        'z' : dictionary_of_symbols[value[25]],
        '1' : dictionary_of_symbols[value[26]],
        '2' : dictionary_of_symbols[value[27]],
        '3' : dictionary_of_symbols[value[28]],
        '4' : dictionary_of_symbols[value[29]],
        '5' : dictionary_of_symbols[value[30]],
        '6' : dictionary_of_symbols[value[31]],
        '7' : dictionary_of_symbols[value[32]],
        '8' : dictionary_of_symbols[value[33]],
        '9' : dictionary_of_symbols[value[34]],
        '0' : dictionary_of_symbols[value[35]],
        ' ' : dictionary_of_symbols[value[36]],
        'A' : dictionary_of_symbols[value[37]],
        'B' : dictionary_of_symbols[value[38]],
        'C' : dictionary_of_symbols[value[39]],
        'D' : dictionary_of_symbols[value[40]],
        'E' : dictionary_of_symbols[value[41]],
        'F' : dictionary_of_symbols[value[42]],
        'G' : dictionary_of_symbols[value[43]],
        'H' : dictionary_of_symbols[value[44]],
        'I' : dictionary_of_symbols[value[45]],
        'J' : dictionary_of_symbols[value[46]],
        'K' : dictionary_of_symbols[value[47]],
        'L' : dictionary_of_symbols[value[48]],
        'M' : dictionary_of_symbols[value[49]],
        'N' : dictionary_of_symbols[value[50]],
        'O' : dictionary_of_symbols[value[51]],
        'P' : dictionary_of_symbols[value[52]],
        'Q' : dictionary_of_symbols[value[53]],
        'R' : dictionary_of_symbols[value[54]],
        'S' : dictionary_of_symbols[value[55]],
        'T' : dictionary_of_symbols[value[56]],
        'U' : dictionary_of_symbols[value[57]],
        'V' : dictionary_of_symbols[value[58]],
        'W' : dictionary_of_symbols[value[59]],
        'X' : dictionary_of_symbols[value[60]],
        'Y' : dictionary_of_symbols[value[61]],
        'Z' : dictionary_of_symbols[value[62]]
}