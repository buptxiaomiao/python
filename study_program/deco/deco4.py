##################################################
#-*- coding:utf-8 -*-
# FileName: deco4.py
# Author: buptxiaomiao
# Mail: buptwjh@outlook.com
# Created Time: 2017年03月07日 星期二 17时11分05秒
################################################## 
#!/usr/bin/python2.7
import time

def deco(func):
    def wrapper(a,b):
        starttime = time.time()
        func(a,b)
        endtime = time.time()
        ms = (endtime - starttime) * 1000
        print "->elapsed time: %f ms"%ms
    return wrapper

@deco 
def myfunc(a,b):
    print "start myfunc(%d + %d)"%(a,b)
    time.sleep(0.6)
    print "result of a + b is ",a+b
    print "end myfunc(%d + %d)"%(a,b)

myfunc(1,2)
