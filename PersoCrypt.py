import os, keys
#if cryptor.status == 'pa':
name = input('ENTER NAME >>  ')
os.makedirs('C:\\Users\\Mon PC\\PycharmProjects\\SecureCrypt\\keys\\'+name)#Изменить путь при загрузке на сервер.
open(name+'_c.py',encoding='utf-8')#Прописать путь для создания py-файла
open(name+'_d.py',encoding='utf-8')#Аналогично
open('dict.py',encoding='utf-8')#Аналогично
