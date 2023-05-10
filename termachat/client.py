import socket

socket = socket.socket()
port = 8000

socket.connect(("127.0.0.1", port))

print(socket.recv(1024).decode())

user = input("Choose a username: ")
socket.send(user.encode())

user = socket.recv(1024).decode()
print(f"Your username is {user}")

socket.close()