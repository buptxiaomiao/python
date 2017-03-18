#########################################################################
#-*- coding:utf-8 -*-
# File Name: minute_convert.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月18日 星期五 13时00分51秒
#########################################################################
#!/usr/bin/env python2.7

def minute_convert():
	while True:
		try:
			num_str=raw_input('Enter a minute in int number:').strip()
			if num_str.isdigit():
				num = int(num_str)
			else:
				print 'Input_str is not a number.Try again.'	
				continue
		except (KeyboardInterrupt,ValueError,EOFError):
			print 'Invalid Value,try again.'
		else:
			break				
	hours = num // 60
	minutes = num - hours*60
	return {'hours':hours,'minutes':minutes}
print minute_convert()
