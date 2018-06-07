# ML lab 05: TensorFlow로 Logistic Classification의 구현하기 (new)
Logistic Regression에서는 ylog를 곱하여 Cost가 작으면 더 작게 크면 더 크게 만들어준다.

~~~
x = tf.placeholder(tf.float32, shape=[None, 2])
y = tf.placeholder(tf.float32, shape=[None, 1])
w = tf.variable(tf.random_normal([2, 1]), name='weight')
b = tf.variable(tf.random_normal([1]), name='bias')
~~~
bias는 항상 나가는 값과 같다 그래서 y와 같은 1로 설정한다.

<br/>

~~~
hypothesis = tf.sigmoid(tf.matmul(x, w) + b)
~~~
hypothesis를 구한다음에 시그모이드 함수를 써서 0~1사이의 값으로 나타낸다.

<br/>

~~~
cost = -tf.reduce_mean(y * tf.log(hypothesis) + (1 - y) * tf.log(1 - hypothesis))
~~~
tf.log를 곱해줘서 값이 확연히 차이나게 만들어준다.

<br/>

~~~
train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)
~~~
Gradient Descent

<br/>

~~~
predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, y), dtype=tf.float32))
~~~
시그모이드 함수를 사용했기 때문에 값이 0~1의 값으로 나올 것이다. 그러나 우리는 0이나 1의 값이 필요하기 때문에 tf.equal를 사용하면 0과 1의 값으로 출력할 수 있다.

<br/>

~~~
with tf.Session() as sess:
  sess.run(tf.global_variables_initializer())
  
  for step in range(10001):
    cost_val, _ = sess.run([cost, train], feed_dict={x: x_data, y:y_data})
    if step % 200 == 0;
      print(step, cost_val)
  
  h, c, a = sess.run([hypothesis, predicted, accuracy],
                      feed_dict={x:x_data, y:y_data})
  print("\nHypothesis: ", h, "\nCorrect (Y): ", c, "\nAccuracy: ", a)
~~~
