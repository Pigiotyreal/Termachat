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
        try:
            message = client.recv(1024).decode()
            print(f"{user}: {message}")
            
            for c in clients:
                c.send(f"{user}: {message}".encode())
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            
            user = user[index]
            print(f"User {user} disconnected")
            break

while True:
    client, address = socket.accept()
    clients.append(client)
    threading.Thread(target=clientThread, args=(client,)).start()