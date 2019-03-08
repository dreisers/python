
#1) year라는 변수에 자신이 태어난 년도를 할당
# age라는 변수에 year 변수를 사용하여 자신의 나이를 계산하여 할당하고 결과 출력
year = 1994
age = 2019 - year + 1
print(age)

#2) age라는 변수에 자신의 나이를 할당
# year라는 변수에 age를 사용하여 자신이 태어난 년도를 계산하여 할당하고 결과 출력
age = 26
year = age + 1994 - 1
print(year)

#3) 주민번호가 801023-1000123일 때, 생년월일을 출력하는 소스코드 작성
msg = "{0}은 {1}년 {2}월 {3}일 입니다."
print(msg.format("당신의 생일", 80, 10, 23))

#4) 
location = "C:\\myphoto\\helloworld.jpg"
print(location[0:10])
print(location[11:21])
print(location[-3:])

#5)
a = [1, 2, 3, 4, 5]
print(a)
a.sort(reverse=True)
print(a)

#6)
str = ["Life", "is", "too", "short"]
data = ' '
print(str)
print(data.join(str))
print(data.join(str).upper())

#7)
a = [1, 2, 3]
b = [4, 5]
a.extend(b)
print(a)

#8)
grade = (7, 5, 5, 5, 5, 10, 7)
print(grade)

#9)
cart = [ {"price":"38000원", "qty":"6개"}
		,{"price":"20000원", "qty":"4개"}
		,{"price":"17900원", "qty":"3개"}
		,{"price":"17900원", "qty":"5개"} ]
tp1 = "{0}원 x {1}개 -> 총 {2}원"
print(tp1.format(cart[0]["price"],cart[0]["qty"],cart[0]["price"] * cart[0]["qty"]))
print(tp1.format(cart[1]["price"],cart[1]["qty"], cart[1]["price"] * cart[1]["qty"]))
print(tp1.format(cart[2]["price"],cart[2]["qty"],cart[2]["price"] * cart[2]["qty"]))
print(tp1.format(cart[3]["price"], cart[3]["qty"],cart[3]["price"] * cart[3]["qty"]))


