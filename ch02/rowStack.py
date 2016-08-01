# _*_ coding: utf-8 _*_
import numpy as num

oned = num.arange(2)

print ("num.arange(2) : ", oned)

twice_oned = 2 * oned

print ("2 * num.arange(2) : ", twice_oned)

rowStack = num.row_stack( (oned, twice_oned) )
print ("num.row_stack( (oned, twice_oned) ) : ", rowStack)
