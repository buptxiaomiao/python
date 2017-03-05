#########################################################################
#-*- coding:utf-8 -*-
# File Name: userpw.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月19日 星期六 16时10分42秒
#########################################################################
#!/usr/bin/env python2.7

db = {}

def newuser():
	prompt = 'Login sign:'
	while True:
		name = raw_input(prompt).strip()
		if name in db:
			prompt = 'Name taken,try again.Login sign:'
		else:
			break
	pwd = raw_input('passwd:')
	db[name] = pwd
def olduser():
	while True:
		try:
			name = raw_input('Login:').strip()
			pwd = raw_input('passwd:')
		except(EOFError,KeyboardInterrupt):
			print 'Invalid.Try again.'
		else:
			break
	passwd = db.get(name)#######get value which key is name.
	if passwd == pwd:
		print 'Welcome back',name
	else:
		print 'Login incorrect.'
def showmenu():
	prompt='''
(N)ew User Login.
(O)ld User Login.
(Q)uit.

Enter choice: '''
	done = False
	while not done:
		chosen = False
		while not chosen:
			try:
				choice = raw_input(prompt).strip()[0].lower()
			except(EOFError,KeyboardInterrupt,IndexError):
				choice = 'q'
			print 'You picked:[%s]'%choice
			if choice not in 'noq':
				print 'Invalid option,try again.'
			else:
				chosen = True
		if choice == 'q':
			done = True
		if choice == 'n':
			newuser()
		if choice == 'o':
			olduser()
			done = True	
if __name__ == '__main__':
	showmenu()
