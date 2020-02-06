import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

def dormir()
    time.sleep(1)

t1 = treading.Thread(target=dormir, name='thread desde funcion')
t1.start()

class UnThread(threading.Thread):
    def __init__(self)
        super().__init__()
        self.name='threadClass'
    def run(self):
        logging.info('enpezando desde clase')
        time.sleep(1)
        logging.info('finalizando desde clase')
