#########################################################################
#-*- coding:utf-8 -*-
# File Name: SocketServer_Tc.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月22日 星期二 16时20分54秒
#########################################################################
#!/usr/bin/env python2.7

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

while True:
	tcpCliSock = socket(AF_INET,SOCK_STREAM)
	tcpCliSock.connect(ADDR)
	data = raw_input('>')
	if not data:
		break
	tcpCliSock.send('%s\r\n'%data)
	data = tcpCliSock.recv(BUFSIZ)
	if not data:
		break
	print data.strip()
	tcpCliSock.close()
