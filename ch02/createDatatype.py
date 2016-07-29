import numpy as num

type1 = num.dtype(float)
print("num.dtype(float) : ", type1)

type2 = num.dtype('f')
print("num.dtype('f') : ", type2)

type3 = num.dtype('d')
print("num.dtype('d') : ", type3)

type4 = num.dtype('f8')
print("num.dtype('f8') : ", type4)

print("num.sctypeDict.keys() : ", num.sctypeDict.keys())
