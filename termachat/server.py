import socket
import threading
from datetime import datetime

socket = socket.socket()
port = 1026
host = "127.0.0.1"

socket.bind((host, port))
print(f"Socket binded to {port}")

clients = []

print("Socket listening")

def globalsend(text):
    try:
        global clients
        timestamp = datetime.now().strftime("%H:%M:%S")
        text = f"[{timestamp}] {text}"
        for client in clients:
            client.sendall(text.encode('utf-8'))
    except:
        print("Error sending message to clients.")

def clientThread(client):
    client.sendall("Welcome to the server".encode('utf-8'))
    
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            
            globalsend(message)
        except:
            clients.remove(client)
            try:
                client.close()
            except:
                pass
            return

while True:
    socket.listen(1)
    client, address = socket.accept()
    clients.append(client)
    threading.Thread(target=clientThread, args=(client,)).start()