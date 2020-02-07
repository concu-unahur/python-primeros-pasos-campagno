import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

#defino funciones y variable
#dale un valor inicial a la variable

var = 1

def sumarUno():
    global var
    var += 1

def multiplicarPorDos():
    global var
    var = var*2
#ejecutá cada función en un thread separado y anotá los resultados
t1 = threading.Thread(target=sumarUno, name='Sumar 1')


t2 = threading.Thread(target=multiplicarPorDos, name='Multiplica por 2')

t1.start()

t2.start()

print(f'Total vale {var}')

