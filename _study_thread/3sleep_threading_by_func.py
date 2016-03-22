#########################################################################
#-*- coding:utf-8 -*-
# File Name: mtsleep3.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月22日 星期二 19时05分13秒
#########################################################################
#!/usr/bin/env python2.7

import threading 
from time import sleep,ctime

sec_l = [4,2]

def loop(n,sec):
	print 'start loop',n,'at:',ctime()
	sleep(sec)
	print 'loop',n,'done at:',ctime()
def main():
	print 'starting at:',ctime()
	threads = []
	nloops = range(len(sec_l))

	for i in nloops:
		#Thread is a class in threading.(like start_new_thread())
		t = threading.Thread(target=loop,args=(i,sec_l[i]))
#Threads dont excute right.
		threads.append(t)#add threads

	for i in nloops:
		threads[i].start()
#threads excute now

	for i in nloops:
		threads[i].join()
#waiting for threads excuted.
	
	print 'all DONE at:',ctime()

if __name__ == '__main__':
	main()

