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
			num = int(num_str) 
		except(KeyboardInterrupt,EOFError,ValueError):
			print 'Invalid input,try again1.'
			continue
		else:
			if isinstance(num,int):
				print 'You picked ',num
				break
			else:
				print 'Invalid input,try agian2.'
				continue
	f = range(1,num//2+1)
	print 'Before:',f

	fac_list = []	
	for i,t in enumerate(f):
		if num % f[i] != 0:
			fac_list.append(t)

	print fac_list
if __name__ == '__main__':
	factor()
