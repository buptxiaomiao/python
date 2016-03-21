#########################################################################
#-*- coding:utf-8 -*-
# File Name: tsUserv.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月21日 星期一 19时01分09秒
#########################################################################
#!/usr/bin/env python2.7

#ss = socket()
#ss.bind()
#inf_loop:
#	cs = cs.recvfrom()
#	cs = ss.sendto()
#ss.close()
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

udpssock = socket(AF_INET,SOCK_DGRAM)#1
udpssock.bind(ADDR)#2

#SERVER know client addr by recvfrom
while True:
	print 'waiting for message...'
	data,addr = udpssock.recvfrom(BUFSIZ)#3 return data and sender addr
	udpssock.sendto('[%s] %s'%(ctime(),data),addr)#4 send data to addr
	print '...received from and return to:',addr
uspssock.close()
