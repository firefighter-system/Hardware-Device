import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.0.19'

port = 65428
s.connect((host, port))
print(s.recv(1024))

inputVar = input('Enter Message')
while inputVar != "END":
    s.send(bytearray(inputVar,'UTF-8'))
    print(s.recv(1024))
    inputVar = input('Enter New Message')

s.close()