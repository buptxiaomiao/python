##################################################
#-*- coding:utf-8 -*-
# FileName: deco5.py
# Author: buptxiaomiao
# Mail: buptwjh@outlook.com
# Created Time: 2017年03月07日 星期二 17时19分40秒
################################################## 
#!/usr/bin/python2.7
import time 

def deco(arg = True):
    if arg:
        def _deco(func):
            def wrapper(*argv,**argc):
                starttime = time.time()
                func(*argv,**argc)
                endtime = time.time()
                ms = (endtime - starttime) * 1000
                print "->elapsed time: %f ms"%ms
            return wrapper
    else:
        def _deco(func):
            return func
    return _deco

@deco(False)
def myfunc():
    print "start myfunc()"
    time.sleep(0.6)
    print "end myfunc()"


@deco(True)
def addfunc(a,b):
    print "start addfunc()"
    time.sleep(0.6)
    print "result is ",a+b
    print "end addfunc()"

print "myfunc is",myfunc.__name__
myfunc()
print
print "addfunc is",addfunc.__name__
addfunc(2,5)


