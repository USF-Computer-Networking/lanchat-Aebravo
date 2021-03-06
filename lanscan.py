#!/usr/bin/python

"""chatserver.py: This is a simple UDP chat server."""

__author__      = "Angelo Bravo"
__sources__     = "https://www.youtube.com/watch?v=waUq2ozwYM8, https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib"


import ipaddress
import sh
import socket


#get network address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
networkAddress = s.getsockname()[0] #returns socket's own address
s.close()

first, second, third, fourth = str(networkAddress).split('.')

#modify network address to scan all addresses
addr = str(first) + '.' + str(second) + '.' + str(third) + '.' + '0/24'

network = ipaddress.ip_network(unicode(addr))

for i in network.hosts():

    try:
        sh.ping(i, "-c 1")
        print i, "is active"
    except sh.ErrorReturnCode_2:
        print "no response from", i