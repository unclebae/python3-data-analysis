# -*- coding: utf-8 -*-
import numpy as num

print("In: b = arange(24).reshape(2,3,4)")
b = num.arange(24).reshape(2,3,4)

# reshape는 n차원의 배열을 다른 n차원의 배열로 변환할때 사용한다. 
# 아래 예는 1차원배열을 3차원 배열로 Z : 2, Y : 3, X : 4의 형태로 변환한 모양이다. 
print("result of reshape(2,3,4) : ", b)

# 우리는 3차원 배열을 기준으로 다음과 같은 작업을 한다. 
# 1. ravel() : 
# ravel은 n차원 배열을 1차원 배열로 풀어놓는다. 
print("result of b.ravel() : ", b.ravel())

# 2. flatten():
# flatten은 ravel()과 결과는 동일하게 나온다. 차이점은 항상 새로운 메모리를 할당하여 
# 새로운 객체를 만든다는 것이다. ravel은 배열의 뷰를 반환한다. 
print("result of b.flatten() : ", b.flatten())

# 3. shape()
# shape()는 reshape() 함수가 있지만 튜플을 직접적인 방법으로 정의할 수 있도록 한다. 
# 보는바와 같이 3차원 배열인 b가 2차원 배열로 변경이 되었다. 
b.shape = (6, 4)
print("result of b.shape = (6, 4) : ", b)

# 4. transpose()
# transpose()는 선형 대수에서 2차원 배열상에서 row --> column으로 column --> row로 변경하는 작업을 한다. 
print ("before trsnspose b : ", b)
print ("after trsnspose b : ", b.transpose())

# 5. resize()
# resize()는 배열을 새로운 차원의 배열로 변경한다. 
# 괄호가 하나더 있음을 확인하자...
b.resize( (2, 12) )
print ("result of b.resize( (2, 12) ) : ", b)
