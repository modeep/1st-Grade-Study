# ML lab 05
## ML lab 05: TensorFlow로 Logistic Classification의 구현하기 (new)
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
학습

## ML lab 5-1 Logistic Classification의 가설 함수 정의

Classification : 기존의 가장 근접한 값을 구하는 것과는 달리 둘중에 1개를 정해진 카테고리 안에서 구하는 것이다.
페이스북에서 이용하는 기술로 여러가지의 타임라인 중에서 몇 가지만을 뽑아서 우리에게 보여준다.

0과 1로 나타내기 때문에

Span Detection: Spam or Ham
Facebook feed:show or hide
Credit Card Fraudulent Transaction detection: legitimate/fraud

Linear Regression한 모델을 학습시키면 Y축은 0~1까지 있고 X축은 무한이 있게 된다. 학습된 모델의 선이 0부터 시작되어 1 끝에 만나게 될 것이다. 그래서 무한히 X축이 늘어난다고 해서 X가 5던 10이던 똑깥이 Y는 1이 된다는 것이다. 그리서 우리는 어느 정도부터가 1이 되고 어느정도 까지가 0으로 Y의 결과값이 나오는지를 구하는 것이 우리의 목표이다.

H(x) = Wx + b의 결과 값이 0~1의 값으로 나와야 하기 때문에 H에 시그모이드 함수를 사용한다.


## ML lec 5-2 Logistic Regression의 cost 함수 설명

Logistic Regression의 cost function을 나타내면 U자로 울퉁불퉁하게 그려진다
시작하는 점에 따라서 도착 지점이 달라지게 된다.
중간에 걸리는 부분이 Local Miniminima, 최종적으로 도착해야하는 목표 점이 Global Mininima이다.
