#!/usr/bin/env python2.7

from random import randint
from random import uniform
from random import random
from random import choice
_string = 'xiaomiao'
print str(_string)
print repr(_string)
print `_string`#*****************for else functions.

print type(42)
print type(' ')
print type({})
print type(type)
print type(1+0j)
print type(())
print type([])

#//---equal / in c++
#for complex:
	#num.real
	#num.imag
	#num.conjugate()

#for num
	#abs(num)
	#coerce(num1,num2)
print 'coerce(5.1,2)is',coerce(5.1,2)
	#divmod(num1,num2)
print 'divmod(5,2)is',divmod(5,2)
	#pow(num1,num2)-----**
	#round(float_num)
print 'round(1.1) is',round(1.1)

#****************************************************
#random_module
	#randint(num1,num2)--return a random int
print 'randint(1,10) is',randint(1,10)
	#randrange(num1,num2)
	#uniform(num1,num2)--return a random float
print 'unifoem(1,10) is',uniform(1,10)
	#random()
print 'random() is',random()
	#choice()		   --return a random list
l = (0,1,2,3,4,5)
m = [0,1,2,3,4,5]
print 'l is',l
print 'm is',m
print 'choice(l) is',choice(l)
print 'choice(m) is',choice(m)

		#n=l+m
print 'l[start:ending:step=1]'
print 'l[0:3] or l[:3] is',l[0:3]
print 'l[::-1] is',l[::-1]

