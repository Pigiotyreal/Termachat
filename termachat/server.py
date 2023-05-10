import socket

socket = socket.socket()
port = 8000

socket.bind(("", port))
print(f"Socket binded to {port}")

socket.listen(5)
print("Socket listening")

while True:
    conn, addr = socket.accept()
    print(f"Got a connection from {addr}")
    
    conn.send("Connected!".encode())
    
    user = conn.recv(1024).decode()
    
    if len(user) < 3:
        conn.send("Invalid username, min chars 3".encode())
        conn.close()
        continue
    if len(user) > 35:
        conn.send("Invalid username, max chars 35".encode())
        conn.close()
        continue
    if user.isalnum() == False:
        conn.send("Invalid username, alphanumeric only".encode())
        conn.close()
        continue
    if user.isspace() == True:
        conn.send("Invalid username, no spaces".encode())
        conn.close()
        continue
    
    conn.send(user.encode())
    
    conn.close()
    break