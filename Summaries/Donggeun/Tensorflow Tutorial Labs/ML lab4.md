# ML lec 04 - multi-variable linear regression
## Summary
우리는 지금까지 가설을 세우는 Hypothesis,예측한 값과 실제 값을 비교하여 오차를 구하는 Cost Function,Cost 함수의 그래프에서 Cost가 최적화가 되는 값을 찾는 Gradient descent algorithm을 배웠다.

기존의 Variable은 1개였다.
![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab4%20Image/Image1.PNG?raw=true)

하지만 3개인 경우에는 어떻게 해야 할까?
![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab4%20Image/Image2.PNG?raw=true)

## Matrix
### Hypothesis
변수 3개를 받아와서 변수와 가중치를 각각 곱해준 다음에 더해주면 된다.
![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab4%20Image/Image3.PNG?raw=true)

### Cost Function
Cost Function은 그대로 가설에서 실제 값을 빼주고 제곱을 해주면 된다.
![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab4%20Image/Image4.PNG?raw=true)

### Multi-Variable Occation
지금까지는 3개였지만 수백, 수천개의 Variable이 있을 경우에는 수식으로 표현하기가 힘들어진다.
![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab4%20Image/Image5.PNG?raw=true)

### Matrix Multiplication
![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab4%20Image/Image6.PNG?raw=true)

Matrix Multiplication방식을 Hypothesis에 적용시킨 모습이다.
(X와 W의 자리는 상관 없다.)
![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab4%20Image/Image7.PNG?raw=true)

Variable를 가지고 Matrix를 사용해서 가설을 세운다.
(Instance)
![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab4%20Image/Image8.PNG?raw=true)

Variable의 Instance가 다섯일 경우에는 가설 또한 다섯 Instance를 출력한다. Variable의 개수와 W(Weight)의 Instance 개수가 같다. 가설의 Y(1)와 W(1)이 같다는 것을 알 수 있다. 이러한 관계를 이해 해야지만 Variable이 주어지고 출력 방식이 정해졌을 때 W의 크기를 구할 수가 있다.
![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab4%20Image/Image9.PNG?raw=true)

## Question
![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab4%20Image/Image10.PNG?raw=true)

<br/>

# ML lab 04-1: multi-variable linear regression을 TensorFlow에서 구현하기 (new)
## 기존의 방법으로 Linear Regression 구현
~~~
import tensorflow as tf

x1_data = [73., 93., 89., 96., 73.]
x2_data = [80., 88., 91., 98., 66.]
x3_data = [75., 93., 90., 100., 70.]
y_data = [152., 185., 180., 196., 142.]

x1 = tf.placeholder(tf.float32)
x2 = tf.placeholder(tf.float32)
x3 = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

w1 = tf.Variable(tf.random_normal([1]), name='weight1')
w2 = tf.Variable(tf.random_normal([1]), name='weight2')
w3 = tf.Variable(tf.random_normal([1]), name='weight3')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = x1 * w1 + x2 * w2 + x3 * w3 + b

cost = tf.reduce_mean(tf.square(hypothesis - y))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train],
                                   feed_dict={x1: x1_data, x2: x2_data, x3: x3_data, y: y_data})
    if step % 20 == 0:
        print(step, cost_val, sess.run(w1), sess.run(w2), sess.run(w3), sess.run(b), "\nPrediction : \n", hy_val)
~~~

## Matrix-Variable Linear Regression 구현
지금은 X의 Variable이 3개 밖에 없지만 수백, 수천개라면 복잡해지고 Instance를 추가를 할 때마다 밑의 코드도 수정해줘야 하는 번거로움이 존재한다. 이를 해결하고자 Matrix를 사용한다.
~~~
import tensorflow as tf

x_data = [[73., 80., 75.],
          [93., 88., 93.],
          [89., 91., 90.],
          [96., 98., 100.],
          [73., 66., 70.]]
y_data = [[152.], [185.], [180.], [196.], [142.]]

x = tf.placeholder(tf.float32, shape=[None, 3])
y = tf.placeholder(tf.float32, shape=[None, 1])

w = tf.Variable(tf.random_normal([3, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = tf.matmul(x, w) + b

cost = tf.reduce_mean(tf.square(hypothesis - y))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train],
                                   feed_dict={x: x_data, y: y_data})
    if step % 20 == 0:
        print(step, cost_val, sess.run(w), sess.run(b), "\nPrediction : \n", hy_val)
~~~
Matrix를 사용하면서 전체적인 소스코드의 길이가 줄어들었고 X의 Instance를 추가하기 위해서는 x_data Variable에 추가만 해주면 된다.

<br/>

# ML lab 04-2: TensorFlow로 파일에서 데이타 읽어오기 (new)

## Summary
x_data를 기존에는 Tensorflow 내부에서 Veriable로 선언하였지만 이번 목표는 외부, 즉 .csv 데이터 파일을 읽어와 x_data로 사용하는 것이다.

##Slicing
.csv 데이터를 불러와 .csv 데이터중 일정부분만이 필요할 때가 있다. 이 때 Slicing 기능을 사용한다.

~~~
nums = range(5)
print(nums) # prints "[0, 1, 2, 3, 4]"
prin(nums[2:4]) # prints "[2, 3]"
print(nums[2:] )# prints "[2, 3, 4]"
print(nums[:2]) # prints "[0, 1]"
printnums[:]) # prints "[0, 1, 2, 3, 4]"
print(nums[:-1]) # prints "[0, 1, 2, 3]"
ums[2:4] = [8, 9] # 2~3 공간에 [8, 9]를 추가
print(nums) # prints [0, 1, 8, 9, 4]
~~~

## Numpy
~~~
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# array = ([[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12]])

b[:, 1]
# array([2, 6, 10])

b[-1]
# array([9, 10, 11, 12])

b[-1, :]
# array([9, 10, 11, 12])

b[-1, ...]
# array([9, 10, 11, 12])

b[0:2, :]
# array([[1, 2, 3, 4],
#        [5, 6, 7, 8]])
~~~

## Loading data from file
data_file.csv
~~~
# EXAM1,EXAM2,EXAM3,FINAL
73,80,75,152
93,88,93,185
89,91,90,180
96,98,100,196
73,66,70,142
53,46,55,101
~~~

Python Numpy
~~~
import numpy as np

xy = np.loadtxt('data_file.csv', delimiter=',', dtype=np.float32)
x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]

# prints data
print(x_data.shape, x_data, len(x_data))
print(y_data.shape, y_data)
~~~

Python TensorFlow
~~~
import tensorflow as tf
import numpy as np
tf.set_random_seed(777)

xy = np.loadtxt('data_file.csv', delimiter=',', dtype=np.float32)
x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]

print(x_data.shape, x_data, len(x_data))
print(y_data.shape, y_data)

x = tf.placeholder(tf.float32, shape=[None, 3])
y = tf.placeholder(tf.float32, shape=[None, 1])
w = tf.Variable(tf.random_normal([3, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')
hypothesis = tf.matmul(x, w) + b
cost = tf.reduce_mean(tf.square(hypothesis - y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train = optimizer.minimize(cost)
sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(2001):
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train],
                                   feed_dict={x: x_data, y: y_data})
    if step % 20 == 0:
        print(step, cost_val, sess.run(w), sess.run(b), "\nPrediction : \n", hy_val)

print("Your score will be ", sess.run(hypothesis, feed_dict={x: [[100, 70, 101]]}))
~~~

## Queue Runners
File이 엄청 커서 numpy로 한번에 메모리에 올리기 힘들 때 사용.

1. 여러개의 파일을 읽어와 Queue에 Stack 형태로 쌓는다.
2. 그 후 Reader로 읽어온다.
3. Reader로 읽어온 값을 Decoding 해준다음에 Queue에 쌓는다.

그 후 학습을 할 때 필요한 데이터만 불러와 사용하면 된다. 이 모든 과정을 TensorFlow가 처리한다.
![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab4%20Image/Image11.PNG?raw=true)

## Tensorflow Source Code
Frist
~~~
filename_queue = tf.train.string_input_producer(
  ['data-01-test-score.csv', ['data-02-test-score.csv', ....],
  shuffle=false, name='filename_queue')
~~~

Second
~~~
reader = tf.TextLineReader()
Key, value = reader.read(filename_queue)
~~~

Third
~~~
record_defaults = [[0.], [0.], [0.], [0.]]
xy = tf.decode_csv(value, record_defaults=record_defaults)
~~~

## tf.train.batch
TensorFlow에 batch라는 것을 만들어 놨는 batch를 가지고 읽어오게 한다.
~~~
# collect batches of csv in
train_x_batch, train_y_batch = \
  tf.train.batch([xy[0:-1], xy[-1:]], batch_size-10)

  sess =  tf.Session()
  ...

# Start populating the filename queue.
  coord = tf.train.Coordinator()
  threads = tf.train.start_queue_runners(sess=sess, coord=coord)

  for step in range(2001):
    # x_batch와 y_batch로 넘겨준다.
    x_batch, y_batch = sees.run([train_x_batch, train_x_batch])
    ...

coord.request_stop()
coord.join(threads)
~~~

Python TensorFlow
~~~
import tensorflow as tf

filename_queue = tf.train.string_input_producer(
  ['data-01-test-score.csv', ['data-02-test-score.csv', ....],
  shuffle=false, name='filename_queue')

reader = tf.TextLineReader()
Key, value = reader.read(filename_queue)

record_defaults = [[0.], [0.], [0.], [0.]]
xy = tf.decode_csv(value, record_defaults=record_defaults)

train_x_batch, train_y_batch = \
  tf.train.batch([xy[0:-1], xy[-1:]], batch_size-10)

x = tf.placeholder(tf.float32, shape=[None, 3])
y = tf.placeholder(tf.float32, shape=[None, 1])

w = tf.Variable(tf.random_normal([3, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = tf.matmul(x, w) + b

cost = tf.reduce_mean(tf.square(hypothesis - y))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

coord. tf.train.Coordinator()
threads = tf.train.start_queue_runners(sess=sess, coord=coord)

for step in range(2001):
  # x_batch와 y_batch로 넘겨준다.
  x_batch, y_batch = sees.run([train_x_batch, train_x_batch])
  cost_val, hy_val, _ = sess.run([cost, hypothesis, train],
    feed_dict={x: x_data, y: y_data})

    if step % 20 == 0:
        print(step, "Cost: ", cost_val, "\nPrediction : \n", hy_val)

coord.request_stop()
coord.join(threads)
~~~

## [출처]
1. 모두를 위한 머신러닝/딥러닝 강의 https://hunkim.github.io/ml/
