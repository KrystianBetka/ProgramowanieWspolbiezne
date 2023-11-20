import os
import errno
import signal
import time

FIFO = 'kolejka'
database = [(1, 'Kowalski'), (2, 'Nowak'), (3, 'Smith'), (4, 'Doe')]

def handle_signals(signum, frame):
    if signum == signal.SIGHUP:
        print("Received SIGHUP signal")
    elif signum == signal.SIGTERM:
        print("Received SIGTERM signal")
    elif signum == signal.SIGUSR1:
        print("Received SIGUSR1 signal. Exiting...")
        os._exit(0)  
signal.signal(signal.SIGHUP, handle_signals)
signal.signal(signal.SIGTERM, handle_signals)
signal.signal(signal.SIGUSR1, handle_signals)

try:
    os.mkfifo(FIFO)
except OSError as oe: 
    if oe.errno != errno.EEXIST:
        raise

fifo_in = os.open(FIFO, os.O_RDONLY)

while True:
    try:
        msg_len = os.read(fifo_in, 2)
        if len(msg_len) > 0:
            msg_len = int(msg_len)
            path = os.read(fifo_in, msg_len).decode()
            id = int(os.read(fifo_in, 2).decode())

            found = False
            for x in database:
                if x[0] == id:
                    found = x[1]
                    print(x[1])
                    break

            res = os.open(path, os.O_WRONLY)

            time.sleep(10)

            if found:
                os.write(res, f'{len(found):02d}{found}'.encode())
            else:
                notFound = "Nie ma"
                os.write(res, f'{len(notFound):02d}{notFound}'.encode())

            os.close(res)

    except Exception as e:
        print(f"Error: {e}")

    time.sleep(5)
