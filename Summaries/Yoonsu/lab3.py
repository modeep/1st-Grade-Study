#cost값을 그래프로 그려보는 코드
import tensorflow as tf
import matplotlib.pyplot as plt
X = [1, 2, 3]                                           #x_train 데이터 입력
Y = [1, 2, 3]                                           #Y_train 데이터 입력

W = tf.placeholder(tf.float32)                          #placeholder로 틀을 만들어 놓음

hypothesis = X * W                                      #hypothesis 정의

cost = tf.reduce_mean(tf.square(hypothesis - Y))         #cost Funstion를 정의 reduce_mean은 텐서가 주어졌을때 그 값을 평균 내주는 것이다.

sess = tf.Session()                                     #session에서 graph실행

sess.run(tf.global_variables_initializer())             #session에서 사용될 변수 초기화

W_val = []                                              # W와 cost값을 저장할 리스트 생성
cost_val = []

for i in range(-30, 50):                                            #range를 -30에서 50으로 두고 0.1씩 움직이게 한다.
    feed_W = i * 0.1
    curr_cost,curr_W = sess.run([cost,W], feed_dict={W: feed_W})     #feed_dict로 값을 넘기면서 cost와 W값의 변동을
    W_val.append(curr_W)                                             #curr cost와 curr W에 넣고 이를 리스트에 저장한다.
    cost_val.append(curr_cost)

plt.plot(W_val, cost_val)                                 #W_val값과 cost_val값을 각각 x와 y축으로 놓은 그래프를 그려본다.
plt.show()


#Minimize : Gradient Descent using derivative:
#W -= Learning_rate * derivative
learning_rate = 0.1                                         #그래프를 따라 내려가는 폭
gradient = tf.reduce_mean((W * X - Y) * X)                  #Gradient 정의
descent = W - learning_rate * gradient                      #descent값 구하는 것을 정의
update = W.assign(descent)                                  #바로 넣을 수 없기에 assign을 사용

import tensorflow as tf
x_data=[1,2,3]
y_data=[1,2,3]

W= tf.Variable(tf.random_normal([1]),name='weight')     #W에 랜덤값 집어넣음
X=tf.placeholder(tf.float32)
Y=tf.placeholder(tf.float32)

hypothesis = X*W

cost = tf.reduce_sum(tf.square(hypothesis-Y))

learning_rate = 0.1                                     #그래프를 따라 내려가는 폭
gradient = tf.reduce_mean((W*X-Y)*X)                    #Gradient 정의
descent = W-learning_rate*gradient                      #descent값 구하는 것을 정의
update=W.assign(descent)                                #바로 넣을 수 없기에 assign을 사용

sess=tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(21):
    sess.run(update,feed_dict={X:x_data,Y: y_data})
    print(step,sess.run(cost,feed_dict={X:x_data,Y: y_data}),sess.run(W))


import tensorflow as tf
X = [1, 2, 3]
Y = [1, 2, 3]

W = tf.Variable(5.0)                                            #W의 초기값설정(제대로 돌아가는지 확인)

hypothesis = X * W
cost = tf.reduce_mean(tf.square(hypothesis - Y))
optimiser = tf.train.GradientDescentOptimizer(learning_rate = 0.1)
train = optimiser.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(100):                                         #
    print(step, sess.run(W))
    sess.run(train)
