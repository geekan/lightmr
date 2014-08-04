#!/usr/bin/env python

import socket
import time

echo_socket = socket.create_connection(('127.0.0.1', 8090))
for i in range(10):
    data = 'print(\'Hello, world!\')'
    echo_socket.send(data)
    print('send: ' + data)
    data = echo_socket.recv(9999)
    print('recv: ' + data)
    time.sleep(1)
