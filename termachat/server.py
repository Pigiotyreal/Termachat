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
    conn.close()
    
    break
    