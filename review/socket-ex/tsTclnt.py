#########################################################################
#-*- coding:utf-8 -*-
# File Name: tsTclnt.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月21日 星期一 16时33分49秒
#########################################################################
#!/usr/bin/env python2.7

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)#1
a= tcpCliSock.connect(ADDR)#2 ADDR IS SERVER_ADDR
						#localhost is 127.0.0.1
						#call localhost server

while True:#3
	#print a---return None
	data = raw_input('>')
	if not data:
		break
	tcpCliSock.send(data)
	data = tcpCliSock.recv(BUFSIZ)
	if not data:
		break
	print data

tcpCliSock.close()

#cs = socket()客户端套接字
#cs.connect()尝试连接服务器
#commen_loop:通信循环
#	cs.send()/cs.recv()对话
#cs.close()
