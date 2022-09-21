'''
selectiva_multiple_2.py
script en Python que muestre un menu con los nombres de distintos
paises de America y si el usuario selecciona alguna de las opciones
se le mostrara el nombre de la capital de ese pais
'''
MEXICO = 1
URUGUAY = 2
COLOMBIA = 3
ARGENTINA = 4
ECUADOR = 5 
PERU = 6

print('''                Capitales de America
1) Mexico
2) Uruguar
3) Colombia
4) Argentina
5) Ecuador
6) Peru
''')

opc = int(input('Selecciona una opcion:'))
if opc == MEXICO:
    print('Ciudad de Mexico')
elif opc == URUGUAY:
        print('Montevideo')
elif opc == COLOMBIA:
    print('Bogota')
elif opc == ARGENTINA:
    print('Buenos Aires')
elif opc == ECUADOR:
    print('Quito')
elif opc == PERU:
    print('Lima')
else:
    print('No elegiste ninguna de las opciones que te dimos')

print('Ten un buen dia')