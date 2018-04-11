# ML lec 03 - Linear Regression의 cost 최소화 알고리즘의 원리 설명

## 1. Summary

### [Hypothesis and Cost]

가설의 값에서 실제 값 차이를 제곱하여 총 더하고 평균을 구하는 것이 Cost Function이다.  여기서 Cost를 최소화하는 W와 b를 구하는 것이 Linear Regression이다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab3%20Image/Image1.PNG?raw=true)

<br/>
<br/>

### [Simplified hypothesis]

간략하게 표현하기  b를 0으로 하였다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab3%20Image/Image2.PNG?raw=true)

<br/>
<br/>

## 2. Cost Function

### [What cost(W) looks like?]

![img](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab3%20Image/Image3.PNG?raw=true)

<br/>

> $$
> W=1, cost(w)=0
> $$
>
> 
> $ {1 \over 3}((1 * 1 - 1)^2 + (1 * 2 - 2)^2 + (1 * 3 - 3)^2) $
> 
>
> 

<br/>

> $$
> W=0,cost(w)=4.76
> $$
>
> $$
> {3 \over 1}((0 * 1-1)^2 + (0 * 2-2)^2 +  (0 * 3-3)^2)
> $$
>
> 

<br/>
<br/>

우리가 가지고 있는 데이터로 그래프를 그리면 밑과 같은 형태로 만들어진다. 우리의 목적은 cost가 최소화되는 점을 찾는 것이다. 이 점을 기계적으로 찾아 내는 것이 Gradient descent algorithm이다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab3%20Image/Image4.PNG?raw=true)

<br/>

<br/>

### [Gradient descent algorithm]

Grdient : 경사, descent : 내려감

Gradient descent algorithem :경사를 따라 내려가는 알고리즘

수 많은 Cost Function 값 중 가장 Minimize한 Cost를 찾는 과정이다. 랜덤 값 부터 점점 경사도를 내리면서 경사도가 0이 되면 그 값이 제일 Minimize한 값이 된다. 장점은 항상 최저점에 도달 할 수 있다는 것이다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab3%20Image/Image5.PNG?raw=true)

<br/>
<br/>

미분을 적용할 때 좀더 쉽게 하기 위해서  m -> 2m으로 2를 붙인다. 똑같은 의미를 지니기 때문에 문제는 없다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab3%20Image/Image6.PNG?raw=true)

<br/>

cost(W) Function을 미분한 것을 곱해준다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab3%20Image/Image7.PNG?raw=true)

<br/>

생략 과정.

여러번 반복하면 W값이 변하게 되는데 그 값이 cost를 Minimize하는 과정이 만들어지게 된다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab3%20Image/Image8.PNG?raw=true)

<br/>

<br/>

### [IMPORT]

$$
W := W -\alpha {1 \over m}\sum_{i=1}^m(Wx^{(i)} - y^{(i)})x^{(i)}
$$

<br/>

<br/>

### [Convex Function]

Cost Function을 밑 처럼 그려질 수도 있다. 밑 그래프에 2가지의 경로가 예시로 나와 있는데 시작점의 위치에 따라 경사도를 따라 내려오면 도착지점이 다르다는 것을 알 수가 있다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab3%20Image/Image9.PNG?raw=true)



<br/>

이럴 경우를 대비해서 Convex Function을 사용한다. 어느 시작점이든 관계 없이 항상 경사도를 따라 내려와도 도착지점은 같게 된다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab3%20Image/Image10.PNG?raw=true)

<br/>
<br/>

## 3. Minimizing Cost Tensorflow

### [IMPORT]

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab3%20Image/Image11.PNG?raw=true)

<br/>

matplotlib 설치 : http://matplotlib.org/users/installing.html

### [SOURCE CODE]

> ~~~python
> import tensorflow as tf
> import matplotlib.pylab as plt
> x = [1, 2, 3]
> y = [1, 2, 3]
>
> w = tf.placeholder(tf.float32)
> hypothesis = x * w
>
> cost = tf.reduce_mean(tf.square(hypothesis - y))
> sess = tf.Session()
> sess.run(tf.global_variables_initializer())
>
> w_val = []
> cost_val = []
> for i in range(-30, 50):
>     feed_w = i * 0.1
>     curr_cost, curr_w = sess.run([cost, w], feed_dict={w: feed_w})
>     w_val.append(curr_w)
>     cost_val.append(curr_cost)
>
> plt.plot(w_val, cost_val)
> plt.show()
>
> ~~~
>
> > ~~~python
> > hypothesis = x * w
> > ~~~
> >
> > $$
> > H(x)=Wx
> > $$
> >
>
> > ~~~python
> > cost = tf.reduce_mean(tf.square(hypothesis - y))
> > ~~~
> >
> > $$
> > cost(W)={1 \over m}\sum_{i=1}^m(Wx^{(i)}-y^{(i)})^2
> > $$
> >
>
> > ~~~python
> > w_val = []
> > cost_val = []
> > for i in range(-30, 50):
> >     feed_w = i * 0.1
> >     curr_cost, curr_w = sess.run([cost, w], feed_dict={w: feed_w})
> >     w_val.append(curr_w)
> >     cost_val.append(curr_cost)
> > ~~~
> >
> > 실행시키면서 w, cost를 저장할 배열을 만들고 -3 ~ 5 까지 0.1 간격으로 움직이도록 for문을 돌렸다. 
>
> > 실행 결과
> >
> > ![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab3%20Image/Image12.PNG?raw=true)

<br/>
<br/>

### [Gradient descent algorithum]

 
$$
cost(W)={1 \over m}\sum_{i=1}^m(Wx^{(i)} - y^{(i)})^2
$$
W - cost Function의 기울기를 빼주면 된다.
$$
W := W -\alpha {1 \over m}\sum_{i=1}^m(Wx^{(i)} - y^{(i)})x^{(i)}
$$

~~~python
learning_rate = 0.1
gradient = tf.reduce_mean((W * X - Y) * X)
descent = W - learning_rate * gradient
update = W.assign(descent)
~~~

<br/>

<br/>

#### [SOURCE CODE]

> ~~~python
> import tensorflow as tf
> x_data = [1, 2, 3]
> y_data = [1, 2, 3]
>
> w = tf.Variable(tf.random_normal([1]), name='weight')
> y = tf.placeholder(tf.float32)
> x = tf.placeholder(tf.float32)
> hypothesis = x * w
>
> cost = tf.reduce_sum(tf.square(hypothesis - y))
>
> learning_rate = 0.1
> gradient = tf.reduce_mean((w * x - y) - y)
> descent = w - learning_rate * gradient
> update = w.assign(descent)
>
> sess = tf.Session()
> sess.run(tf.global_variables_initializer())
>
> w_val = []
> cost_val = []
> for step in range(21):
>     sess.run(update, feed_dict={x: x_data, y: y_data})
>     print(step, sess.run(cost, feed_dict={x: x_data, y: y_data}), sess.run(w))
>
> ~~~
>
> > ~~~python
> > w = tf.Variable(tf.random_normal([1]), name='weight')
> > y = tf.placeholder(tf.float32)
> > x = tf.placeholder(tf.float32)
> > ~~~
> >
> > w는 랜덤 값을 주고 y, x를 값을 넘겨주려고 한다.
>
> > ~~~python
> > learning_rate = 0.1
> > gradient = tf.reduce_mean((w * x - y) - y)
> > descent = w - learning_rate * gradient
> > update = w.assign(descent)
> > ~~~
> >
> > $$
> > W := W -\alpha {1 \over m}\sum_{i=1}^m(Wx^{(i)} - y^{(i)})x^{(i)}
> > $$
> >
>
> > 실행 결과.
> >
> > 반복 할 수록 cost 값이 작아지고 w는 1에 가까워 진다.
> >
> > ![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab3%20Image/Image13.PNG?raw=true)

<br/>

<br/>

cost가 쉽게 주어졌지만 복잡하게 주어질 경우.

~~~python
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train = optimizzer.minimize(cost)
~~~

Tensorflow에서 Optimizer를 통해 cost를 Minimize 해준다.

<br/>

> ~~~python
> import tensorflow as tf
> x = [1, 2, 3]
> y = [1, 2, 3]
>
> w = tf.Variable(5.0)
>
> hypothesis = x * w
>
> gradient = tf.square(hypothesis - y)
> cost = tf.reduce_mean(tf.square(hypothesis - y))
> optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
> train = optimizer.minimize(cost)
>
> sess = tf.Session()
> sess.run(tf.global_variables_initializer())
>
> for step in range(100):
>     print(step, sess.run(w))
>     sess.run(train)
> ~~~
>
> > ~~~python
> > w = tf.Variable(5.0)
> > ~~~
> >
> > ![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab3%20Image/Image14.PNG?raw=true)
>
> > ~~~python
> > w = tf.Variable(-3.0)
> > ~~~
> >
> > ![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab3%20Image/Image15.PNG?raw=true)

<br/>

<br/>

> ~~~python
> import tensorflow as tf
> x = [1, 2, 3]
> y = [1, 2, 3]
>
> w = tf.Variable(-3.0)
>
> hypothesis = x * w
>
> gradient = tf.reduce_mean((w * x - y) * x) * 2
> cost = tf.reduce_mean(tf.square(hypothesis - y))
> optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
>
> gvs = optimizer.compute_gradients(cost)
> apply_gradients = optimizer.apply_gradients(gvs)
>
> sess = tf.Session()
> sess.run(tf.global_variables_initializer())
>
> for step in range(100):
>     print(step, sess.run([gradient, w, gvs]))
>     sess.run(apply_gradients)
> ~~~
>
> > ~~~python
> > gvs = optimizer.compute_gradients(cost)
> > apply_gradients = optimizer.apply_gradients(gvs)
> > ~~~
> >
> > gradients 출력, gradients apply
>
> > ~~~python
> > gradient = tf.reduce_mean((w * x - y) * x) * 2
> > ~~~
> >
> > ~~~python
> > gvs = optimizer.compute_gradients(cost)
> > apply_gradients = optimizer.apply_gradients(gvs)
> > ~~~
> >
> > 수식을 사용하여 계산한 값과 자동으로 계산된 gradients의 값이 같은지 비교해보자.
> >
> > ![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab3%20Image/Image16.PNG?raw=true)

<br/>

<br/>

## [출처]

1. 모두를 위한 머신러닝/딥러닝 강의 https://hunkim.github.io/ml/
