import os
import random

inferior = 1
superior = 100 
secreto = random.randint(1, 100)
usuario = -1
maquina = -1

while usuario != secreto and maquina != secreto:
    os.system('cls')
    print('Maquina, Cual crees que 1sea el numero secreto?')
    maquina = random.randint(inferior, superior)
    print(f'Maquina: {maquina}')
    if maquina < secreto:
        print('Tu numero es menor ')
        inferior = maquina + 1
    elif maquina > secreto:
        print('Tu numero es mayor')
        superior = maquina - 1
    else:
        print('Ha ganado la maquina')


    # USUARIO
    if maquina != secreto:

       usuario =int(input('Usuario, Cual crees que sea el numero secreto?'))
    if usuario < secreto:
            print('Tu numero es menor')
            if usuario > inferior:
                inferior = usuario + 1
    elif usuario > secreto:
            print('Tu numero es mayor')
            if usuario < superior:
                superior = usuario - 1

    else:
            print(('El usuario ha ganado'))
    input('Presiona enter para continuar...')
    
input('Nos vemos')
