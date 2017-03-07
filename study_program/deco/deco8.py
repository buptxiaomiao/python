##################################################
#-*- coding:utf-8 -*-
# FileName: deco8.py
# Author: buptxiaomiao
# Mail: buptwjh@outlook.com
# Created Time: 2017年03月07日 星期二 17时35分17秒
################################################## 
#!/usr/bin/python2.7
import time

def deco_1(func):
    print "enter into deco_1"#4
    def wrapper(a,b):
        print "enter into deco_1_wrapper"#5
        func(a,b)#6 deco_2.wrapper()
    print "111111"
    return wrapper

def deco_2(func):
    print "enter into deco_2"#1
    def wrapper(a,b):
        print "enter into deco_2_wrapper"#7
        func(a,b)#8 addfunc(a,b)
    print "2222222"#2
    return wrapper#3

@deco_1
@deco_2
def addfunc(a,b):
    print "result is %d"%(a+b)
#addfunc = deco_1(deco_2(addfunc(a,b)))

addfunc(2,6)
