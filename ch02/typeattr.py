# -*- coding: utf-8 -*-
import numpy as num

# char 어트리뷰트의 사용 
t = num.dtype('Float64')
print("t.char of Float64 : ", t.char)

# type 어트리뷰트는 배열 엘리먼트의 객체 타입에 상응한다. 
print("t.tyep of Float64 : ", t.type)

# str 속성은 데이터타입을 string으로 표현한다. 
# 엔디안을 나타내는 표기식과 바이트의 수를 노출한다. 
# 엔디안은 32비트 혹은 64비트 내부에 바이트 순서를 표시한다. 
# 빅 엔디안의 경우 가장 중요한 바이트는 맨 처음에 저장된다. 그리고 '>'로 표기된다. 
# 리틀 엔디안의 경우 가장 최근의 바이트가 가장 먼저 저장된다. 그리고 '<'로 표기된다.

print("t.str of Float64 : ", t.str)

