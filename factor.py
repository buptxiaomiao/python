#########################################################################
#-*- coding:utf-8 -*-
# File Name: factor.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月18日 星期五 11时34分42秒
#########################################################################
#!/usr/bin/env python2.7

def factor():
	while True:
		try:
			num_str = raw_input('Enter an int:').strip()
			if num_str.isdigit():
				num = int(num_str) 
			else:
				print 'Not a number.Try again.'
				continue
		except(KeyboardInterrupt,EOFError,ValueError):
			print 'Invalid input,try again.'
			if raw_input(''''q' to quit:''')=='q':
				exit(0)
		else:
			print 'You picked ',num
			break
	f = range(1,num//2+1)
	print 'Before:',f
	fac_list = []	
	for i,t in enumerate(f):
		if num % t == 0:
			fac_list.append(t)
	fac_list.append(num)
	print 'After: ',fac_list
if __name__ == '__main__':
	factor()
