#/section01/04-string.py

"""
문자열 "" 나 ''로 감싸야 한다.
혼용은 불가

"""

msg1 = "Lifr is too short"
msg2 = 'You need Python'

print(msg1)
print()
print(msg2)

print(msg1 + "," + msg2)
name = "python"
print(name * 50)

pay = "100000"
bonus = "100"
print(pay + bonus)

case1 = "Life is \' too \' short"
print(case1)

case2 = "Life is \" too \" short"
print(case2)

case3 = "Life is 'too' short"
print(case3)

print("\n")# #
print("#\n#")# #
print("\"")# "
print("\'")# '
print("\\")# \