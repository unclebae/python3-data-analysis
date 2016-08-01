# _*_ coding: utf-8 _*_
import numpy as num

a = num.arange(9).reshape(3, 3)
print ("num.arange(9).reshape(3, 3) : ", a)

b = 2 * a
print ("b = 2 * a : ", b)

# column_stack 
print ("column_stack of 2D : column_stack( (a, b) ) : ", num.column_stack( (a, b) ) )

print ("compare column_stack of 2D and hstack : ", num.column_stack( (a, b) ) == num.hstack( (a, b) ) )
