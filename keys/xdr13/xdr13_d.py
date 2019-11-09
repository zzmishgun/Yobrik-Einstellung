from keys.xdr13 import dict

def key_xdr13():
    text = ''
    message = list(input('ENTER the MESSAGE >>  '))
    сharacters = len(message)
    for i in range(сharacters):
        text += dict.dict_main[message[i]]
    print('             ',text,sep='')
