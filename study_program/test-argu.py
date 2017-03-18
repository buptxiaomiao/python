#########################################################################
#-*- coding:utf-8 -*-
# File Name: test-argu.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月21日 星期一 21时27分47秒
#########################################################################
#!/usr/bin/env python2.7

def testit(func,*nk,**k):
	try:
		retval = func(*nk,**k)#调用
		result = (True,retval)#结果
	except Exception,diag:
		result = (False,str(diag))#异常
	return result

def test():
	funcs = (int ,long ,float)
	vals = (1234,12.34,'1234','12.34')
	for eachf in funcs:
		print '_'*20
		for eachv in vals:
			retval = testit(eachf,eachv)#每次只调用了一个元素
			if retval[0]:#result 返回，调用True,False.
				print '%s(%s)='%(eachf.__name__,eachv),retval[1]#结果
			else:
				print '%s(%s)=FAILED'%(eachf.__name__,eachv),retval[1]#异
if __name__ == '__main__':
	test()
