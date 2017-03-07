##################################################
#-*- coding:utf-8 -*-
# FileName: deco1.py
# Author: buptxiaomiao
# Mail: buptwjh@outlook.com
# Created Time: 2017年03月07日 星期二 16时55分18秒
################################################## 
#!/usr/bin/python2.7
import time

def deco(func):
    starttime = time.time()  
    func()
    endtime = time.time()
    ms = (endtime - starttime) * 1000
    print "-> elapsed time: %f ms"%ms

def myfunc():
    print "start myfunc()"
    print "...",
    time.sleep(0.6)
    print "  ..."
    print "end myfunc()"

deco(myfunc)
myfunc
