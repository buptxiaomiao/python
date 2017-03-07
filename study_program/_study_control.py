#########################################################################
#-*- coding:utf-8 -*-
# File Name: _study_control.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月19日 星期六 19时54分16秒
#########################################################################
#!/usr/bin/env python2.7

ddict=dict(zip(('x','y','z'),(1,2,3)))
print ddict
for i in ddict.itervalues():
	print i,
for i in ddict.iteritems():
	print i,
for i in ddict.iterkeys():
	print i,


#获取文件最大的行
#
#f = open ('./qqq.txt','r')
#longest = max(len(x.strip()) for x in f)# 生成器
#return longest
