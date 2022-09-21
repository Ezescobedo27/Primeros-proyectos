# '''
# selectiva_doble_2.py
# script en Python que simule el sistema de validacion de una
# plataforma digital. El usuario debera proporcionar tanto su nombre
# como la contrasena. Si coinciden los valores con los previamente almacenados
# entonces se le dara la bienvenida, sino se indicara que hubo un error.
# '''


print('Sistema de validacion de datos')
USER= 'ESESE'
PASSWORD = '1234'

print('Ahora tienes que iniciar sesion')
user= input('user: ')
password = input('password:')

if user == USER and password == PASSWORD:
    print('Iniciaste sesion')
else:
    print('Datos incorrectos')

print(f'Que tengas un buen dia {USER}')


