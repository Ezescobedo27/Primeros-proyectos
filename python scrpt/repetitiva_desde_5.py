'''
repetitiva_desde_5.py
script en Python que muestre las tablas de multiplicar de los
numeros del 1 al 10. Cada tabla se muestra hasta el decimo multiplo.
'''
import os

for  numero in range(1, 11):
    os.system('cls')
    print(f'                                   Tabla de multiplicar de; {numero}')
    for multiplo in range(1, 11):
        print(f'{numero} * {multiplo} = {numero * multiplo}')
    input('Presiona enter para continuar')
print('Nos vemos')