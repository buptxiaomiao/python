#########################################################################
#-*- coding:utf-8 -*-
# File Name: 5sleep_threading_by_inheriting_class.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月23日 星期三 03时42分20秒
#########################################################################
#!/usr/bin/env python2.7

import threading
from time import ctime,sleep

loops=[4,2]
class MyThread(threading.Thread):#parent calss
	def __init__(self,func,args,name=''):
		threading.Thread.__init__(self)
		self.func = func
		self.args = args
		self.name = name
	def run(self):#invoked by run
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
		t = MyThread(loop,(i,loops[i]),loop.__name__)
		threads.append(t)
	for i in nloops:
	#thread.start() do prepare for the thread.----->run()
		threads[i].start()#start() invoke run()
	for i in nloops:
		threads[i].join()#make main() waiting for threads.
	print 'all DONE at:',ctime()

if __name__=='__main__':
	main()
