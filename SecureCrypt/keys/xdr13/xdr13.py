from keys.xdr13 import dict
def xdr13_c():
    text = ''
    message = list(input('ENTER the MESSAGE >>  '))
    сharacters = len(message)
    for i in range(сharacters):
        text += dict.dictionary[message[i]]
    print('             ', text, sep='')
def xdr13_d():
    text = ''
    message = list(input('ENTER the MESSAGE >>  '))
    сharacters = len(message)
    for i in range(сharacters):
        text += dict.dictionary_reverso[message[i]]
    print('             ', text, sep='')
