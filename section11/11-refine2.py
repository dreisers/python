# /section11/11-refine2.py

# 데이터정제(2) - 결측치 대처법

from print_df import print_df
from pandas import DataFrame
from sample import grade_dic
import numpy
# pip install sklearn
from sklearn.impute import SimpleImputer

df = DataFrame(grade_dic, index=["철수", "영희", "민철", "수현", "호영"])
print_df(df)
#-------------------------------------------------------------------------------
# 결측치를 특정값으로 채움
# -> sklearn 모듈이 아닌 DataFrame 자체 기능
re_df1 = df.fillna(value=50)
print_df(re_df1)
#-------------------------------------------------------------------------------
# sklearn 모듈 기반으로 결측치 대처

# 1) 결측치를 정제할 규칙 정의
# -> 각 열단위로 평균(strategy="mean")을 결측치(missing_values)에 지정
# -> strategy 옵션 : mean=평균, median=중앙값, most_frequent : 최빈값(가장 많이 관측되는 수)
imr = SimpleImputer(missing_values=numpy.nan, strategy="mean")

# 2) dataframe의 값에 대해 규칙 적용
df_imr = imr.fit_transform(df.values)
print_df(df_imr)

# 3) 적용된 규칙으로 새로운 데이터 프레임 생성
re_df2 = DataFrame(df_imr, index=df.index, columns=df.columns)
print_df(re_df2)