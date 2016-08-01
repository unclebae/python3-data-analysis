# _*_ coding: utf-8 _*_
import numpy as num

a = num.arange(9).reshape(3, 3)

print("num.arange(9).reshape(3, 3) : ", a)

# vertical split using vsplit
print("num.vsplit(a, 3) : ", num.vsplit(a, 3) )

# vertical split using split with axis=0
print("num.split(a , 3, axis=0) : ", num.split(a, 3, axis=0))
