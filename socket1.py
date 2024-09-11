import socket
s = socket.socket()
host = "ftp.ibiblio.org"
port = 21
s.connect((host, port))
data = s.recv(512)
print(data.decode())
s.send("USER anonymous\r\n".encode())
data = s.recv(512)
print(data.decode())
s.send("PASS test@free.fr\r\n".encode())
data = s.recv(512)
print(data.decode())
s.close()
