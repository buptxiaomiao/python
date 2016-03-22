#########################################################################
#-*- coding:utf-8 -*-
# File Name: rodcons.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月22日 星期二 21时36分33秒
#########################################################################
#!/usr/bin/env python2.7

from random import randint
from time import sleep
from Queue import Queue
#Queue 供多线程使用的队列
#SocketServer 具有线程控制
from myThread import MyThread

def addQ(queue):
	print 'producing object for Q...',
	queue.put('xxx,1')#put 'xxx' in the queue
	print 'size now',queue.qsize()#return the size of Queue obj


def subQ(queue):
	val = queue.get(1)#getout the queue
	print 'consumed object from Q...size now',queue.qsize()

def produce(queue,loops):
	for i in range(loops):
		addQ(queue)
		sleep(randint(1,3))#produce_eachtime < consume_eachtime

def consume(queue,loops):
	for i in range(loops):
		subQ(queue)
		sleep(randint(2,5))

funcs = [produce,consume]
nfuncs = range(len(funcs))

def main():
	nloops = randint(2,5)#produce_times equals consume_times
	q = Queue(32)
	threads = []
	for i in nfuncs:
		t = MyThread(funcs[i],(q,nloops),funcs[i].__name__)	
		threads.append(t)

	for i in nfuncs:
		threads[i].start()

	for i in nfuncs:
		threads[i].join()

	print 'add Done.'

if __name__ == '__main__':
	main()
