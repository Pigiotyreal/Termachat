import socket
import threading
import sys
import time
import os
import shutil
from time import sleep, time

socket = socket.socket()
port = 1026
host = "127.0.0.1"

lastTime = 0
messageCount = 0

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
    global lastTime
    global messageCount
    
    while True:
        message = input()
        if message == "/exit":
            socket.sendall(bytes(f"User '{user}' has disconnected.",'utf-8'))
            socket.close()
            sys.exit()
        elif message == "/help":
            print("Commands:\n/exit - Disconnect from the server")
            print("/help - Show this help message")
            print("/clear - Clears all visible messages")
        elif message == "/clear":
            print("\n"*100)
        elif message.startswith("/upload "):
            try:
                filename = message.split(" ", 1)[1]
                if os.path.isfile(filename):
                    if os.path.getsize(filename) > 2097152:
                        print("File must be under 2MB.")
                        continue
                    with open(filename, "rb") as f:
                        socket.sendall(f.read())

                    shutil.copy(filename, "files")
                    
                    print("File uploaded successfully.")
                else:
                    print("File does not exist.")
            except:
                print("Error uploading file.")
        elif message.startswith("/download "):
            try:
                filename = message.split(" ", 1)[1]
                if os.path.isfile(f"files/{filename}"):
                    with open(f"files/{filename}", "rb") as f:
                        with open(filename, "wb") as f2:
                            f2.write(f.read())
                        
                    print("File downloaded successfully.")
                else:
                    print("File does not exist.")
            except:
                print("Error downloading file.")
            
        elif len(message) > 612:
            print("Message must be 612 characters or less.")
        elif len(message) < 1:
            print("Message must be 1 character or more.")
        else:
            currTime = time()
            timeLast = currTime - lastTime
            
            if timeLast < 1 and messageCount > 5:
                print("You are sending messages too fast.")
                continue
            
            try:
                socket.sendall(bytes(f"{user}: {message}",'utf-8'))
                messageCount += 1
                lastTime = currTime
            except:
                print("Error sending message to server.")
        
def receive():
    while True:
        try:
            message = socket.recv(1024).decode('utf-8')
            if not message.startswith(user):
                timestamp, message = message.split("] ", 1)
                print(f"{timestamp}] {message}")
        except:
            print("Error receiving message from server.")
        
print("Starting listener..")
threading.Thread(target=receive).start()
sleep(0.25)

socket.sendall(bytes(f"User '{user}' has connected. Say hello!",'utf-8'))

print("Starting sender..")
sleep(0.25)

print("Connected!")
send()