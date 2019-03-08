#/section07/02-moduse2.py

# 1) 클래스가 정의된 모듈 참조하기
"""
import my_mod2
mem = my_mod2.Member("무궁화", "moo@soldesk.com")
mem.view_info()
#-----------------------------------------------

# 2) 클래스가 정의된 모듈에 별칭 적용하기
import my_mod as user
mem = my_mod2.Member("홍길동", "hong@soldesk.com")
mem.view_info()
"""
#-----------------------------------------------

# 3) 클래스가 정의된 모듈에서 특정 기능만 가져오기
form my_mod2 import Member
mem = Member("대한민국", "korea@soldesk.com")
mem.view_info()