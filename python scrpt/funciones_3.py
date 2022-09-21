'''
funciones_3.py
script en Python que implemente una funciona encargada de convertir
grador Fahrenheit a Celcius.
'''



def fahrenheit_a_celcius():
    f = float(input('Grados Fahrenheit: '))
    c = (f-32)/1.8
    return c

print('Programa que convierte grador Fahrenheit a Celcius')
celcius = fahrenheit_a_celcius()
print(f'Celcius: {celcius:.2f}')
