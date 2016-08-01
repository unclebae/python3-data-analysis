# _*_ coding: utf-8 _*_
import numpy as num

a = num.arange(9).reshape(3, 3)
print ("num.arange(9).reshape(3, 3) : ", a)

b = 2 * a
print ("b = 2 * a : ", b)

# concatenate + axis=0 = vstack()
print ("concatenate( (a, b), axisx=0) : ", num.concatenate( (a, b), axis=0 ) )
print ("concatenate( (a, b), axisx=1) : ", num.concatenate( (a, b), axis=1 ) )
