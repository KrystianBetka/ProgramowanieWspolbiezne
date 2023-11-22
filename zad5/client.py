import sysv_ipc
import os

input_key = 111
output_key = 222

mq_input = sysv_ipc.MessageQueue(input_key)
mq_output = sysv_ipc.MessageQueue(output_key)

request = input("Znajdź szukane słowo: ")

pid = os.getpid()

mq_input.send(request.encode(),True,pid)


response, msg_type = mq_output.receive(True, pid)
response = response.decode()

print(f"Otrzymałem odp od serwera: {response}")