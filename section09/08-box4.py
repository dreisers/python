# /section09/08-box4.py

# 다중 가로 막대그래프

import numpy
from matplotlib import pyplot
from sample import seoul
from sample import busan
from sample import label

pyplot.rcParams["font.family"] = "NanumGothicCoding"
pyplot.rcParams["font.size"] = 12
pyplot.rcParams["figure.figsize"] = (6, 4)

pyplot.figure()

# 막대그래프 기준축에 대한 좌표를 표현한 배열 생성(0~11)
y = numpy.arange(len(label))
print(y)

# 기준축(y축)의 좌표와 굵기를 설정한 막대그래프
pyplot.barh(y-0.1, seoul, label="서울", height=0.7, color="#ff6600")
pyplot.barh(y+0.1, busan, label="부산", height=0.7, color="#fc3000")

pyplot.yticks(y, label)
pyplot.legend()
pyplot.ylabel('월')
pyplot.xlabel('교통사고 수')
pyplot.xlim(0, 4000)
pyplot.title('2017년 서울, 부산 교통사고 현황')

pyplot.show()
pyplot.close()