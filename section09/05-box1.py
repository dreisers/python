# /section09/05-box1.py

# 막대그래프
# -> 범주, 빈도 데이터를 요약해서 보여주는 그래프

from matplotlib import font_manager
from matplotlib import pyplot
from sample import newborn
from sample import year

# 한글폰트 설정
pyplot.rcParams["font.family"] = "NanumGothicCoding"
pyplot.rcParams["font.size"] = 12

# 생성될 결과물의 가로, 세로 크기 (inch단위)
pyplot.rcParams["figure.figsize"] = (12, 8)

pyplot.figure()

# 세로 막대 그래프
# -> bar() 함수의 기준축은 x방향임
pyplot.bar(year, newborn, label="신생아 수")
pyplot.legend()    #범주 표시하기
pyplot.xlabel("년도")    # 기준축(x축) 라벨
pyplot.ylabel("신생아 수") # 데이터(y축) 라벨
pyplot.ylim(350000, 450000) # 데이터(y축) 범위
pyplot.title("년도별 신생아 수") # 그래프 제목 
pyplot.grid() # 격자 선 표시
pyplot.show()  

pyplot.close()
