from keys.xdr13 import xdr13_c, xdr13_d

status = input('CRYPT(c) or DECRYPT(d) or INSTRUCTIONS(i) >>  '
               "IF YOU WAN'T CREATE YOR PERSONAL CRYPTO-ALGORITHM CONTACT US OR ENTER(pa) >>  ")


KEY = input('ENTER the KEY >>  ')

keys = ['xdr13']

if status == 'c':
    if KEY in keys[:] and KEY == 'xdr13':
        xdr13_c.key_xdr13()
    else: print('/error')
elif status == 'd':
    if KEY in keys[:] and KEY == 'xdr13':
        xdr13_d.key_xdr13()
    else: print('/error')
elif status == 'i':
    print('1.ENTER THE LETTER(COMPLETED)'
          "2.ENTER YOUR KEY.IF YOU DON'T HAVE A KEY CONTACT US."
          '3.ENTER YOUR MESSAGE.'
          '4.COPY THE RESULT.')
else:
    print("ENTER 'c' or 'd' or 'i' or 'pa' >>  ")


