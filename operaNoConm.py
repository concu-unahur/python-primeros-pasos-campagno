import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

#defino funciones y variable
#dale un valor inicial a la variable

var = 1
lock = threading.Lock()

def sumarUno():
    global var
    global lock
    try:
        lock.acquire()
        var += 1
    finally:
        lock.release()

def multiplicarPorDos():
    global var
    global lock
    try:
        lock.acquire()
        var = var*2
    finally:
        lock.release()
#ejecutá cada función en un thread separado y anotá los resultados
t1 = threading.Thread(target=sumarUno, name='Sumar 1')


t2 = threading.Thread(target=multiplicarPorDos, name='Multiplica por 2')

t1.start()

t2.start()

print(f'Total vale {var}')

