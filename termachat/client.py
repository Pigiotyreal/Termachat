import socket
import threading

socket = socket.socket()
port = 8000

socket.connect(("127.0.0.1", port))

print(socket.recv(1024).decode())

user = input("Choose a username: ")
socket.send(user.encode())

user = socket.recv(1024).decode()
print(f"Your username is {user}")

def send():
    while True:
        message = input()
        socket.send(message.encode())
        
def receive():
    while True:
        message = socket.recv(1024).decode()
        print(message)
        
threading.Thread(target=send).start()
threading.Thread(target=receive).start()