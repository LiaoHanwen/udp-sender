import socket
import time

PORT = 8090

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # create udp socket
counter = 0  # counter for receive
server.bind(("0.0.0.0", PORT))  # bind port
while(True):
    counter += 1
    data, addr = server.recvfrom(1024)
    print(str(counter) + ":", addr, data)
