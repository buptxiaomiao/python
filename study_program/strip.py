#########################################################################
#-*- coding:utf-8 -*-
# File Name: strip.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月18日 星期五 12时12分34秒
#########################################################################
#!/usr/bin/env python2.7

#coding a func like strip()
def strip_space():
    s_in = raw_input('Enter a string:')
    s_tmp=''
    s_out=''
    if s_in[0] is not ' ':
        s_tmp = s_in
    else:
        for i,t in enumerate(s_in):
            if t is not ' ':
                s_tmp = s_in[i:]
                break
	
    if s_tmp[-1] is not ' ':
        s_out = s_tmp
    else:
        for i in range(len(s_tmp)):
            if s_tmp[-1-i] is not ' ':
                s_out = s_tmp[:-1-i+1]
                break
    print "Your input:   ",s_in
    print "after strip():",s_out
    return s_out

if __name__ == '__main__':
	strip_space()
