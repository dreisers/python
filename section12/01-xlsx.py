#/section12/01-xlsx-py
#엑셀파일을 통한 데이터 수집

# pip install xlrd
# pip install openpyxl

from print_df import print_df
from pandas import ExcelFile
from pandas import DataFrame
from matplotlib import pyplot
import datetime as dt

# 엑셀파일 읽기
xls_file = ExcelFile('section12/children_house.xlsx')

# 엑셀의 sheet 이름들 표시
sheet_names = xls_file.sheet_names
print_df(sheet_names)

# 첫 번째 sheet를 dataframe으로 변환
df = xls_file.parse(sheet_names[0])
print_df(df)
#-----------------------------------------------------
# 데이터 전처리
# 이름에 대한 열을 리스트로 추출
city_list = list(df["지역"])
print_df(city_list)

# 새로 적용할 인덱스 이름에 대한 딕셔너리 구조 생성
index_dict = {}
for i, v in enumerate(city_list):
     index_dict[i] = v

print_df(index_dict)

# 원본에서는 이름에 대한 열을 제거하고 인덱스 이름 변경
df.drop("지역", axis=1, inplace=True)
df.rename(index=index_dict, inplace=True)

# 전국에 대한 데이터는 필요 없으므로 행 삭제
df.drop(["전국(계)"], inplace=True)

# 결과확인
print_df(df)

# 생성된 정보를 엑셀로 저장하기
# 요약정보 데이터 프레임을 엑셀로 저장
# 파일이름
# sheet_name -> 시트이름
# na_rep -> 결측치를 표시할 문자열 (기본값=빈문자열)
# index -> False로 지정할 경우 index는 저장안함 (여기서는 사용하지 않음)
# index_label-> 인덱스에 표시될 제목 (기본값=빈문자열)
# header -> 각 컬럼의 제목으로 사용될 문자열 리스트 (기본값=데이터프레임의 컬럼명)
# encoding -> 파일인코딩(기본값=utf-8)
#df.to_excel("전국어린이집.xlsx", sheet_name="어린이집", na_rep="NaN", index=True, index_label="지역", header=['15년', '16년', '17년'])

#------------------------------------------------------------------------------
# 데이터 시각화
# 그래프 만들기
pyplot.rcParams["font.family"] = "NanumGothicCoding"
pyplot.rcParams["font.size"] = 14
pyplot.rcParams["figure.figsize"] = (14, 8)

# 전체 컬럼에 대한 시각화
df.plot.bar()
pyplot.grid()
pyplot.title("2014~2016년 전국 어린이집 분포")
pyplot.legend()
pyplot.ylabel("어린이집 수")
pyplot.show()
pyplot.close()
