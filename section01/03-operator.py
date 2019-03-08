#/section01/03-operator.py

"""--------------------------
 연산자
 
 -----------------------------"""

"""
a = 3
b = 4
print(a+b) 
print(a-b)
print(a*b)
print(a/b) #몫. 소수점 발생
print(a%b) # 나머지
#파이선에만 있음 
print(a//b) # 몫. 소수점 버림
print(a**b) # 제곱   

"""

"""
# 단항연산자
a = 1
a += 100
a *= 10
a //= 3
a % 5
print(a)

# 비교연산자
print(100==5)
print(100!=5)
print(100>=5)
print(100>5)
print(100<=5)
print(100<5)

# 논리연산자 
print(100>=100 and 50==10)
print(10%2==0 or 10%5==0)

"""

# is 연산자 : 두 변수가 동일한지 판별
a = True
b = True
c = False

s1 = a is b 
print(s1) #True

s2 = a is c 
print(s2) #False

# == 와 is의 차이
x = 100
y = 100.0 

# 단순히 값 비교하므로 두 값이 같다고 판단함
print(x==y) #True

# 데이터 타입까지 비교하므로 정수와 실수는 다르다고 판단함
print(x is y) #False
