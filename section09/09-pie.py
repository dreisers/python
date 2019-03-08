# /section09/08-box4.py

# 원형그래프
# 전체를 기준으로 한 부분이 상대적 크기를 표시하는 그래프

from matplotlib import pyplot

pyplot.rcParams["font.family"] = "NanumGothicCoding"
pyplot.rcParams["font.size"] = 12
pyplot.rcParams["figure.figsize"] = (6, 4)

pyplot.figure()

# 표시할 데이터 설정
# -> 총 합이 100이 아닐 경우 라이브러리가 자동으로 비율을 계산함
ratio = [3700, 2800, 1300, 590, 600]

# 각 항목의 라벨
labels = ['Apple', 'Samsung', 'LG', 'Sony', '기타']

# 확대비율
explode = [0.0, 0.0, 0.0, 0.2, 0.1]

# 파이차트 표시
# -> (데이터, 라벨, 색상, 확대, 수치값 표시형식, 그림자, 시작각도)
# -> autopct 파라미터 설정 안할 경우 수치값 표시 안됨
#      의미 : %0.2f (소수점 2째 자리까지 표시) + %% (순수한 퍼센티지)
# -> startangle 기본값은 0도
# -> 각 데이터 항목들은 반시계 방향으로 회전하면서 배치됨

# 각 항목의 색상
colors = ['#ff6600', '#ff00ff', '#ffff00', '#0000ff', '#ff2222']

pyplot.title('스마트폰 점유율')
pyplot.pie(ratio, labels=labels, colors=colors, explode=explode, autopct='%0.2f%%', shadow=False, startangle=90)
            #  데이터,    라벨                색상                  확대비율         수치값 표시 형식          그림자           시작각도
pyplot.show()
pyplot.close()
