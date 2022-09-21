'''

anidamiento_estructural.pu
script en Python que simula un juego de preguntas y respuestas, 
si es usuario contesta corretamente una pregunta puede continuar
con la siguiente, en csso de fallar, se le ndica que ha perdidos y
si contesta acertadamente todas las preguntas se le felicita por su
conocimiento.
'''
print('Bienvenid@, pongamos a prueba tus conocimiento')
respuesta = int(input('Cual es la velocidad de la luz en m/s?'))
if respuesta == 299792458:
    print('Respues correcta')
    respuesta = int(input('Cuanto es 8+8/8*8?'))
    if respuesta == 8+8/8*8:
        print('Respues correcta')
        respuesta = int(input('De que color eran las mangas del chaleco de napoleon: '))
        if respuesta == 'Los chalecos no tienen mangas':
            print('Felicidades')
        else:
            print('Lo siento, no es la respuesta correcta')


    else:
        print('Lo siento, la respuesta es incorrecta')
        
else:
    print('Lo siento, la respuesta es incorrecta')

print('Nos vemos') 