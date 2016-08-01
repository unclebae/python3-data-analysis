# _*_ coding: utf-8 _*_
import numpy as num

a = num.array([ 1. + 1.j, 3. + 2.j])
print("num.array([ 1. + 1.j, 3. + 2.j]) : ", a)

# tolist()함수를 이용하여 배열을 리스트로 변환한다.
print("a.tolist() : ", a.tolist())

# 배열을 특정 타입의 배열로 변환한다. 
print("a.astype(int) : ", a.astype(int))

# 배열을 복소수형 타입으로 변환한다. 
print("a.astype('complex') : ", a.astype('complex'))
