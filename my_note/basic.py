#!/usr/bin/env python2.7

#print
mystring='Hello world!'
print 'mystring is %s '%mystring
print mystring*2


#open file
f = open('qqq.txt','r')
for eachline in f:
	print eachline,
f.close()


#raw_input
user=raw_input('Enter login name: ')
print 'Your login is:',user
print 'Your login is: %s '%user

#function
def foo():						#Don't forget :::::::::::::::::
	"This is a doc string."#help(foo)
	return True
print foo()
help(foo)



#+ - * / // **
#\go on
#and or not
#n-- n++ xxxxxxxxx
#help(raw_input)
#list tuple dict
adict={'host':'earth'}
print adict,adict['host']

count = 0
while count<3:					#Don't forget :::::::::::::::::
	print 'loop #%d'%count
	count+=1
#元组做函数参数时func(*tuple)
#字典做函数参数时func(**dict)


#when import,__name__ is port_name
#when excute,__name__ is __main__


