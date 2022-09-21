'''
procedimientos_2.py
script en Python solicite el nombre del usuari y lo salude
de manera personalizada haciendo uso de un procedimiento 
'''
from pprint import pprint


def saludo_personalizado():
    nombre = input('Hola Como te llamaas?')
    print(f'Gusto en conocerte, {nombre}')

saludo_personalizado()
