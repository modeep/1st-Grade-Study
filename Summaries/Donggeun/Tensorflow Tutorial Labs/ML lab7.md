# lec 07-1: 학습 rate, Overfitting, 그리고 일반화 (Regularization)
## Gradient descent
우리는 지금까지 Gradient descent에서 Learning_rate를 임의로 정해주었다.(보통 0.001 ~0.01)

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab7/Image1.png?raw=true)

그러나 Learning_rate의 값을 매우 크게 설정하면 오버슈팅(Overshoting)이 발생할 수 있다. 오버슈팅은 쉽게 말해서 Cost가 줄어들지 않고 값자기 증가하는 현상을 말한다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab7/Image2.png?raw=true)

Learning_rate를 작게 설정하면 매우 느리게 내려가서 우리가 횟수를 설정한 값이 끝날때 우리가 원하는 Cost에 도달하기도 전에 끝날 수도 있다.

## Data(X) preprocessing for gradient descent

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab7/Image3.png?raw=true)

여기에서는 그래프가 동고선과 같은 형태로 나타난다.
이 그래프는 가운데가 낮아서 시작 지점에서 출발하면 가운데에 도착하게 된다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab7/Image5.png?raw=true)

데이터의 범위가 클 경우에는 zero-centered data나 Normalize를 하여 중심점을 중앙(0, 0)으로 잡아주고 전체적인 분포도를 줄여준다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab7/Image4.png?raw=true)

</br>

### Standardization

데이터를 쉽게 비교하기 위해서 Standardization을 사용한다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab7/Image6.png?raw=true)

우리가 계산한 평균과 분산 값을 가지고 나눠주면 된다.

## Overfitting

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab7/Image7.png?raw=true)

우리가 머신러닝의 학습을 통해서 모델을 만들어 갈때 우리가 학습데이터에 맞는 모델을 만들어 낼 수 있다. 하지만 실행해보면 잘 맞지 않을 때가 있다.
오버슈팅을 줄일 수 있는 방법...
1. 최대한 많은 트레이닝 데이터를 사용한다.
2. 우리가 가지고 있는 features의 중복을 줄인다.
3. Regularization을 사용.

### Regularization
가중치(Weight)를 최대한 일반화 시킨다는 것이다.(너무 큰 Weight를 가지지 말자, 최대한  Decent boundary를 펴자!)
우리가 기존에 사용했던 Cost Function에서 뒤에 regularization straight를 더해준다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab7/Image8.png?raw=true)

엘리먼트
~~~
l2reg = 0.001 * tf.reduce_sum(tf.square(W))
~~~

</br>
</br>

# lec 07-2: Training/Testing 데이타 셋

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab7/Image10.png?raw=true)

우리는 Training set을 가지고 학습을 시키는데 그 후에 Training set을 집어 넣어보면 이후의 값을 예측해서 출력할 것이다. 그러나 이것이 잘 됬다고 할 수 있는 것일까? 매우 나쁜 방법이다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab7/Image11.png?raw=true)

그래서 Training set에서 70%로는 학습을 시킬때 사용하고 나머지 30%는 학습이된 모델에 테스트를 해보는 용도로 사용해야 효율적으로 모델학습을 할 수 있다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab7/Image12.png?raw=true)

또한 70%에서도 2가지 Training과 Validation으로 나누어 Training으로는 모델학습에 사용하고 Validation은 학습된 모델에 어떠한 값이 좋을지 튜닝을 하는 것이다. 모의 테스트를 해보는 것이라고 할 수 있다.

</br>

## Online learning


![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab7/Image13.png?raw=true)

한번에 모든 데이터를 사용하여 학습을 시키면 메모리 공간이 부족할 수 있다.
100만개의 Training Data가 있다고 할 때 10만개씩 나눠서 학습을 시키는 방식을 말한다.
Ex. MNIST

</br>

# ML lab 07-1: training/test dataset, learning rate, normalization
이번 강의의 핵심은 Training Data를 2가지로 나누어 1가지는 직접적으로 모델을 학습할 때 사용하고 또 다른 하나는 모델 테스트를 할 때 사용한다. 테스트를 할 때에는 당연히 기존 데이터에서는 보지못한 데이터여야 할 것이다.

~~~
x = tf.placeholder("float", [None, 3])
y = tf.placeholder("float", [None, 2])
w = tf.Variable(tf.random_normal([3, 3]))
b = tf.Variable(tf.random_normal([3]))

hypothesis = tf.nn.softmax(tf.matmul(x, w) + b)
is_correct = tf.equal(prediction, tf.arg_max(y, 1))
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))

with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
	for step in range(201):
		cost_val, w_val, _ = sess.run([cost, w, optimizer], feed_dict={x: x_data, y: y_data})
		print(step, cost_val, w_val)
		
print("Prediction:", sess.run(Prediction, feed_dict={x: x_test}))
print("Accuracy: ", sees.run(accuracy, feed_dict={x: x_test, y: y_test}))
~~~

## Big or Small Learning

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab7/Image14.png?raw=true)

learning_rate를 크게 할 경우에는 오버슈팅이 발생하고 어떤 경우에는 [nan]을 출력하는 사태가 발생하기도 한다. (학습 포기)
반대로 매우 작게 설정을 하게 되면 Cost의 변경값이 너무 작아 학습을 반복되는 횟수를 늘릴 수 밖에 없게된다...

~~~
xy = np.array([[834, 343, 857, 989],
				[847, 826, 913, 428]])
xy = MinMaxScaler(xy)
~~~

가장 작은 값이 0이 되고 가장 큰 값이 1이 된다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab7/Image15.png?raw=true)

</br>

# ML lab 07-2: Meet MNIST Dataset

28x28xI image
가로, 세로 28개씩의 픽셀을 가진다. 총 784개의 픽셀이다.

~~~
X = tf.Placeholder(tf.float32, [None, 784])
Y = tf.placeholder(tf.float32, [None, nb_classes])
~~~

픽셀 처리

한꺼번에 메모리에 올리지 않고 100개씩 올린다.

~~~
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
...
batch_xs, batch_ys = mnist.train.next_batch(100)
...
print("Accuracy: ", accuracy.eval(session=sess,
          feed_dict={X: mnist.test.images, Y: mnist.test.labels}))
~~~

Reading data and set variables

class를 10개를 사용한다.
그리고 각각의 placeholder와 Variable의 Shape을 정해준다.

~~~
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

nb_classes = 10

X = tf.placeholder(tf.float32, [None, 784])
Y = tf.placeholder(tf.float32, [None, nb_classes])

w = tf.Variable(tf.random_normal([784, nb_classes]))
b = tf.Variable(tf.random_normal([nb_classes]))
~~~

</br>

### Softmax

~~~
hypothesis = tf.nn.softmax(tf.matmul(X, W) + b)

# 축을 1로 설정하고 합을 구한다.
cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), axis=1))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

# print True or False
is_correct = tf.equal(tf.arg_max(hypothesis, 1), tf.arg_max(Y, 1))
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
~~~

### Training epoch/batch

batch: 한번에 몇개씩 학습을 시키는가
epoch: 전체 데이터 셋을 몇번 학습을 시켰는지

~~~
# 전체 데이터 셋 15번 반복
training_epochs = 15
# 한번에 100개씩 학습
batch_size = 100

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    for epoch in range(training_epochs):
        avg_cost = 0
        # 만약 전체 데이터 셋이 10000개이고 batch_size가 100이면 나누어 주면 한번 데이터 셋을 학습을 시킬 때 100개씩 batch를 100번 학습을 해                  야한다.
        total_batch = int(mnist.train.num_examples / batch_size)
        
        # batch 반복
        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            c, _ = sess.run([cost, optimizer], feed_dict={X: batch_xs, Y: batch_ys})
            avg_cost += c / total_batch
            
        print('Epoch', '%04d' % (epoch + 1), 'cost =', '{:.9f}'.format(avg_cost))
~~~

### Report results on test dataset

학습한 모델 테스트

~~~
print("Accuracy: ", accuracy.eval(session = sess,
    feed_dict={X: mnist..test.images, Y: mnist.test.labels})) 
~~~
