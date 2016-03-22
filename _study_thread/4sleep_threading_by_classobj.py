#########################################################################
#-*- coding:utf-8 -*-
# File Name: mtsleep4.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月22日 星期二 21时19分05秒
#########################################################################
#!/usr/bin/env python2.7

import threading 
from time import sleep,ctime

loops = [4,2]

class ThreadFunc(object):
	
	def __init__(self,func,args,name=''):
		self.name = name
		self.func = func
		self.args = args

	def __call__(self):#__call__相当于重载（）
						#可以把一个类对象当作函数
						#当作函数调用
		apply(self.func,self.args)	

def loop(nloop,nsec):
	print 'start loop',nloop,'at:',ctime()
	sleep(nsec)
	print 'loop',nloop,'done at:',ctime()

def main():
	print 'starting at:',ctime()
	threads = []
	nloops = range(len(loops))
	
	for i in nloops:
		t = threading.Thread(
			#target is a callable obj to be invoked by the run()
			target = ThreadFunc(loop,(i,loops[i]))#callable obj
					,loop.__name__)#name is the thread name可选
			#transfer a obj to Thread class
		threads.append(t)

	for i in nloops:
		threads[i].start()
	
	for i in nloops:
		threads[i].join()

	print 'all DONE at:',ctime()

if __name__ =='__main__':
	main()
