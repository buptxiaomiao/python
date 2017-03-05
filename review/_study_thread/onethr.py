#########################################################################
#-*- coding:utf-8 -*-
# File Name: onethr.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月22日 星期二 17时03分28秒
#########################################################################
#!/usr/bin/env python2.7

from time import sleep,ctime

def loop0():
	print 'start loop0 at:	',ctime()
	sleep(4)
	print 'stop loop0 at:	',ctime(),'\n'

def loop1():
	print 'start loop1 at:	',ctime()
	sleep(2)
	print 'stop loop1 at:	',ctime(),'\n'

def main():
	print 'startint at:	',ctime(),'\n'
	loop0()
	loop1()
	print 'stopping at:	',ctime()

if __name__  == '__main__':
	main()
	
