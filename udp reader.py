import socket
import time

TIME = 1     #s

PORT = 8090

server90=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #create udp socket
counter = 0     #counter for dispatch
server90.bind(("0.0.0.0",PORT))
while(True):
    counter += 1
    addr, data = server90.recvfrom(1024)
    print(str(counter) + ":", addr, data)
    time.sleep(TIME)
