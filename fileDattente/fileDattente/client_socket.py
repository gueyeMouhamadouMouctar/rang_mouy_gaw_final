#not /usr/bin/python
# -*- coding: latin-1 -*-
import socket

def client(ip, port, message):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
		sock.connect((ip, port))
		sock.sendall(bytes(message, 'utf-8'))
		response = str(sock.recv(1024), 'utf-8')