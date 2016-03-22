#########################################################################
#-*- coding:utf-8 -*-
# File Name: mtsleep1.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月22日 星期二 18时31分11秒
#########################################################################
#!/usr/bin/env python2.7

import thread
from time import sleep,ctime
def loop0():
	print 'start loop0 at:	',ctime()
	sleep(4)
	print 'loop0 done at:	',ctime()
def loop1():
	print 'start loop1 at:		',ctime()
	sleep(2)
	print 'loop1 done at:		',ctime()

def main():
	print 'starting at :',ctime()
	thread.start_new_thread(loop0,())#start_new_thread(func,argument)
									#必须两个参数，没有()
	thread.start_new_thread(loop1,())
	sleep(5)#让sleep（）做同步不好
			#主线程运行完就被停止
	print 'all done at :',ctime()

if __name__ == '__main__':
	main()
