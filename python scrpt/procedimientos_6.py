'''
procedimientos_6.py
script en Python que inplemente un procedimiento que reciba el
nombre y la edad del usuario y en cas oque la edad sea mayor o igual que
18 le indique que ya es mayor de edad; en caso contrario le indique que es 
menor de edad
'''
def mayor_edad(nombre, edad):
    print(f'Hola {nombre}, un gusto verte de nuevo')
    if edad >= 18:
        print('Veo que ya eres mayor de edad')
    else:
        print('Veo que aun eres menor de edad')

mayor_edad('Juan', 20)

print('Nos vemos...')