import os
import errno
import time

FIFO = 'kolejka'
database = [(1, 'Kowalski'), (2, 'Nowak'), (3, 'Smith'), (4, 'Doe')]


# utworzenie kolejki
try:
    os.mkfifo(FIFO)
except OSError as oe: 
    if oe.errno != errno.EEXIST:
        raise

fifo_in = os.open(FIFO, os.O_RDONLY)

fifo_out1 = os.open(FIFO, os.O_WRONLY|os.O_NDELAY) 

print(os.read(fifo_in,2),len(os.read(fifo_in,2)))
# while True:
#     msg = os.read(fifo_in, 2) # czytanie 2 bajtĂłw
#     print(msg)
#     if len(msg)>0:    
#       print(msg)
#     else:       
#       print("Klient skończył")
#       break
#     time.sleep(5) 