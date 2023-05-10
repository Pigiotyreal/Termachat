import socket

socket = socket.socket()
port = 8000

socket.bind(("", port))
print(f"Socket binded to {port}")