#/section08/02-numpy2.py

# 배열 연산

import numpy

grade = numpy.array([82, 76, 91, 65])
print(grade)

# 모든 원소에 대하여 2씩 더하기
new1 = grade + 2
print(new1)

# 모든 원소에 대하여 5씩 빼기
new2 = grade - 5
print(new2)

#-----------------------------------------

# 배열 원소끼리 연산
# 인덱스가 동일한 원소끼리 수행
arr1 = numpy.array([10, 15, 20, 25, 30])
arr2 = numpy.array([2, 3, 4, 5, 6])

arr3 = arr1 + arr2
print(arr3)

arr4 = arr1 - arr2
print(arr4)

#------------------------------------------

sample = numpy.array( [82, 77, 95, 60] )
print("0총점 : %d" % numpy.sum(sample))
print("평균 : %d" % numpy.average(sample))
print("최대값 : %d" % numpy.max(sample))
print("최소값 : %d" % numpy.min(sample))
