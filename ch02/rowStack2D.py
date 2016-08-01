# _*_ coding: utf-8 _*_
import numpy as num

a = num.arange(9).reshape(3, 3)
print ("num.arange(9).reshape(3, 3) : ", a)

b = 2 * a
print ("b = 2 * a : ", b)

# row_stack 
print ("row_stack of 2D : row_stack( (a, b) ) : ", num.row_stack( (a, b) ) )

print ("compare row_stack of 2D and vstack : ", num.row_stack( (a, b) ) == num.vstack( (a, b) ) )
