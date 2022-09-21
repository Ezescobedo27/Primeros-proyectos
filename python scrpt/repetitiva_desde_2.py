'''
repetitiva_desde_2.py
script en python que imprima los numeros pares 
desde el 2 hasta el 20 haciendo un ciclo for
'''

print('Programa que muestra los numeros pares desde el 2 hasta el 20')

print('Metodo 1')

for numero in range(1, 11):
    print(f'par: {numero*2}')
print('/'*20)

print('Metodo 2')
for numeros in range(2, 21):
    if numeros % 2 == 0:
        print(f'par: {numeros}')

print('*'*20)
print('Metodo 3')
for par in range(2, 21, 2):
    print(f'par: {par}')

