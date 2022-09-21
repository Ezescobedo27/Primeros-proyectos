# '''
# repetitiva_mientras_4.py
# script en Python que muentre un menu con distintos personajes de un videojuego.
# Si el usuario selecciona alguno de los personajes, se le mostraran algunas de uss caracteristicas.
# El menu sera ciclico y se mostrara mientras el usuario nos indique que desea salir
# '''

import os

MAGO = 1
GUERRERO = 2
SACERDOTIZA = 3
SALIR = 4

# BANDERA
continuar =True 

while continuar:
    os.system('cls')
    print(f'''                    PERSONAJES
    {MAGO}) Mago
    {GUERRERO}) Guerrero
    {SACERDOTIZA}) Sacerdotiza
    {SALIR}) Salir
        ''')
    opc = int(input('Selecciona tu personaje:'))
    if opc == MAGO:
        print('''
        fuerza: 20
        magia: 30''')
    elif opc ==GUERRERO:
        print('''
        fuerza: 20
        magia:19''')
    elif opc == SACERDOTIZA:
        print('''
        fuerza: 20
        magia: 30''')
    elif opc == SALIR:
        continuar = False
    else:
        print('Opcion no valida')
    input('Presiona enter para continuar...')

input('Nos vemos...')