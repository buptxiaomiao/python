##################################################
#-*- coding:utf-8 -*-
# FileName: recursion.py
# Author: buptxiaomiao
# Mail: buptwjh@outlook.com
# Created Time: 2017年03月08日 星期三 16时22分09秒
################################################## 
#!/usr/bin/python2.7
import random

def factorial(n):
    if n == 1 or n == 0:#if 问题简单，直接求解
        return 1
    else:               #else 分解成小问题
        return n * factorial(n-1)
print factorial(4)

count = 0
def hanoi(n, A, B, C):
    global count
    if n ==1:
        print 'Move', n, 'from', A, 'to', C
    else:
        hanoi(n - 1, A, C, B)
        print 'Move', n, 'from', A, 'to', C
        count += 1
        hanoi(n-1, B, A, C)
hanoi(6,'left','mid','right')
print count

def parking(low, high):
    if high - low < 1:
        return 0
    else:
        x = random.uniform(low, high - 1)
        return parking(low, x) + 1 + parking(x + 1, high)
s = 0
for i in range(10000):#模拟1000次
    s += parking(0, 5)#一共停车的辆数
print s / 10000.
print s / 10000. / 5 

