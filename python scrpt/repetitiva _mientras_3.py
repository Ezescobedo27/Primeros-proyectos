# '''
# repetitivaa_mientras_3.py
# script en Python que simule el sistema de validacion de datos en una plataforma digital
# Se le solicitara al usuario su nombre y contrasena mientras la informacion
# proporcionada no coincida con la informacion previamente registrada
# '''
import os

USER = 'esco'
PASSWORD = '1234'

user = ''
password = ''

while USER != user or PASSWORD != password:
    os.system('cls')
    print('               kit-kot')
    user = input('Usuario: ')
    password = input('Contrasena: ')

    if USER != user or PASSWORD != password:
        print('Credenciales incorrectas')
        print('Intenta de nuevo')
        input('Presiona enter para continuar... ')
    else:
        print('Bienvenid@')

    input('Nos vemos...')