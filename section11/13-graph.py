# /section11/13-graph.py
# 데이터프레임 시각화

from matplotlib import pyplot
from print_df import print_df
from pandas import DataFrame
from sklearn.impute import SimpleImputer
from sample import traffic
import numpy

df = DataFrame(traffic)
print_df(df)
#-------------------------------------------------
# 데이터 전처리
month = list(df["month"]) # "월"에 대한 컬럼만 리스트로 추출
new_name = {} # 빈 딕셔너리 생성
print_df(month)  

# "월" 리스트에 대해 반복
for i, v in enumerate(month):
     # 딕셔너리에 {인덱스번호 : 값} 형식으로 채워넣음
     new_name[i] = v

# 데이터프레임의 인덱스 변경
df.rename(index=new_name, inplace=True)
# 기존의 "월" 컬럼은 삭제
df.drop("month", axis=1, inplace=True)
print_df(df)
#-------------------------------------------------
# 한글폰트, 그래픽 크기 설정
pyplot.rcParams["font.family"] = "NanumGothicCoding"
pyplot.rcParams["font.size"] = 15
pyplot.rcParams["figure.figsize"] = (15, 10)

"""------------------------------------------------
# 1) 상자그림
pyplot.grid()
df.boxplot()
pyplot.title("2017년 교통사고 변화")
pyplot.ylabel(교통사고 수")
#pyplot.savefig('boxplot3.png', dpi=200) #파일로 저장
pyplot.show()
pyplot.close()
------------------------------------------------"""
# 2) 선 그래프
x = numpy.arange(len(month))
df.plot()
pyplot.grid()
pyplot.legend()
pyplot.title("2017년 월별 교통사고 변화")
pyplot.ylabel("교통사고 수")
pyplot.xticks(x, month)
pyplot.xlim(0, 11)
pyplot.show()
pyplot.close()