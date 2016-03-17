#!/usr/bin/env python2.7

from random import randint
from random import uniform
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
#random
	#randint(num1,num2)--return a random int
print 'randint(1,10) is',randint(1,10)
	#randrange(num1,num2)
	#uniform(num1,num2)--return a random float
print 'unifoem(1,10) is',uniform(1,10)
	#choice()		   --return a random list
choice = list(1,2,3,4,5)
print 'choice(list) is',choice(list)


