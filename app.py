#!/usr/bin/env python
import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
while True:
    conn, addr = sock.accept()
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())
    conn.close()
#Test comment
