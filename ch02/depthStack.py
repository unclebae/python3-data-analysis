# _*_ coding: utf-8 _*_
import numpy as num

a = num.arange(9).reshape(3, 3)
print ("num.arange(9).reshape(3, 3) : ", a)

b = 2 * a
print ("b = 2 * a : ", b)

# depth stacking 
print ("dstack( (a, b) ) : ", num.dstack( (a, b) ) )
