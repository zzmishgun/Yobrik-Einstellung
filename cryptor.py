from keys import xdr13_c
from keys import xdr13_d
from tkinter import *
import tkinter.scrolledtext as tkst
import socket
import threading


status = input('CRYPT(c) or DECRYPT(d) >>  ')


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

status = input('CRYPT(c) or DECRYPT(d) >>  ')



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



