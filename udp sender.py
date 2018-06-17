# python3

# udp sender
# send a udp packet every time span
# PACKET: packet content
# TIME: time span
# IP: ip address of the destination
# PORT: port of the destination

import socket
import time

PACKET = bytes("12345", encoding="utf-8")    #use bytes or encode with "bytes(string, encoding)"

########################  EXAMPLE ##############################
# BYTES = b'\x12\x34\x56\x78\x90\xab\xcd\xef'
# BYTES = bytes(STR, encoding="utf-8")      #convert str to bytes
# BYTES = bytes(str(NUM), encoding="utf-8") #convert num to bytes
################################################################

TIME = 1     #s

IP = "192.168.137.255"
PORT = 8090

client=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #create udp socket
counter = 0     #counter for dispatch

while(True):
    counter += 1
    client.sendto(PACKET, (IP,PORT))   #send message
    print("counter:" + str(counter))
    time.sleep(TIME)
