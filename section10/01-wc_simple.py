# /section10/01-wc-simple.py

# Word Cloud
# 텍스트마이닝(Text mining)
# -> 문자로 된 데이터에서 가치 있는 정보를 얻어 내는 분석 기법

# 형태소분석
# -> 문장을 구성하는 어절들이 어떤 품사로 되어 있는지 파악

# 모듈설치
# -> pip install wordcloud
# -> 일단 영어만 처리 가능

from matplotlib import pyplot  # 그래프모듈
from wordcloud import WordCloud  # 워드클라우드모듈

text = ""
with open("section10/res/이상한나라의앨리스.txt", "r", encoding="utf-8") as f:
    text = f.read()

print(text)

# WordCloud클래스의 객체 생성

wc = WordCloud(width=1200, height=800, scale=3.0)
# width : 모니터 해상도  가로크기
# height : 모니터 해상도 세로크기
# scale : 보고서용, 인쇄용으로는 최소 2,3배는 크게 해야함

# 단어 빈도수 계산
# WordCloud 객체를 사용하여 텍스트에 대한 단어 빈도수 추출
# -> {'단어' : 빈도수, '단어' : 빈도수 ~~ } 형식으로 딕셔너리를 직접 코딩으로 정의해도 무관함
gen = wc.generate(text)
print(gen.words_)

# 그래픽 생성
pyplot.figure()

# 그래프 표시 데이터를 단어 빈도수에 대한 딕셔너리로 지정
# interpolation : 워드클라우드에 등록되어 있는 정렬방식
pyplot.imshow(gen, interpolation="bilinear")
wc.to_file("simple.png") #크기는 scale에서 조정가능

pyplot.close()