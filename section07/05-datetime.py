#/section07/05-datetime.py

# 시스템의 현재 날짜 정보 조회하기

import datetime as DT
now_time = DT.datetime.now()
print(now_time)

# 현재시각 객체서 원하는 값만 추출하기
print(now_time.year)
print(now_time.month)
print(now_time.day)
print(now_time.hour)
print(now_time.minute)
print(now_time.second)
print(now_time.microsecond)

#요일 이름 출력
d = now_time.weekday()
print(d)
days = ("월", "화", "수", "목", "금", "토", "일")
print(days[d])

#출력 형식 만들기
print(now_time.strftime("%y/%m/%d %H:%M:%S"))
