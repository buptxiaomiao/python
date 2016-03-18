#########################################################################
#-*- coding:utf-8 -*-
# File Name: strip.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月18日 星期五 12时12分34秒
#########################################################################
#!/usr/bin/env python2.7

#coding a func like strip()
def strip_space():
	s_in = raw_input('Enter a string:')
	s_tmp=''
	s_out=''
	for i,t in enumerate(s_in):
		if t is not ' ':
			s_tmp = s_in[i:-1]+s_in[len(s_in)-1]
			break
	
	for i,t in enumerate(reversed(list(s_tmp))):
		if t is not ' ':
			s_out = s_tmp[i:-1]+s_tmp[len(s_tmp)-1]
			break
	list(s_out).reverse()
	print "Your input:   ",s_in
	print "after strip():",str(s_out)
	return s_out

if __name__ == '__main__':
	strip_space()
