'''
funciones_2.py
script en Python que implemente una funcion encargada de calcular el
indice de masa corporal del usuarior.
'''
def calcular_IMC():
    peso = float(input('Peso: '))
    estatura = float(input('Estatura: '))
    imc = peso / (estatura ** 2)
    return imc
    
print('Vamos a calcular tu IMC: ')
imc = calcular_IMC()
print(f'Tu indice de mas corporal es: {imc :.2f}')

print('Nos vemos....')