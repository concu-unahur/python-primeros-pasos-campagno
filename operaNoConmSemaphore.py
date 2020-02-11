import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

#defino funciones y variable
#dale un valor inicial a la variable

#Implementamos Semaphore para realizar el Mismo ejercicio en lugar de utilizar Lock

var = 1
semaphore = threading.Semaphore(3)

def sumarUno():
    global var
    global semaphore
    try:
        semaphore.acquire()
        var += 1
    finally:
        semaphore.release()

def multiplicarPorDos():
    global var
    global semaphore
    try:
        semaphore.acquire()
        var = var*2
    finally:
        semaphore.release()


#ejecutá cada función en un thread separado y anotá los resultados


t1 = threading.Thread(target=sumarUno, name='Sumar 1')
t2 = threading.Thread(target=multiplicarPorDos, name='Multiplica por 2')


#semaphore.acquire()


t2.start()
t1.start()


logging.info(t2)

#t1.join()
#t2.join()

print(f'Total vale {var}')

