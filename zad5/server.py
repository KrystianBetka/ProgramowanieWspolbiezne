import sysv_ipc
import time

input_key = 111
output_key = 222

mq_input = sysv_ipc.MessageQueue(input_key, sysv_ipc.IPC_CREAT)
mq_output = sysv_ipc.MessageQueue(output_key, sysv_ipc.IPC_CREAT)

slownik = { 'dom': 'house',
            'kot': 'cat',
            'pies': 'dog',
            'samochód': 'car'}

while True:
    message, client_pid = mq_input.receive(True, 0)
    message = message.decode()
    
    odpowiedz = slownik.get(message, 'Nie znam takiego słowa')

    mq_output.send(odpowiedz.encode(), True, client_pid)