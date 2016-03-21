#########################################################################
#-*- coding:utf-8 -*-
# File Name: tsUclnt.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月21日 星期一 19时06分56秒
#########################################################################
#!/usr/bin/env python2.7

#cs = socket()
#commen_loop:
#	cs.recvfrom()/cs.sendto()
#cs.close()

from socket import *
HOST = 'localhost'
PORT = 21567	
BUFSIZ = 1024
ADDR = (HOST,PORT)
#client must know ADDR of SERVER
udpcsock = socket(AF_INET,SOCK_DGRAM)#1
#no connection.
while True:
	data = raw_input('> ')
	if not data:
		break
	udpcsock.sendto(data,ADDR)#2 send data to ADDR
	data,addr = udpcsock.recvfrom(BUFSIZ)#3 return data and sender addr
	if not data:
		break
	print data
udpcsock.close()

