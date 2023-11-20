import socket

host = socket.gethostname()
port = 3000

socket_client = socket.socket()
socket_client.connect((host, port))

message = input(" -> ")

while message.lower().strip() != "bye":
    socket_client.send(message.encode())
    
    data = socket_client.recv(1024).decode()

    print("Response from server: "+ data)

    message = input(" -> ")
socket_client.close()