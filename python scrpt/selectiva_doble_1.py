'''
selectiva_doble_1.py
script en Python que solicite al usuario intente adivinar un numero
entre el 1 y 10. Si el usuario lo adivina entonces lo felicita por su logro; 
en caso contrario le indica cual era el numero secreto.
'''
import random
secreto = random.randint(1, 10)
print('Acabo de generar un numero secreto entre 1 y 10.')
usuario = int(input('Cual crees que sea mi numero secreto?'))

if usuario == secreto:
    print('Logro desbloqueado: Adivin@ mistico')
else:
    print(f'Mi numero secreto era {secreto}')

print('Que tengas un buen dia')