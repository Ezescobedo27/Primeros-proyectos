# '''
# secuencial_4.py
# script en Python que solicite al usuario 2 numeros y posteriormente uestre
# la suma de ambos valores.
# '''

Numero_1 = input('Escribe un numero: ')
# Conversion de tipo str a int
Numero_1 =  int(Numero_1)
Numero_2 = int(input('Escribe otro numero: '))
Real = float(input('Ingresa un numero con punto decimal'))
Suma = Numero_1 + Numero_2 + Real
print(Suma)