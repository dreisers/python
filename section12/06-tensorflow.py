#/section12/06-tensorflow.py

# 노동시간에 따른 매출 예측 프로그램

# 모듈 설치
# pip install tensorflow

import tensorflow as tf                              # 오픈소스 라이브러리 모듈
hello = tf.constant('Hello World!')
sess = tf.Session()
#print(sess.run(hello))


"""
# 데이터 셋팅
xData = [1, 2, 3, 4, 5, 6, 7]
yData = [25000, 55000, 75000, 110000, 128000, 155000, 180000]

# W값을 텐서에게 부여
W = tf.Variable(tf.random_uniform([1], -100, 100))                          

# b값을 텐서에게 부여
b = tf.Variable(tf.random_uniform([1], -100, 100))

# W의 값을 임의로 주기 위해 생성
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

#리니어 예측하기
H = W * X + b  

# 예측값 - 실제값의 제곱
cost = tf.reduce_mean(tf.square(H - Y))


# 최소화
# 기울기의 값을 줄여 나가는 것
a = tf.Variable(0.01)
optimizer = tf.train.GradientDescentOptimizer(a)
train = optimizer.minimize(cost)

init = tf.global_variables_initializer()

# Session 생성
sess = tf.Session()
sess.run(init)

# linear 찾기 (학습)
for i in range(5001) :
     sess.run(train, feed_dict={X: xData, Y: yData})
     if i%500 == 0 :
         print(i, sess.run(cost, feed_dict={X: xData, Y: yData}), sess.run(W), sess.run(b))
print(sess.run(H, feed_dict={X: [8]}))
"""
#------------------------------------------------------------------------------------------
xData = [1, 2, 3, 4, 5, 6, 7]
yData = [25000, 55000, 75000, 110000, 128000, 155000, 180000]
W = tf.Variable(tf.random_uniform([1], -100, 100))                           
b = tf.Variable(tf.random_uniform([1], -100, 100)) 
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)
H = W * X + b                                                                               
cost = tf.reduce_mean(tf.square(H - Y))
a = tf.Variable(0.01)
optimizer = tf.train.GradientDescentOptimizer(a)
train = optimizer.minimize(cost)
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
for i in range(5001) :
     sess.run(train, feed_dict={X: xData, Y: yData})
     if i%500 == 0 :
         print(i, sess.run(cost, feed_dict={X: xData, Y: yData}), sess.run(W), sess.run(b))
print(sess.run(H, feed_dict={X: [8]}))