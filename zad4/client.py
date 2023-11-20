import os
import random
import errno
import time

FIFO = 'kolejka'

fifo_name = f"fifo_{random.randint(2, 9999)}"
fifo_path = os.path.join(os.path.dirname(__file__), fifo_name)
print(fifo_path)



id = input("Podaj id z bazy danych: ")

try:
    os.mkfifo(fifo_name)
except OSError as oe:
    if oe.errno != errno.EEXIST:
        raise

sign_to_server = os.open(FIFO, os.O_WRONLY)
os.write(sign_to_server, f'{len(fifo_path):02d}{fifo_path}{int(id):02d}'.encode())
os.close(sign_to_server)

print("Awaiting server response...")


fifo_in =  os.open(fifo_name, os.O_RDONLY)

while True:
    msg_len = os.read(fifo_in, 2)
    if len(msg_len) > 0:
        msg = os.read(fifo_in, int(msg_len)).decode()
        print("Msg: ", msg)
        break
    time.sleep(5)

os.close(fifo_in)
os.remove(fifo_path)