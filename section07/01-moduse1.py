#/section07/01-moduse1.py

#모듈의 활용
#모듈 : 다른 프로그램에서 활용하기 위한 프로그램 조각
#import 파일이름

"""
import my_mod1 

print(my_mod1.NAME)
print(my_mod1.plus(5, 3))
print(my_mod1.minus(5, 3))
"""

#--------------------------------
# 2) 모듈에 별칭 적용
# -> import 파일이름 as 별칭
import my_mod1 as hello
print(hello.NAME)
print(hello.plus(5, 3))
print(hello.minus(5, 3))

#--------------------------------
# 3) 모듈안에 포함된 특정 기능만 골라서 가져오기
# -> from 모듈이름 import 기능명
from my_mod1 import NAME
from my_mod1 import plus

print(NAME)
print(plus(5, 3))
#에러. minus함수는 import하지 않았으므로 사용불가
#print(minus(5, 3))
