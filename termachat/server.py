import socket
import threading

socket = socket.socket()
port = 8000

socket.bind(("", port))
print(f"Socket binded to {port}")

socket.listen(5)
print("Socket listening")

clients = []

def clientThread(client):
    client.send("Welcome to the server".encode())
    
    user = client.recv(1024).decode()
    print(f"User {user} connected")
    client.send(user.encode())
    
    while True:
        message = client.recv(1024).decode()
        print(f"{user}: {message}")
        
        if message == "exit":
            clients.remove(client)
            break
        
        for c in clients:
            if not message == "exit":
                c.send(f"{user}: {message}".encode())
    
    client.close()
    print(f"User {user} disconnected")

while True:
    client, address = socket.accept()
    clients.append(client)
    threading.Thread(target=clientThread, args=(client,)).start()