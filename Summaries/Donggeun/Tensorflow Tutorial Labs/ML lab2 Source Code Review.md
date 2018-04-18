# Source Code

~~~python
import tensorflow as tf

x_train = [1, 2, 3]
y_train = [1, 2, 3]

w = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = x_train * w + b

cost = tf.reduce_mean(tf.square(hypothesis - y_train))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(cost), sess.run(w), sess.run(b))
~~~

~~~
x_train = [1, 2, 3]
y_train = [1, 2, 3]
~~~

리스트 생성



<br/>

<br/>



~~~python
w = tf.Variable(tf.random_normal([1]), name = 'weight')
b = tf.Variable(tf.random_normal([1]), name = 'bias')
~~~

Tensorflow로 1차원 배열을 선언한다. 값은 랜덤으로 한다. Tensorflow의 변수를 파이썬 변수에 저장



<br/>

<br/>



~~~python
hypothesis = x_train * w + b
~~~

x_train 리스트에 weight(random)와 bias(random)를 곱하여 준다.



<br/>

<br/>



~~~python
cost = tf.reduce_mean(tf.square(hypothesis - y_train))
~~~

hypothesis와 y_train의 거리를 제곱하고 모두 더하여 평균을 낸다.



<br/>

<br/>



~~~python
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)
~~~

W축에 대해서 cost가 작은 쪽으로 경사를 따라서 0.01씩 움직인다는 것이다.

minimize 함수를 사용하여 우리가 줄일 cost를 전달한다.



<br/>

<br/>



~~~python
sess = tf.Session()
sess.run(tf.global_variables_initializer())
~~~

모델 실행과 초기화.

<br/>

<br/>



~~~python
for step in range(2001):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(cost), sess.run(w), sess.run(b))
~~~

2001 - 1번 반복한다.

반복할 동안 sess를 실행하고 20번 마다 반복횟수, cost, w, b를 출력한다.