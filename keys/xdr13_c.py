def key_xdr13():
    text = ''
    message = list(input('ENTER the MESSAGE >>  '))
    сharacters = len(message)
    dictionary = {
        'a' : '∑',
        'b' : '‰',
        'c' : '○',
        'd' : '∰',
        'e' : '—',
        'f' : '≣',
        'g' : '¤',
        'h' : '⟰',
        'i' : '⤗',
        'j' : 'Σ',
        'k' : '✥',
        'l' : '⊌',
        'm' : '∨',
        'n' : '⋏',
        'o' : '∄',
        'p' : '⋋',
        'q' : '⊣',
        'r' : '∎',
        's' : '∺',
        't' : 'ⅵ',
        'u' : '∵',
        'v' : '✖',
        'w' : '⋻',
        'x' : '⋵',
        'y' : 'Ⅳ',
        'z' : '☭',
        '1' : '↫',
        '2' : '卐',
        '3' : '♝',
        '4' : '♬',
        '5' : '☪',
        '6' : '۞',
        '7' : '♲',
        '8' : '⇔',
        '9' : 'ت',
        '0' : '*',
        ' ' : '∬',
    }
    for i in range(сharacters):
        text += dictionary[message[i]]
    print('             ',text,sep='')
