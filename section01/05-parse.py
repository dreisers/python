# /section01/05-parse.py
# 문자열의 인덱싱 및 슬라이싱

# 인덱싱 - 특정 위치의 글자를 추출

str = "Life is to short. You need Python"
"""
print(str[3]) #0부터 시작
print(str[-3]) #h
print(str[-1]) #n 
"""
# 슬라이싱 - 특정 범위의 글자들을 추출
print("#" + str[0:3] + "#")
print("#" + str[5:7] + "#")
print("#" + str[19:] + "#")
print("#" + str[:17] + "#")

print("#" + str + "#")
print("#" + str[:] + "#")
print("#" + str[19-7] + "#")

#문제)
jumin = "8712301"
#생년월일 
birth = jumin[:6]
#성별 
gender = jumin[-1]
#년도
year = "19" + jumin[:2]
#월
month = jumin[2:4]
#일 
day = jumin[4:6]

print(jumin)
print(birth)
print(gender)
print(year)
print(month)
print(day)