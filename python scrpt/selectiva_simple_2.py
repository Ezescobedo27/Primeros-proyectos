'''
selectiva_simple_2.py
script en Python que genere un numero aleatorio entre 1 y 10 y le pida al usuario que intente adivinarlo. Si adivina
el numero que lo felicite por su logro
'''
nombre = input('Cual es tu nombre?')
#agree el modulo random a mi progra,a y con eso me permite generar numeros aleatorios
import random

secreto = random.randint(1, 10)

print('Acabo de generar un numero aleatorio entre 1 y 10. Intenta adivinar')
numero = int(input('Cual crees que Eduqsea mi numero?: '))

if numero == secreto:
    print(f'Felicidades {nombre} adivinaste el numero')


print('Sigue disfrutando tu dia')
