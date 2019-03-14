# /section11/05-boxplot.py

# 상자그림
# 데이터에 이상이 있는지, 어느정도 분포되어 있는지 알수 있다.

from matplotlib import pyplot
from pandas import DataFrame
from sample import grade_dic

# 데이터 구성하기
df = DataFrame(grade_dic, index=["철수", "영희", "민철", "수현", "호영"])

# 한글폰트, 그래픽 크기 설정
pyplot.rcParams["font.family"] = "NanumGothicCoding"
pyplot.rcParams["font.size"] = 12
pyplot.rcParams["figure.figsize"] = (12, 8)

# 국어 점수에 대한 상자그림 보기
pyplot.figure()
df.boxplot("국어")
pyplot.savefig("boxplot1.png", dpi=300)
pyplot.show()
pyplot.close()