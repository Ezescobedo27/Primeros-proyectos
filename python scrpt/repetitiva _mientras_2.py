
'''
script en Python que sume valores pares y multiplique valores
impares mientras el usuario no ingrese un 0. Se debera utilizar
la estructura repetitiva "Mientras" para solicitar al usuario 
un  numero dependiendo del numero lo suma o lo multiplica'''



print('Programa que suma los numeros pares y multiplica los impares')
suma = 0
multiplicacion = 1
numero = -1

while numero != 0:
    numero = int(input('Ingresa un numero(0 para salir)'))
    if numero % 2 == 0:
        suma = suma + numero
    else:
        multiplicacion = multiplicacion * numero
    
    print(f'suma: {suma}')
    print(f'multiplicacion: {multiplicacion}')

print('Nos vemos ')