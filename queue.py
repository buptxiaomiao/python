#########################################################################
#-*- coding:utf-8 -*-
# File Name: queue.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月18日 星期五 11时02分30秒
#########################################################################
#!/usr/bin/env python2.7

queue=[]
def enQ():
	queue.append(raw_input('Enter new string:').strip())
def deQ():
	if len(queue) == 0:
		print 'Can not pop from empty queue.'
	else:
		print 'Removed {',queue.pop(0),'}'
def viewQ():
	print queue

cmds = {'e':enQ,'d':deQ,'v':viewQ}

def showmenu():
	pr='''
(E)nqueue.
(D)equeue.
(V)iewqueue.
(Q)uit.

Enter choice:'''
	while True:
		while True:
			try:
				choice = raw_input(pr).strip()[0].lower()
			except (EOFError,KeyboardInterrupt,IndexError):
				choice = 'q'
			print "You picked [%s]."%choice
			if choice not in 'edvq':
				print "Invalid Input,try again."
			else:
				break
		if choice == 'q':
			break
		cmds[choice]()
if __name__ == '__main__':
	showmenu()
