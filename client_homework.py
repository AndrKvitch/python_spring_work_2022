import socket
import base64
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50012))
s.sendall(b'Hello, world')
data = s.recv(1024)
decode = open('dobriden.jpg', 'wb')
decode.write(base64.b64decode((data)))
decode.close()
s.close()