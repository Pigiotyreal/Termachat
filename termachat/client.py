import socket

socket = socket.socket()
port = 8000

socket.connect(("127.0.0.1", port))

print(socket.recv(1024).decode())
socket.close()