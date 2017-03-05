#########################################################################
#-*- coding:utf-8 -*-
# File Name: myThread.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月22日 星期二 21时47分32秒
#########################################################################
#!/usr/bin/env python2.7

import threading
from time import ctime

class MyThread(threading.Thread):
	def __init__(self,func,args,name=''):
		threading.Thread.__init__(self)
		self.name=name
		self.func=func
		self.args=args
	def getResult(self):
		return self.res	
	def run(self):
		print 'starting',self.name,'at:',ctime()
		self.res = apply(self.func,self.args)
		print self.name,'finished at:',ctime()

