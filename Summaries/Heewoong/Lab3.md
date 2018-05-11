# 2018/04/14 lab 3#

```
import tensorflow as tf
import  matplotlib.pyplot as plt
X = [1, 2, 3]
Y = [1, 2, 3] ##데이터 입력

W = tf.placeholder(tf.float32)
hypothesis = X * W ##H(x) = Wx

cost = tf.reduce_mean(tf.square(hypothesis - Y)) ##차를 제곱하여 평균을 냄.
sess = tf.Session()
sess.run(tf.global_variables_initializer()) ##variable 초기화

W_val = []
cost_val = [] ##리스트 생성(그래프 위함)
for i in range(-30, 50):
    feed_W = i* 0.1 ##-3에서 5까지 0.1씩 움직임.
    curr_cost, curr_W = sess.run([cost, W], feed_dict={W: feed_W})
    W_val.append(curr_W)
    cost_val.append(curr_cost) ##리스트에 값 집어넣음

plt.plot(W_val, cost_val)
plt.show()


import tensorflow as tf
x_data = [1, 2, 3]
y_data = [1, 2, 3]

W = tf.Variable(tf.random_normal([1]), name='weight') ##랜덤값 지급
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

hypothesis = X*W

cost = tf.reduce_sum(tf.square(hypothesis - Y))

learning_rate = 0.1 ##이동하는 수치
gradient = tf.reduce_mean((W * X - Y) * X) ##GradientDescentOptimizer와 같다.
descent = W - learning_rate * gradient ##descent 구하기
update = W.assign(descent) ##W업데이트

sess = tf.Session()

sess.run(tf.global_variables_initializer())
for step in range(31):
    sess.run(update, feed_dict={X: x_data, Y: y_data}) ##X데이터, Y데이터로 업데이트
    print(step, sess.run(cost, feed_dict={X: x_data, Y: y_data}), sess.run(W))
##첫 출력값이 스텝, 두번째가 코스트 값, 마지막이 W값이다.
tf.train.GradientDescentOptimizer


import tensorflow as tf
X = [1, 2, 3]
Y = [1, 2, 3]

W = tf.Variable(5.0) ##W의 초기값

hypothesis = X * W
cost = tf.reduce_mean(tf.square(hypothesis - Y))
optimiser = tf.train.GradientDescentOptimizer(learning_rate = 0.1)
train = optimiser.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(100):
    print(step, sess.run(W))
    sess.run(train)


import tensorflow as tf
X = [1, 2, 3]
Y = [1, 2, 3]

W = tf.Variable(5.0) ##W의 초기값

hypothesis = X * W
gradient = tf.reduce_mean((W * X - Y) * X) * 2
cost = tf.reduce_mean(tf.square(hypothesis - Y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate= 0.01)

gvs = optimizer.compute_gradients(cost)
##이 순서에 원하는 gradient 값을 조정할 수 있다.
apply_gradients = optimizer.apply_gradients(gvs)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(100):
    print(step, sess.run([gradient, W, gvs]))
    sess.run(apply_gradients)
##각각 스텝, gradient 값, 그에 해당하는W값을 출력한다.
```
