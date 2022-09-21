import os

DOMINIC = 1
KEVIN = 2
DURAN = 3
DANIEL = 4
NANCY = 5

bandera = True
while bandera:
    os.system('cls')
    print(f'''
    {DOMINIC})Dominic
    {KEVIN})Kevin
    {DURAN})Duran
    {DANIEL})Daniel
    {NANCY})Nancy
    ''')

    opc = input('Elige un personaje')
    
    if opc == 1:
        print('Tu personaje es Dominic')

    elif opc == 2:
        print('Tu persona es Kevin')

    elif opc == 3:
        print('Tu persona es Duran')

    elif opc == 4:
        print('Tu persona es Daniel')

    elif opc == 5:
        print('Tu personaje es Nancy')

    else:
        print('Opcion no valida')
        bandera = False
        input('Presiona enter para continuar')
    
print('Nos vemos')