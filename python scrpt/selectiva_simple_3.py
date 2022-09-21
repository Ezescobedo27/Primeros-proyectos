# '''
# selectiva_simple_3.py
# script en Python que solicite al calificacion y cantidad de asistencia a un
# curso. Si la calificacion es mayor o igual que 60 y la cantidad de
# asistencias es mayor que 20 entonces que le indique que ha aprobado el curso

# ''' 
nombre = input('cual es tu nombre? ')


calificacion = int(input('Cual es tu calificacion? '))
asistencia = int(input('cuantas asistencias tuviste? '))

if calificacion >= 60 or asistencia >= 20:
    print(f'felicidades {nombre}, aprovaste')
if calificacion >= 95:
    print(f'{nombre} eres un exelente estudiante, pidele beca a amlo')

print('Sigue disfrutando tu dia')