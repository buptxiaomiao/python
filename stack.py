#########################################################################
#-*- coding:utf-8 -*-
# File Name: stack.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月18日 星期五 02时15分34秒
#########################################################################
#!/usr/bin/env python2.7

stack=[]
def pushit():
	stack.append(raw_input('Enter New string: ').strip())
def popit():
	if len(stack) == 0:			#do not forget ::::::::::::
		print 'Can not pop from empty stack!'
	else:
		print 'removed[',`stack.pop()`,']'
def viewstack():
	print stack
cmds={'u':pushit,'o':popit,'v':viewstack}
def showmenu():
	pr='''
p(U)sh
p(O)p
(V)iew
(Q)uit

Enter choice:'''
	while True:
		while True:
			try:
				choice = raw_input(pr).strip()[0].lower()
			except (EOFError,KeyboardInterrupt,IndexError):
				choice = 'q'
			print '\nYou picked:[%s]'%choice
			if choice not in 'uovq':
				print 'Invalid option,try again.'
			else:
				break
		if choice == 'q':
			break
		cmds[choice]()

if __name__=='__main__':
	showmenu()
