#/section06/01-obj1.py

#생성자 함수
"""
class Member:
	username = None
	email = None

	#생성자 함수 앞뒤로 언더바 2개
	def __init__(self):
		print("생성자 함수 호출")
		self.username = "python"
		self.email = "webmaster@soldesk.com"

	def view_info(self):
		tpl = "이름:{0} / 이메일:{1}"
		print(tpl.format(self.username, self.email))

#객체생성
mem1 = Member()
mem1.view_info()
"""
#------------------------------------------
#파라미터를 갖는 생성자

class Member:
	username = None
	email = None

	def __init__(self, username, email):
		print("생성자 함수 호출")
		self.username = username
		self.email = email

	def view_info(self):
		tpl = "이름:{0} / 이메일:{1}"
		print(tpl.format(self.username, self.email))

#객체생성
mem1 = Member("홍길동", "hong@soldesk.com")
mem1.view_info()

mem2 = Member("무궁화", "moo@soldesk.com")
mem2.view_info()