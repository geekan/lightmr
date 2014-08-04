#!/usr/bin/env python

import socket

echo_socket = socket.create_connection(('127.0.0.1', 8090))
echo_socket.send('Im sure u r a stupid guy')
