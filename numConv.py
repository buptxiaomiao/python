#########################################################################
#-*- coding:utf-8 -*-
# File Name: numConv.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月21日 星期一 21时01分18秒
#########################################################################
#!/usr/bin/env python2.7

def convert(func,seq):
	'conv.sequence of numbers to same type.'
	return [func(each) for each in seq]
convert.x = 1
convert.y = 2
seq = (123,45.67,-6.2e8,99999999L)
print convert(int,seq)
print convert(float,seq)
print convert(long,seq)
print convert.x+convert.y
