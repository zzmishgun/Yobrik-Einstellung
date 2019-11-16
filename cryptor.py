import os
from keys.xdr13 import xdr13

status = input('CRYPT(c) or DECRYPT(d) or INSTRUCTIONS(i)\n '
               "IF YOU WAN'T CREATE YOR PERSONAL CRYPTO-ALGORITHM CONTACT US OR ENTER(pa) >>  ")
KEY = input('ENTER the KEY >>  ')

keys = ['xdr13']

if status == 'c':
    if KEY in keys[:] and KEY == 'xdr13':
        xdr13.xdr13_c()
    else: print('/error')
elif status == 'd':
    if KEY in keys[:] and KEY == 'xdr13':
        xdr13.xdr13_d()
    else: print('/error')
elif status == 'i':
    print('1.ENTER THE LETTER(COMPLETED)'
          "2.ENTER YOUR KEY.IF YOU DON'T HAVE A KEY CONTACT US."
          '3.ENTER YOUR MESSAGE.'
          '4.COPY THE RESULT.')
if status == 'pa':
    name = input('ENTER NAME >>  ')
    path = 'C:\\Users\\Mon PC\\PycharmProjects\\SecureCrypt\\keys\\' + name
    os.makedirs(path)  # Изменить путь при загрузке на сервер.
    open(path + '\\' + name + '_c.py', 'tw', encoding='utf-8')
    open(path + '\\' + name + '_d.py', 'tw', encoding='utf-8')
    open(path + '\\' + 'dict.py', 'tw', encoding='utf-8')
