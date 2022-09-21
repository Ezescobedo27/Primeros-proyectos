'''
repetitiva_desde_e.py
script en Python que muestre un cronometro en formato de 24 horas.
El despliegue seguira en formato h:m:s. El cronometro debera
iniciar en 0:0:0 y podra llegar hasta las 23:59:59. implementar
retardor de 1 segundo y limpieza de pantalla de tal forma que solo
se vea un tiempo en pantalla
'''
import os
import time

for hora in range(24):
    for minuto in range(60):
        for segundo in range(60):
            os.system('cls')
            print(f'{hora}:{minuto}:{segundo}')
            time.sleep(1)
                
        
            
 