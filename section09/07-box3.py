# /section09/07-box3.py

# 가로 막대그래프


from matplotlib import font_manager
from matplotlib import pyplot
from sample import newborn
from sample import year

# 한글폰트 설정
pyplot.rcParams["font.family"] = "NanumGothicCoding"
pyplot.rcParams["font.size"] = 12

# 생성될 결과물의 가로, 세로 크기 (inch단위)
pyplot.rcParams["figure.figsize"] = (5, 3)

pyplot.figure()

# 세로 막대 그래프
# -> barh() 함수의 기준축은 x방향임
pyplot.barh(year, newborn, label="신생아 수")
pyplot.legend()    #범주 표시하기
pyplot.ylabel("년도")    # 기준축(x축) 라벨
pyplot.xlabel("신생아 수") # 데이터(y축) 라벨
pyplot.xlim(350000, 450000) # 데이터(y축) 범위
pyplot.title("년도별 신생아 수") # 그래프 제목 
pyplot.grid() # 격자 선 표시
pyplot.show()  

pyplot.close()
