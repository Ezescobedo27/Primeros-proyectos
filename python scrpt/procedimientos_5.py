'''
procedimientos_5.py
script en Python que implemente un procedimiento que reciba el
nombre del usuario como argumento e imprima un saludo personalizado'''

def saludo(nombre):
    print(f'Hola {nombre}, gusto en conocerte!')


Pp = input('Como te llamas?')
saludo(Pp)
saludo('Rom')
saludo('SQ')

print('Nos vemos')