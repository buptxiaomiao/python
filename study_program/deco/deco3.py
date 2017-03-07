##################################################
#-*- coding:utf-8 -*-
# FileName: deco3.py
# Author: buptxiaomiao
# Mail: buptwjh@outlook.com
# Created Time: 2017年03月07日 星期二 17时06分54秒
################################################## 
#!/usr/bin/python2.7
import time

def deco(func):
    def wrapper():
        starttime = time.time()
        func()
        endtime = time.time()
        ms = (endtime - starttime) * 1000
        print "->elapsed time: %f ms"%ms
    return wrapper

@deco
def myfunc():
    print "start myfunc()"
    time.sleep(0.6)
    print "end myfunc()"

myfunc()
