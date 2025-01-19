import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(
    socket.SOL_SOCKET, socket.SO_REUSEADDR, 1
)  # allows reuse of the same port if the server script restarts
serversocket.bind(("", 8089))
serversocket.listen(5)  # become a server socket, maximum 5 connections

while True:
    connection, address = serversocket.accept()
    try:
        buf = connection.recv(64)
        if buf:
            print(buf)
    finally:
        connection.close()
