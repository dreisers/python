# /section/07-formatting.py
# 문자열 포매팅 (출력서식)

# %d 정수
# %f 실수
# %s 문자열

"""

str1 = "나는 %d원을 갖고 있다." % 5000
print(str1)

str2 = "%s날짜는 %d년 %d월 %d일 입니다."
msg1 = str2 %("정모", 2019, 3, 4)
print(msg1)

msg2 = str2 %("약속", 2019, 3, 5)
print(msg2)

print("%d원을 입금했습니다." % 12345)
print("%010d원을 입금했습니다." % 12345)
print("%-010d원을 입금했습니다." % 12345)

print("%s에 살고 있습니다." % "KOREA")
print("%10s에 살고 있습니다." % "KOREA")
print("%-10s에 살고 있습니다." % "KOREA")

money = 123.456789
print("%f원 입니다. " % money)
print("%010.3f원 입니다. " % money)
print("%10.3f원 입니다. " % money)
print("%-10.3f원 입니다. " % money)
print("%.3f원 입니다. " % money)
print("0.3%f원 입니다. " % money)

"""

#파이선에만 있음
#0번쨰 위치에 format()함수에 전달된 0번째 값을 대입
msg1 = "I eat {0} apples."
print(msg1.format(3))

msg2 = "{0}은 {1}년 {2}월 {3}일 입니다."
print(msg2.format("오늘", 2019, 3, 4))

#이름으로 넣기
msg3 = "{name}은 {yy}년 {mm}월 {dd}일 입니다."
print(msg3.format(name="내일", yy=2019, mm=3, dd=5))

#혼합사용
msg4 = "{0}은 {1}년 {mm}월 {dd}일 입니다."
print(msg4.format("손흥민", 2019, mm=3, dd=5))

#문자열에 "{", "}" 포함시키기 -> 두겹사용
msg5 = "{{파이선}}은 {0}다"
print(msg5.format("쉽"))
print(msg5.format("좋"))