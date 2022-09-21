''' 
procedimientos_4.py
script en Pythin que muestre un menu ciclico; dicho menu sera
implementado en un procedimiento'''
import os
ESP = 1
ING = 2
NO_SUBS = 3
SALIR = 4

def mostrar_menu():
    print(f'''
                                Subtitulos
    {ESP}) Espanol
    {ING}) Ingles
    {NO_SUBS}) No subtitulos
    {SALIR}) Salir    
    ''')

continuar = True 
while continuar:
    os.system('cls')
    mostrar_menu()
    opc = int(input('Selecciona una opcion'))
    os.system('cls')
    
    if opc == ESP:
        print('Subtitulos en espanol')

    elif opc == ING:
        print('Subtitulos en Ingles')
    elif opc == NO_SUBS:
        print('Sin subtitulos')

    elif opc == SALIR:
        continuar = False
    else:
        print('opcion no valida')
    input('Presiona enter para continuar...')
        
print('Nos vemmos...')
# import os

# MAGO = 1
# GUERRERO = 2
# SACERDOTIZA = 3
# SALIR = 4

# # BANDERA
# continuar =True 

# while continuar:
#     os.system('cls')
#     print(f'''                    PERSONAJES
#     {MAGO}) Mago
#     {GUERRERO}) Guerrero
#     {SACERDOTIZA}) Sacerdotiza
#     {SALIR}) Salir
#         ''')
#     opc = int(input('Selecciona tu personaje:'))
#     if opc == MAGO:
#         print('''
#         fuerza: 20
#         magia: 30''')
#     elif opc ==GUERRERO:
#         print('''
#         fuerza: 20
#         magia:19''')
#     elif opc == SACERDOTIZA:
#         print('''
#         fuerza: 20
#         magia: 30''')
#     elif opc == SALIR:
#         continuar = False
#     else:
#         print('Opcion no valida')
#     input('Presiona enter para continuar...')

# input('Nos vemos...')