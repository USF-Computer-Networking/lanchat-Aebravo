#!/usr/bin/python

"""chatclient.py: This is the client application to the UDP chat server."""

__author__      = "Angelo Bravo"
__sources__     = "https://www.youtube.com/watch?v=PkfwX6RjRaIp"



import socket
import threading
import argparse
import time



shutdown = False

def receiving(name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print str(data)
        except:
            pass


host = '127.0.0.1'
port = 0 #pick any free port on computer

server = ('127.0.0.1', 10000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

#We run a thread so that we can be constantly receiving messages as well as sending them
rT = threading.Thread(target = receiving, args = ("RecvThread", s))
rT.start()


parser = argparse.ArgumentParser(description = 'This is your chat screen. Enter your name as a parameter to begin chatting.')
parser.add_argument("-name", help = "Enter your name. After you enter your name, type the messages youd like to send in the prompt.", dest = "name")
args = parser.parse_args()

name = args.name

s.sendto(name + " has joined chat.", server) #Becoming a client before you send your first message so you can receive messages as soon as you make your name
message = raw_input()

#typing q as a message will lead to shutdown
while message != 'q':
    if message != '':
        #sends message to server, server sends message to all clients
        s.sendto(name + ": " + message, server)
    message = raw_input()
    time.sleep(0.2)

shutdown = True
rT.join()
s.close()

