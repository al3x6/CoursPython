import socket

host = 'localhost'  # ou l'adresse IP de ton serveur
port = 1234

s = socket.socket()
s.connect((host, port))
s.send(b"Hello Server!")
s.close()