import socket
import base64
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 50012))
s.listen(1)
conn, addr = s.accept()
while 1:
    data = conn.recv(1024)
    if not data:
        break
    with open('dobriden.jpg', "rb") as image2str:
        converted_string = base64.b64encode(image2str.read())
    conn.send(converted_string)
conn.close()