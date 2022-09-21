# '''
# selectiva_Simple_e.py
# script en Python que implemente un sistema de redonde de 
# calificaciones. El usuario es el encargado de ingresar
# su calificacion. Si a la calificacion le faltan 4 unidades o menos
# para el siguiente multiplo de 10, entonces su calificaciones
# sera redondeada al siguiente muktiplo de 10, en caso
# contrario la calificacion no es modificada.
# ejemplo:

# Si el usuario obtuvo 76 entonces se redondea a 80.
# '''

Calificacion = int(input('Cual es tu calificacion?'))
residuo = Calificacion % 10
mensaje = 'Tu calificacion no amerita redondeo.'

if 0 <= Calificacion <= 100 and residuo >= 6:
    Calificacion = Calificacion + (10 - residuo)
    mensaje = f'Tu calificacion es {Calificacion} '

print(mensaje)
print('Que tengas un buen dia') 

