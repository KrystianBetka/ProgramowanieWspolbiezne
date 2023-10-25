import socket

host = socket.gethostname()
port = 3000

server_socket = socket.socket()
server_socket.bind((host,port))
server_socket.listen(1)
print("server listening on port: "+ str(port) )

connection, address = server_socket.accept()

print("Connection from: " + str(address))

while True:
    data = connection.recv(1024).decode()
    if not data:
        break
    print("from connected user: " + str(data))
    data = input(' -> ')
    connection.send(data.encode())

connection.close