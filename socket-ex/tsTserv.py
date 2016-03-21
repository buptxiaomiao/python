#########################################################################
#-*- coding:utf-8 -*-
# File Name: tsTserv.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月21日 星期一 16时27分00秒
#########################################################################
#!/usr/bin/env python2.7

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)#1
tcpSerSock.bind(ADDR)#2
tcpSerSock.listen(5)#3

while True:
	print 'waiting for connection...'
	tcpCliSock,addr = tcpSerSock.accept()#4
	print '...connected from:',addr

	while True:#5
		data = tcpCliSock.recv(BUFSIZ)
		if not data:
			break
		tcpCliSock.send('[%s] %s'%(
						ctime(),data))
		#tcpCliSock.close()
		#接收完客户端请求，就把客户端关了
tcpSerSock.close()
#ss = socket(AF_INET,SOCK_STREAM)创建服务器套接字
#ss.bind(addr)	把地址绑定到套接字上
#ss.listen(链接数)监听链接
#inf_loop:
#	cs = ss.accept()接收客户端连接
#comm_loop:
#	data = cs.recv()/cs.send()对话，接收/发送
#cs.close()	关闭客户端套接字
#ss.close() 关闭服务器套接字
