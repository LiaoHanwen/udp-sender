#!/usr/bin/python3

'''
Receive data from port 8090/8091 and transmit it to destination
'''

import socket
import threading

HOST = "192.168.137.1"  # IP for local host
TRANSMIT_IP = "www.bjxiaozhuan.com"  # IP for transmit destination


class StartThread(threading.Thread):
    '''New Thread'''

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Thread Start：" + self.name)
        transmit(self.thread_id, self.name)


def transmit(port, name):
    '''
    Create a UDP socket
    Receive data and transmit
    '''
    server = socket.socket(
        socket.AF_INET, socket.SOCK_DGRAM)  # create udp socket
    server.bind((HOST, port))
    while True:
        data, client = server.recvfrom(1024)  # receive

        # print message
        print("Thread name:", end="")
        print(name, end="")
        print("    From: ", end="")
        print(client, end="")
        print("    Data: ", end="")
        print(data)
        server.sendto(data, (TRANSMIT_IP, port))  # send


# Change the port there
THREAD8090 = StartThread(8090, "8090", 1)
THREAD8091 = StartThread(8091, "8091", 2)

THREAD8090.start()
THREAD8091.start()
