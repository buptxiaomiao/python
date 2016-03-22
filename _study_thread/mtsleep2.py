#########################################################################
#-*- coding:utf-8 -*-
# File Name: mtsleep2.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月22日 星期二 18时39分29秒
#########################################################################
#!/usr/bin/env python2.7

import thread
from time import ctime,sleep

sec_l = [4,2]

def loop(n,sec,lock):
	print 'start loop',n,'at:',ctime()
	sleep(sec)
	print 'loop',n,'done at:',ctime()
	lock.release()#释放锁#3
def main():
	print 'starting at:',ctime()
	locks = []
	nloops = range(len(sec_l))

	for i in nloops:
		lock = thread.allocate_lock()#1获取锁对象
		lock.acquire()#获取锁
					  #获取锁要花些时间
		locks.append(lock)

	for i in nloops:
		thread.start_new_thread(loop,(i,sec_l[i],locks[i]))#分配线程#2
	
	for i in nloops:
		while locks[i].locked():
			pass#检查所有锁是否都关掉，不是则什么都不做再检查
	print 'all done at:',ctime()

if __name__ == '__main__':
	main()
