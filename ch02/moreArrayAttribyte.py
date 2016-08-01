# _*_ coding: utf-8 _*_
import numpy as num

a = num.arange(24).reshape(2, 12)
print("num.arange(24).reshape(2, 12) : ", a)

print("a.ndim : ", a.ndim)

print("a.size : ", a.size)

print("a.itemsize : ", a.itemsize)

print("a.nbytes : ", a.nbytes)

print("a.size * a.itemsize : ", (a.size * a.itemsize))

print("num.resize(6, 4) : ", num.resize(6, 4))

print("a.T : ", a.T)

print("a.ndim after transform T : ", a.ndim)

print("a.T after transform T :", a.T)

print("num.array([1.j + 1, 2.j + 3]) : ", num.array([1.j + 1, 2.j + 3]))

print("a.real : ", a.real)
