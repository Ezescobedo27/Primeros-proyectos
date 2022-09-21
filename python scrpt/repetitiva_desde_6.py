'''
repetitiva_desde_6.py
script en Python que muestre uno a uno los simbolos de una 
palabra o frase. Por ejemplo si la frasw fuera "Hola" se 
deberia imprimir:
H
o
l
a
'''

frase = input('Ingresa una frase o palabra:')
print('Los simbolos de tu frase/palabra son: ')

for simbolo in frase:
    print(f'{simbolo}')

print('Nos vemos....')