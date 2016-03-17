#########################################################################
#-*- coding: utf-8 -*-
# File Name: slice.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月18日 星期五 01时05分28秒'''
#########################################################################
#!/usr/bin/env python2.7
l = (0,1,2,3,4,5)
m = [0,1,6,3,4,5]

print 'l is',l
print 'm is',m
print 'l[start:ending:step=1]'
print 'l[0:3] or l[:3] is',l[0:3]
print 'l[::-1] is',l[::-1]
n=list(l)
print str(l)#tuple
print str(n)#list
print 'length of l is',len(l)
print 'sorted(m) is',sorted(m)
print 'sum of l is',sum(l)


#zip(iter1,iter2,iter3)--------return a list
print "zip(l,m,n) is",zip(l,m,n)
#enumerate()
for i,t in enumerate(m):		#do not forget::::::::
	print i,t
#isinstance()
print 'isinstance(1,int) is',isinstance(1,int)
