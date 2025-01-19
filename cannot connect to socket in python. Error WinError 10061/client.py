import socket

print("Client calling .....")

socket_main = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_main.connect(("192.168.1.171", 8089))
message = "Hello"
socket_main.send(message.encode())
