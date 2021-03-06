# /section02/01-list.py

"""
연속성 자료형
 - 하나의 변수에 여러개의 값을 저장하는 형태
 - 리스트, 튜플, 딕셔너리, 집합
 - 일반적인 프로그래밍언어에서는 배열로 많이 사용

"""

#5명의 학생에 대한 성적 나열
grade = [90, 85, 73, 64, 100]
print(grade)

names = ["홍길동", "무궁화", "개나리", "진달래", "라일락"]
print(names)

#인덱스 번호를 통해 각 원소(element)에 접근할 수 있다.
kor_point = grade[1]
student_name = names[1]
print("%s의 점수는 %d점 입니다." % (student_name, kor_point))

#파이선은 서로 다른 자료형들을 함께 사용 가능
stud1 = ["홍길동", 98]
stud2 = ["무궁화", 82]
print(stud1)
print(stud2)

#값의 변경
stud1[0] = "라일락"
stud2[1] = 100

#리스트의 원소를 출력
#msg = "{0}의 점수는 {1}점 입니다"
msg = "{1}의 점수는 {0}점 입니다"
print(msg.format(stud1[0], stud1[1]))
print(msg.format(stud2[0], stud2[1]))