import socket
import threading
from time import sleep

socket = socket.socket()
port = 1026
host = "127.0.0.1"

print("Connecting..")
socket.connect((host, port))

print(socket.recv(1024).decode())

while True:
    user = input("Choose a username: ")
    if len(user) > 30 or len(user) < 2:
        print("Username must be 2-30 characters long.")
    else:
        break

def send():
    while True:
        message = input()
        socket.sendall(bytes(f"{user}: {message}",'utf-8'))
        
def receive():
    while True:
        message = socket.recv(1024).decode('utf-8')
        if not message.startswith(user):
            timestamp, message = message.split("] ", 1)
            print(f"{timestamp}] {message}")
        
print("Starting listener..")
threading.Thread(target=receive).start()
sleep(1)

socket.sendall(bytes(f"User '{user}' has connected. Say hello!",'utf-8'))
print("Starting sender..")
sleep(1)

print("Connected!")
send()