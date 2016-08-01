# _*_ coding:utf-8 _*_
import numpy as num

# make 3 * 3 * 3 array
a = num.arange(27).reshape(3, 3, 3)

print("num.arange(27).reshape(3, 3, 3) : ", a)

# depth-wise splitting
print("num.dsplit(a, 3) : ", num.dsplit(a, 3) )

