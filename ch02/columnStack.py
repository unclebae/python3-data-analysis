# _*_ coding: utf-8 _*_
import numpy as num

oned = num.arange(2)

print ("num.arange(2) : ", oned)

twice_oned = 2 * oned

print ("2 * num.arange(2) : ", twice_oned)

columnStack = num.column_stack( (oned, twice_oned) )
print ("num.column_stack( (oned, twice_oned) ) : ", columnStack)
