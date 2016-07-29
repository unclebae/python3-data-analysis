# -*- coding: utf-8 -*-
import numpy as num

a = num.arange(9)
print("a[3:7] of arange(9) : ", a[3:7])

# 다음으로 우리는 0 ~ 7 까지 2씩 증가하면서 데이터를 추출할 수 있다. 
print("a[:7:2] of arange(9) : ", a[:7:2])

# 음수 인덱스를 지정하여 역순 배열을 생성할 수 있다. 
print("a[::-1] of arange(9) : ", a[::-1])
