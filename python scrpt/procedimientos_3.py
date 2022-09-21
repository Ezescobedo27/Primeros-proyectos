'''
procedimientos_3.py
script en Python que dentro de un procedimiento 
solicite el nombre y la edad 
del usuario y en caso de ser mayor o igual que 18 indique que
 es maypr
de edad, en caso contrario indicarle que aun es menor'''

def mayor_edad():
    
    Nombre = input('Cual es tu nombre? ')
    Edad = int(input('Cual es tu edad? '))
    if Edad >= 18:
        print(f'Ya eres mayor de edad, {Nombre}')
    else:
        print(f'Aun eres menor, {Nombre}')
mayor_edad()
        

print('Nos vemos')
 