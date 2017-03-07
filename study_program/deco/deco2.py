##################################################
#-*- coding:utf-8 -*-
# FileName: deco2.py
# Author: buptxiaomiao
# Mail: buptwjh@outlook.com
# Created Time: 2017年03月07日 星期二 17时01分07秒
################################################## 
#!/usr/bin/python2.7
import time

def deco(func):
    def wrapper():
        starttime = time.time()
        func()
        endtime = time.time()
        ms = (endtime - starttime) * 1000
        print "->elapsed time: %f ms " %ms
    return wrapper

def myfunc():
    print "start myfunc()"
    time.sleep(0.6)
    print "end myfunc()"
    
print "myfunc is",myfunc.__name__
myfunc = deco(myfunc)
print "myfunc is",myfunc.__name__

print 
myfunc()
