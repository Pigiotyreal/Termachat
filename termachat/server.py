import socket
import threading

socket = socket.socket()
port = 8000

socket.bind(("", port))
print(f"Socket binded to {port}")

socket.listen(5)
print("Socket listening")

clients = []
users = []

def clientThread(client):
    client.send("Welcome to the server".encode())
    
    user = client.recv(1024).decode()
    
    if user in users:
        user = user + "1"
        while user in users:
            user = user[:-1] + str(int(user[-1]) + 1)
    users.append(user)
    
    if len(user) > 25:
        client.send("Username too long, max 25 chars".encode())
        return
    if len(user) < 3:
        client.send("Username too short, min 3 chars".encode())
        return
    if not user.isalnum() or " " in user:
        client.send("Username must be alphanumeric and cannot contain spaces".encode())
        return
    
    print(f"User {user} connected")
    client.send(user.encode())
    
    while True:
        try:
            message = client.recv(1024).decode()
            
            if message == "/exit":
                index = clients.index(client)
                clients.remove(client)
                
                user = user[index]
                print(f"User {user} disconnected")
                return
            
            print(f"{user}: {message}")
            
            for c in clients:
                c.send(f"{user}: {message}".encode())
        except:
            index = clients.index(client)
            clients.remove(client)
            
            user = user[index]
            print(f"User {user} disconnected")
            return

while True:
    client, address = socket.accept()
    clients.append(client)
    threading.Thread(target=clientThread, args=(client,)).start()