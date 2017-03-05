##################################################
#-*- coding:utf-8 -*-
# FileName: list_comprehensions&generator.py
# Author: buptxiaomiao
# Mail: buptwjh@outlook.com
# Created Time: 2017年03月05日 星期日 21时34分43秒
################################################## 
#!/usr/bin/python2.7

######################################
#------------List Comprehensions------
######################################
#P205 [exep for iter_var in iterable if cond_exep)  
print [x ** 2 for x in range(4)]

print [(x+1,y+1) for x in range(3) for y in range(5)]

f = open("qqq.txt",'r')
print len([word for line in f for word in line.split()])
f.seek(0)
print sum([len(word) for line in f for word in line.split()])
f.close()
 

######################################
#-------------generator--------------
#####################################
#寻找文件最长的行
#----v1--
def func1():
	f = open('qqq.txt','r')
	longest = 0
	while True :
		linelen = len(f.readline().strip())
		if not linelen: break
		if linelen > longest :
			longest = linelen
	f.close()
	return longest

#----v2--
def func2():
	f = open('qqq.txt','r')
	longest = 0
	allLines = f.readlines()
	f.close()
	for line in allLines:
		linelen = len(line.strip())
		if linelen > longest :
			longest = linelen
	return longest
	
#-----v3--
def func3():
	f = open('qqq.txt','r')
	longest = 0
	allLines = [x.strip() for x in f]
	f.close()
	for line in allLines:
		linelen = len(line)
		if linelen > longest:
			longest = linelen
	return longest
#------v4--
def func4():
	f = open('qqq.txt','r')
	longest = max(len(x.strip())  for x in f)
	f.close()
	return longest

#------v5--
def func5():
	return max(len(x.strip())  for x in open('qqq.txt'))
	
print func1()
print func2()
print func3()
print func4()
print func5()
