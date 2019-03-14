# /section09/06-box2.py

# 다중 막대그래프

import numpy
from matplotlib import pyplot
from sample import seoul
from sample import gyeunggi
from sample import busan
from sample import daegu
from sample import inchun
from sample import label

pyplot.rcParams["font.family"] = "NanumGothicCoding"
pyplot.rcParams["font.size"] = 12
pyplot.rcParams["figure.figsize"] = (9, 7)

pyplot.figure()

# 막대그래프 기준축에 대한 좌표를 표현한 배열 생성(0~11)
x = numpy.arange(len(label))
print(x)


# 2)
pyplot.bar(x-0.1, seoul, label="서울", width=0.1, color="#ff6600")
pyplot.bar(x+0.05, gyeunggi, label="경기", width=0.1, color="#fc3000")
pyplot.bar(x+0.2, busan, label="부산", width=0.1, color="#80ff00")
pyplot.bar(x+0.35, inchun, label="인천", width=0.1, color="#80ffff")
pyplot.bar(x+0.5, daegu, label="대구", width=0.1, color="#ffff80")


pyplot.xticks(x, label)
pyplot.legend()
pyplot.xlabel('요일')
pyplot.ylabel('이용자 수')
pyplot.ylim(300000, 4500000)
pyplot.title('17년 지역별 대중교통 이용 현황')


pyplot.savefig('data.png', dpi=200)
pyplot.show()
pyplot.close()