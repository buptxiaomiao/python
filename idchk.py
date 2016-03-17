#########################################################################
#-*- coding:utf-8 -*-
# File Name: idchk.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月18日 星期五 01时56分01秒
#########################################################################
#!/usr/bin/env python2.7
import string
al = string.letters+'_'
nums = string.digits

print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long'
myinput = raw_input('Identifier to test?')

if len(myinput)>1:			#do not forget ::::::::
	if myinput[0] not in al:
		print '''invalid:first symbol must be 
				alphabetic'''
	else:
		for otherchar in myinput[1:]:
			if otherchar not in al+nums:
				print '''invalid: remaing
				symbols must be alphanumberic'''
				break
		else:#excute when for is excute without break
			print 'okay as an identifier'
