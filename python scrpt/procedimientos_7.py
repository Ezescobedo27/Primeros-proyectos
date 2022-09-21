'''
procedimientos_7.py
script en Python que implemente un procedimieinto dentro
del cual se miestre la tabla de muultiplicar de
un numero recibido como argumento.
El procedimiento contara con un segundo arguumento
que indicara que multiplo se mostrara la tabla
de multiplicar. Ese segundo argumento tendra valor por
omision del numero 10
'''
def tabla_multiplicar(numero, limite=10):
    print(f'                  Tabla de multiplicar del {numero}')
    for i in range(1, limite+1):
        print(f'{numero} x {i} = {numero * i}')
  
tabla_multiplicar(8)
tabla_multiplicar(5, 18) 