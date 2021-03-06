# /section03/07-range.py

"""---------------------------------------------------
#변수의 유효 범위
num1 = 100
if num1 == 100:
	num2 = 300 #지역변수
	print(num1)
	print(num2)

print(num2)

# 반복문이 1회 이상 수행되었다면 반복문 안에서 생성된 변수는 밖에서 식별 가능
for i in range(1, 10):
	result = i * 100

print(result)
print(i)

------------------------------------------------------"""
#중첩 if문
"""---------------------------------------------------

point = 70
if point>70:
	print("패스입니다")
	if point>90:
		print("A학점")
	elif point>80:
		print("B학점")
	else:
		print("C학점")
else:
	print("불합격입니다")
------------------------------------------------------"""

#1~10까지 짝수, 홀수의 합을 구분해서 출력
x=0
y=0
for i in range(1, 11):
	if i%2 == 0:
		x += i
		print("%d는 짝수" % i)
	else:
		y += i
		print("%d는 홀수" % i)	
print(x)
print(y)

#--------------------구구단--------------------
tp1 = "{0} * {1} = {2}"
for i in range(2, 10):
	for j in range(1, 10):
		k = i * j
		print(tp1.format(i, j, k))

#--------------------정 렬--------------------		
mylist = [9, 7, 5, 3, 1]
size = len(mylist)
for i in range(0, size-1):
	for j in range(i+1, size):
		if mylist[i]<mylist[j]:
			mylist[i], mylist[j] = mylist[j], mylist[i]

print(mylist)