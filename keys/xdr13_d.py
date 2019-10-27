def key_xdr13():
    text = ''
    message = list(input('ENTER the MESSAGE >>  '))
    сharacters = len(message)
    dictionary = {
        '∑' : 'a',
        '‰' : 'b',
        '○' : 'c',
        '∰' : 'd',
        '—' : 'e',
        '≣' : 'f',
        '¤' : 'g',
        '⟰' : 'h',
        '⤗' : 'i',
        'Σ' : 'j',
        '✥' : 'k',
        '⊌' : 'l',
        '∨' : 'm',
        '⋏' : 'n',
        '∄' : 'o',
        '⋋' : 'p',
        '⊣' : 'q',
        '∎' : 'r',
        '∺' : 's',
        'ⅵ' : 't',
        '∵' : 'u',
        '✖' : 'v',
        '⋻' : 'w',
        '⋵' : 'x',
        'Ⅳ' : 'y',
        '☭' : 'z',
        '↫' : '1',
        '卐' : '2',
        '♝' : '3',
        '♬' : '4',
        '☪' : '5',
        '۞' : '6',
        '♲' : '7',
        '⇔' : '8',
        'ت' : '9',
        '*' : '0',
        '∬' : ' ',
    }
    for i in range(сharacters):
        text += dictionary[message[i]]
    print('             ',text,sep='')
