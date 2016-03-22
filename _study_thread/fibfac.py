#########################################################################
#-*- coding:utf-8 -*-
# File Name: fibfac.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月23日 星期三 04时03分25秒
#########################################################################
#!/usr/bin/env python2.7
from  myThread import MyThread
from time import ctime ,sleep

def fib(x):
	sleep(0.005)
	return 1 if x<2 else (fib(x-2)+fib(x-1))
def fac(x):
	sleep(0.1)
	return 1 if x<2 else (x*fac(x-1))
def sum_(x):
	sleep(0.1)
	return 1 if x<2 else (x+sum_(x-1))
funcs = (fib,fac,sum_)
n = 12
def main():
	nfuncs = range(len(funcs))
	print '***************SINGLE THREAD*****************'
	for i in nfuncs:
		print 'starting',funcs[i].__name__,'-------at:',ctime()
		print funcs[i](n)
		print 'done',funcs[i].__name__,'at',ctime()

	print '***************MULTIPLE THREAD****************'
	threads = []
	for i in nfuncs:
		t = MyThread(funcs[i],(n,),funcs[i].__name__)
		threads.append(t)

	for i in nfuncs:
		threads[i].start()

	for i in nfuncs:
		threads[i].join()
		print threads[i].getResult()
	
	print 'all DONE at:',ctime()

if __name__ == '__main__':
	main()
