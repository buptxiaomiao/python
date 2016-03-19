#########################################################################
#-*- coding:utf-8 -*-
# File Name: _study_dict.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月19日 星期六 14时09分00秒
#########################################################################
#!/usr/bin/env python2.7

import copy
#zip()
a=(1,2,3)
b=['yi','er']
print zip(a,b)
#dict()
adict = dict(zip(a,b))
print adict
fdict = dict(  (['x','1'],['y','2'])  )#1,2 is strings.
print fdict	
ddict = dict(x=1,y=2)#x,y become a string.
					 #1,2 is int.
print ddict
ddict = fdict.copy()#dict.copy() is faster than = 
print ddict
print '''ddict is {'x':'1','y':'2'}'''
print 'len(ddict) is',len(ddict)
print 'ddict.keys() is',ddict.keys()
print 'ddict.values() is',ddict.values()
print ddict.__contains__('x')
print ddict.fromkeys(adict)#value is None.
print ddict.fromkeys(adict,1)
print "*******************************"
print adict,ddict
print ddict.update(adict)
print ddict
print int(ddict.get('x'))+2
print '*********************************8'
print ddict.items()
ddict.pop('x')
print ddict
print ddict.viewkeys()
print ddict.viewitems()
