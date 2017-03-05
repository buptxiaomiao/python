#########################################################################
#-*- coding:utf-8 -*-
# File Name: idchk.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月18日 星期五 01时56分01秒
#########################################################################
#!/usr/bin/env python2.7
import string
import keyword

alpha = string.letters+'_'
nums = string.digits
keys=keyword.kwlist

print 'Welcome to the Identifier Checker v1.1'
print ' Identifier must be at least 1 chars long'
print ' Spaces in start or endding will be ignored'
print ' First char must be char.'
myinput = raw_input('Identifier to test?\n').strip()

if len(myinput) >= 1:			#do not forget ::::::::
	if myinput[0] not in alpha:
		print '''Invalid:first symbol must be alphabetic'''
	else:
		for otherchar in myinput[1:]:
			if otherchar not in alpha+nums:
				print '''Invalid: remaing symbols must be alphanumberic'''
				break
		else:#excute when for is excute without break
			if myinput not in keyword.kwlist:
				print '%s is okay as an identifier'%myinput
			else :
				print 'Sorry ,%s'%myinput,'is an keyword.'
