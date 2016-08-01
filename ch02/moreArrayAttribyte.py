# _*_ coding: utf-8 _*_
import numpy as num

a = num.arange(24).reshape(2, 12)
print("num.arange(24).reshape(2, 12) : ", a)

# ndim은 배열의 차수를 반환한다. 
print("a.ndim : ", a.ndim)

# size는 배열이 가지는 엘리먼트의 총 개수를 나타낸다. 
print("a.size : ", a.size)

# itemsize는 배열내에 각 엘리먼트가 가지는 바이트 수를 반환한다. 
print("a.itemsize : ", a.itemsize)

# nbyte는 전체 배열이 필요로 하는 총 바이트수이다. 이는 size * itemsize로 계산된다. 
print("a.nbytes : ", a.nbytes)

print("a.size * a.itemsize : ", (a.size * a.itemsize))

print("num.resize(6, 4) : ", num.resize(6, 4))

# T는 transpose()함수와 동일한 결과를 반환한다. 
print("a.T : ", a.T)

print("a.ndim after transform T : ", a.ndim)

print("a.T after transform T :", a.T)

# 복소수는 numpy에서 j로 표현된다. 
print("num.array([1.j + 1, 2.j + 3]) : ", num.array([1.j + 1, 2.j + 3]))

# real은 배열에서 숫자의 real파트를 반환한다. 
print("a.real : ", a.real)

# imag는 배열의 허수 영역을 출력한다. 
print("a.imag : ", a.imag)

# dtype은 배열이 저장하는 데이터 타입이며 복소수의 경우 complex가 반환된다. 
print("a.dtype : ", a.dtype)

print("a.dtype.str : ", a.dtype.str)

# flat속성은 numpy.flatiter객체를 나타낸다. flatiter 를 통해서만 flat객체에 접근할 수 있으며, 생성자로 생성할 수 없다. 
# flat 반복자는 flat 배열의 각 엘리먼트를 반복하면서 조회가능하다. 
b = num.arange(4).reshape(2,2)
print("num.arange(4).reshape(2,2) : ", b)

f = b.flat
print("b.flat : ", f)

print("for it in f: print it : ")
for it in f:
	print (it)

# 직접적으로 flatiter 객체의 특정 인덱스에 접근하여 object를 획득할 수 있다.  
print("b.flat[2] : ", b.flat[2])

# 또한 직접 엘리먼트를 조회할 수 있다. 
print("b.flat[[1, 3]] : ", b.flat[[1, 3]])

print("b : ", b)

# flat속성은 세팅이 가능하며 다음과 같이 세팅한다. 
b.flat[[1, 3]] = 1
print("b.flat[[1, 3]] = 1 : ", b)

