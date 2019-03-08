# /section10/03-wc-backgroundimage.py

# Word Cloud 배경이미지

from matplotlib import pyplot
from wordcloud import WordCloud
from wordcloud import STOPWORDS
# 이미지 처리 모듈 - 기본 모듈이므로 따로 설치 X
from PIL import Image
import numpy # 연산모듈

text = ""
with open("section10/res/Brooklyn.txt", "r", encoding="utf-8") as f:
    text = f.read()

print(text)


# 금지어 설정 -> 필요한 만큼 add()함수 호춣해서 추가
# 금지어 -> Alice, said
ignore = set(STOPWORDS)
ignore.add("someone")
ignore.add("know")


#------------------------------------------------------
# 꾸밈기능 : 앨리스 이미 파일위에 출력
# 배경이미지 가져오기
img = Image.open("section10/res/ficklefriend.jpg")
# 배경이미지 데이터를 numpy리스트로 변환
img_array = numpy.array(img)
#------------------------------------------------------

#WordCloud 클래스의 객체 생성
wc = WordCloud( width=1200, height=800, scale=2.0, stopwords=ignore, max_font_size=150, max_words=100, mask=img_array, background_color="#e1fdfc") 

gen = wc.generate(text)
print(gen.words_)

pyplot.figure()

pyplot.imshow(gen, interpolation="bilinear")
wc.to_file("brooklyn2.png")

pyplot.close()