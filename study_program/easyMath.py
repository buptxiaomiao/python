#########################################################################
#-*- coding:utf-8 -*-
# File Name: easyMath.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月21日 星期一 20时42分18秒
#########################################################################
#!/usr/bin/env python2.7

#P270

from operator import add , sub
from random import randint,choice

opr_dict = {'+':add,'-':sub}
MAXTRIES = 2
def calnum():
	opra = choice('+-')
	nums = [randint(1,10) for i in range(2)]

#>>>>>>>>>>>>列表解析P205
#[exep for iter_var in iterable if cond_exep] exep应用于序列的每个成员
#[x ** 2 for x in range(4)]  => [0,1,4,9]
#生成器(exep for iter_var in iterable if cond_exep)

	nums.sort(reverse = True)#reverse=True make 321
							 #default ->123
	ans = opr_dict[opra](*nums)
#>>>>>>>>元组做函数参数时func(*tuple)
#>>>>>>>>字典做函数参数时func(**dict)
	pr = '%d %s %d ='%(nums[0],opra,nums[1])#prompt->提示符
	wrong_times = 0
	while True:
		try:
			if int(raw_input(pr)) == ans:#correct.
				print 'correct'
				break
			if wrong_times == MAXTRIES:#wrong 2 times
				print 'answer\n %s %d'%(pr,ans)
				break
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

