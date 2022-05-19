import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = 'This is the message. It will be repeated.'.encode()

for p1 in range(8000, 8100):
    for p2 in range(8000, 8100):
        for p3 in range(8000, 8100):
            print(p1,p2,p3)
            sent = sock.sendto(message, ('10.0.108.66', p1))
            sent = sock.sendto(message, ('10.0.108.66', p2))
            sent = sock.sendto(message, ('10.0.108.66', p3))
            sent = sock.sendto(message, ('10.0.108.66', p1))
            sent = sock.sendto(message, ('10.0.108.66', p2))
            sent = sock.sendto(message, ('10.0.108.66', p3))
socket.close()