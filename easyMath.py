#########################################################################
#-*- coding:utf-8 -*-
# File Name: easyMath.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月21日 星期一 20时42分18秒
#########################################################################
#!/usr/bin/env python2.7

from operator import add , sub
from random import randint,choice

opr_dict = {'+':add,'-':sub}
MAXTRIES = 2
def calnum():
	opra = choice('+-')
	nums = [randint(1,10) for i in range(2)]
	nums.sort(reverse = True)#reverse=True make 321
							 #default ->123
	ans = opr_dict[opra](*nums)#when add(*tuple) add(*nums)
	pr = '%d %s %d ='%(nums[0],opra,nums[1])#prompt->提示符
	wrong_times = 0
	while True:
		try:
			if int(raw_input(pr)) == ans:#correct.
				print 'correct'
				break
			if wrong_times == MAXTRIES:#wrong 2 times
				print 'answer\n %s %d'%(pr,ans)
			else:#when wrong
				print 'incorrect...try again.'
				wrong_times+=1
		except (KeyboardInterrupt,EOFError,ValueError):
			print 'invalid input...try again.'
def main():
	while True:
		calnum()
		try:
			option = raw_input('Again?[y]').lower()
			if option and option[0] == 'n':
				break
		except(KeyboardInterrupt,EOFError):
			break
if __name__ == '__main__':
	main()

