#########################################################################
#-*- coding:utf-8 -*-
# File Name: SocketServer_Ts.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月22日 星期二 16时15分26秒
#########################################################################
#!/usr/bin/env python2.7

from SocketServer import (TCPServer as TCP,StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST,PORT)

class MyRequestHandler(SRH):
	def handle(self):
		print '...connected from:',self.client_address
		self.wfile.write('[%s] %s'%(ctime(),self.rfile.readline()))
tcpServ = TCP(ADDR,MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()
