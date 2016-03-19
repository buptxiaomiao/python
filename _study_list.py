#########################################################################
#-*- coding:utf-8 -*-
# File Name: list_study.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月18日 星期五 10时39分19秒
#########################################################################
#!/usr/bin/env python2.7

l=[0,1,2,3,4,5]
#del l[1] or l.remove(obj)---return None
print l
del l[-1]
print 'del l[-1]',l
print 'l.remove(2)',l.remove(2),l


t=(0,1,2,3,4,5)
t=(1,)#define a single-item tuple
# tuple is not allowed item deletion.
print 'del t[-1] is not allowed.'
del t #tuple can be -------del t

#list.fuc()
print 'l.append(obj)',l.append(1),l
print 'l.count(obj)',l.count(1)
print 'l.insert(index,obj)',l.insert(-1,6),l
print 'l.pop(index=-1)',l.pop(),l
print 'l.reverse()',l.reverse(),l
print 'sum(l) =',sum(l)
#sum(),len(),sorted(),reversed(),enumerate(),zip(l1,l2),list(),tuple()

print sum(tuple(l))


