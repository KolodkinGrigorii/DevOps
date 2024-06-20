#!/usr/bin/env python
import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
while True:
    conn, addr = sock.accept()
    conn.send('Hello from Server!'.encode())
    conn.close()
