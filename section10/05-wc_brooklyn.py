# /section10/03-wc-backgroundimage.py

from matplotlib import pyplot
from wordcloud import WordCloud
from wordcloud import STOPWORDS

text = ""
with open("section10/res/Brooklyn.txt", "r", encoding="utf-8") as f:
    text = f.read()

print(text)

ignore = set(STOPWORDS)
ignore.add("someone")

#WordCloud 클래스의 객체 생성
wc = WordCloud( width=1200, height=800, scale=2.0,  max_font_size=150, max_words=100, background_color="#e1fdfc")

gen = wc.generate(text)
print(gen.words_)

pyplot.figure()

pyplot.imshow(gen, interpolation="bilinear")
wc.to_file("brooklyn.png")

pyplot.close()