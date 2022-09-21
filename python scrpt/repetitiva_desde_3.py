'''
repetitiva_desde_3.py
script en Python que muestra una cuenta regresiva
usando un ciclo for y esperando un segundo
entre cada numero.
'''
import os
import time

for numero in range(10, -1, -1):
    os.system('cls')
    print(numero)
    time.sleep(1)
else:
    print('Happy new year')
print('Nos vemos....')