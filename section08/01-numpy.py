#/section08/01-numpy1.py

# numpy 모듈 : 리스트의 기능 강화판
# numpy 모듈 설치
print(arr)
print(len(arr))

# 리스트를 통한 1차원 배열 만들기
a = numpy.array(arr)
print(a)
print(len(a))

# -> cmd -> pip install numpy
# -> pip list 모듈 설치 확인

# 모듈 가져오기
import numpy

arr = [1, 2, 3]
arr2 = [1.2, 3, "4"]
print(arr2)

# 실수가 범위가 더 크므로 모든 원소가 실수형으로 변환
b = numpy.array([1, 2.3, 4, 5.6])
print(b)

# 모든 타입이 문자열로 변환
c = numpy.array([1.2, 3, '4'])
print(c)

# 모든  원소의 타입을 강제로 int로 지정
d = numpy.array( [1, 2.4, 3, 4.6], dtype='int')
print(d)

arr3 = numpy.array([1, 3, 5, 7, 9])
size = len(arr3)
print("배열의 원소는 %d개 입니다." % size)

# 배열 원소 접근
print(arr3[0])
print(arr3[1])
print(arr3[3])

