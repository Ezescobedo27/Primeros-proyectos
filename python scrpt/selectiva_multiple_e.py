# '''
# selectiva_multiple_e.py
# script en Python que simule una calculadora con las operaciones aritmeticas basicas.
# El menu mostrado sera el siguiente


# '''

print('Por favor ingrese los siguientes 2 numeros de su cuenta')

SUMA = 1
RESTA = 2
MULTIPLICACION = 3
DIVISION = 4
DIVISION_ENTERA = 5
MODULO = 6
POTENCIA = 7
print(f'''  Operaciones aritmeticas
{SUMA}) suma
{RESTA}) resta
{MULTIPLICACION}) multiplicacion
{DIVISION})division
{DIVISION_ENTERA}division_entera
{MODULO})modulo
{POTENCIA})potencia
''')
opc = int(input("Elige una opcion: ")) 
numero_1 = int(input('Elige un numero: '))
numero_2 = int(input('Elige otro numero: '))

if opc == SUMA: 
    print(f'{numero_1} + {numero_2} = {numero_1+numero_2}')
elif opc == RESTA:
    print(f'{numero_1}-{numero_2} = {numero_1*-numero_2}')
elif opc == MULTIPLICACION:
    print(f'{numero_1} * {numero_2} = {numero_1*numero_2}')
elif opc == DIVISION:
    print(f'{numero_1} / {numero_2} = {numero_1/numero_2}')
elif opc == DIVISION_ENTERA:
    print(f'{numero_1} // {numero_2} = {numero_1//numero_2}')
elif opc == MODULO:
    print(f'{numero_1} % {numero_2} = {numero_1%numero_2}')
elif opc == POTENCIA:
    print(f'{numero_1} ** {numero_2} = {numero_1**numero_2}')

else:
    print('Opciones invalidas')

print('Ten un buen dia') 