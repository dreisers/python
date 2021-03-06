# /section04/01-func1.py

# 함수
# 형식) def 함수이름():

def say_hello():
	print("Hello Python")
	print("안녕 파이선")

# 함수호출
say_hello()
say_hello()
#-----------------------------
#2) 매개변수를 갖는 함수
def f1(x):
	y = x+1
	tp1 = "f1({0}) => {0} + 1 = {1}"
	print(tp1.format(x, y))

f1(3)
f1(5)
f1(7)
#-----------------------------
def f2(x, y):
	z = x+y
	tp1 = "f2({0},{1}) => {0} + {1} = {2}"
	print(tp1.format(x, y, z))

f2(1, 3)
f2(5, 7)
f2(2, 4)
#-----------------------------
#매개변수에 초기값 설정하기
#sum1(x,y=0,z)와 같은 형태는 에러
def sum1(x, y, z=0):
	tp1 = "sum({0}, {1}, {2}) => {0}+{1}+{2}={3}"
	print(tp1.format(x, y, z, x+y+z))

sum1(1, 3, 5)
sum1(2, 4)
sum1(z=7, y=8, x=9) #매개변수를 직접 대입 가능
sum1(y=6, x=4)
