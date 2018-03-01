#!/usr/bin/python

"""chatserver.py: This is a simple UDP chat server."""

__author__      = "Angelo Bravo"
__sources__     = "https://www.youtube.com/watch?v=PkfwX6RjRaIp"


import socket
import time

host = '127.0.0.1'
port = 10000

#keep a list of clients to send data to
clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #create a udp socket
s.bind((host,port))
s.setblocking(0) #will not block data, if no data is available, an error will be thrown


running = True
print "Server started."

while running:
    try:
        data, addr = s.recvfrom(1024) #recieve data with a budder of 1024 bits
        if  "Quit" in str(data):
            running = False
        if addr not in clients:
            clients.append(addr) #add new clients to clients list

        print time.ctime(time.time()) + str(addr) + ":" + str(data) #print message with time stamp
        #server sends message data to all clients
        for client in clients:
            if(addr != client) : #So you dont resend yourself messages
                s.sendto(data, client)

    except:
        pass

s.close()

