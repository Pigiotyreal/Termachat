import socket
import threading

socket = socket.socket()
port = 1026
host = "127.0.0.1"

socket.bind((host, port))
print(f"Socket binded to {port}")

clients = []

print("Socket listening")

def globalsend(text):
    global clients
    for i in clients:
        i.sendall(bytes(text,'utf-8'))

def clientThread(client):
    client.sendall("Welcome to the server".encode('utf-8'))
    
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            
            if message == "/exit":
                clients.remove(client)
                client.close()
                return
            else:
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