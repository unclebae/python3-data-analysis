# -*- coding: utf-8 -*-

import sys
from datetime import datetime
import numpy as np

"""
    이 프로그램은 파이선 방식으로 벡터를 추가하는 예제를 보여준다. 
	이 프로그램은 다음과 같이 실행한다. 
	python vectorTest.py n

	n 값은 정수형으로 벡터의 총 길이를 나타낸다. 

	첫번째 벡터는 0 에서 n까지 스퀘어 값을 저장한다. 
	두번재 벡터는 0 에서 n까지 큐브 값을 저장한다. 

	이 프로그램은 마지막으로 2개의 엘리먼트들의 합을 구하는 것으로 이 시간을 기록하여 출력한다. 
"""

def numpysum(n) :
	a = np.arange(n) ** 2
	b = np.arange(n) ** 3
	c = a + b

	return c

def pythonsum(n):
	a = range(n)
	b = range(n)
	c = []

	for i in range(n):
		a[i] = i ** 2
		b[i] = i ** 3
		c.append(a[i] + b[i])

	return c

size = int(sys.argv[1])

start = datetime.now()
c = pythonsum(size)
end = datetime.now()

print ("The last 2 elements of the sum", c[-2:])
print ("PythonSum elasped time in microseconds", (end-start).microseconds)

start = datetime.now()
c = numpysum(size)
end = datetime.now()

print ("The last 2 elements of the sum", c[-2:])
print ("PythonSum elasped time in microseconds", (end-start).microseconds)
