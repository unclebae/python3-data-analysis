# _*_ coding: utf-8 _*_
import numpy as num

# make 3 * 3 narray
a = num.arange(9).reshape(3, 3)

print("num.arange(9).reshape(3, 3) : ", a)

# horizontal Split
print("num.hsplit(a, 3) : ", num.hsplit(a, 3)) 

# same horizontal split using split and axis
print("num.split(a, 3, axis=1) : ", num.split(a, 3, axis=1))

