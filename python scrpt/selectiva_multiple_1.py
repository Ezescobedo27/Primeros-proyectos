'''
selectiva_multiple_1.py
script en Python que solicite al usuario una calificacion y una cantidad de
asistencias a un curso. Si la calificacion y la cantidad de asistencias son aprobatorias entonces
se le felicita por su logro; en caso contrario se le indicara en que fallo
'''
MIN_CAL = 60
MIN_ASI = 24

print('Por favor ingrese los siguientes datos')
Nombre = input('Cual es tu nombre? ')
calificacion = int(input('Calificacion: '))
asistencias = int(input('Asistencia: '))

if calificacion >= MIN_CAL and asistencias >= MIN_ASI:
    print(f'Felicidades {Nombre}, aprobaste este curso')

elif calificacion < MIN_CAL and asistencias >= MIN_ASI:
    print(f'Calificacion insuficiente. El minimo es {MIN_CAL}')

elif calificacion >= MIN_CAL and asistencias < MIN_ASI:
    print(f'Asistencias insuficientes. El minimo de asistencias es {MIN_ASI}')

else:
    print('Calificacion y Asistencias insuficientes')

print('Buen dia :D')


