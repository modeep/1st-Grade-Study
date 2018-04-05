# ML lec 02 - Linear Regression의 Hypothesis 와 cost 설명
## 1. Linear Regression

### [Training]

데이터를 가지고 학습을 하는 것을 'Training'이라고 하며 데이터를 'Training Data' 라고 한다.

![](./ML\ lab2\ Image/Image1.jpg)
<br/>
<br/>
### [Linear and Regression]

 Regression을 학습을 할 때 가설을 세울 필요가 있으며 가설을 세우는 것이 Linear Regression이다. Linear하게 가설을 세운다는 것은 데이터가 있다면 데이터에 알맞은 Linear한 선을 찾는 것이다. 그리고 이 선을 찾는 과정이 학습을 하는 것이다.

![](C:\Users\jkl81\Desktop\사진3.PNG)
<br/>
<br/>
## 2. Cost Function

### [Cost Function Concepts]

여러가지의 선이 만들어지면 어떤 선이 데이터에 적합한지를 찾아야 한다. 데이터와 가설로 만들어진 선의 거리를 측정하여 실제 데이터 값과 어느정도 차이가 있는지를 구하는 과정을 Cost Function이라고 한다.

![](C:\Users\jkl81\Desktop\사진5.PNG)
<br/>
<br/>
### [IMPORTANT]

~~~
H(x) = Wx + b
~~~
<br/>
<br/>

### [GETTIING DISTANCE]

~~~
H(x) - y
~~~

를 통해 구할 수 있다. 그러나 음수일 경우는 결과가 이상하기 때문에

~~~
(H(x) - y)<sup>2</sup>
~~~

 (H(x) - y)<sup>2</sup>를 사용한다.
<<<<<<< HEAD

=======
 
>>>>>>> f56b49270362a14e06c86f539f8cb52d0218c4d6
<br/>
<br/>


### [GOAL]

Cost(W, b), 가장 작은 W, b를 구하자!
<br/>
<br/>

## 3. Hypothesis and Cost


### [IMPORT]

![](C:\Users\jkl81\Desktop\사진6.PNG)

~~~H(x) = Wx + b
H(x) = Wx + b
~~~

W와 b를 정의 하는데 다른 프로그램과 같이 변수라는 개념이 아닌 텐서플로우에서는 Variable이라는 Node로 정의 할 수 있다.
<br/>
<br/>

### [SOURCE CODE]

> ~~~
> H(x) = Wx + b
> ~~~
>
> > ~~~python
> > # x, y data
> > x_train = [1, 2, 3]
> > y_train = [1, 2, 3]
> >
> > w = tf.Variable(tf.random_normal([1]), name = 'weight')
> > b = tf.Variable(tf.random_normal([1]), name = 'bias')
> >
> > # hypothesis = x * w + b
> > hypothesis = x_train * w + b
> > ~~~
> >
> > > ~~~python
> > > tf.random_normal([1])
> > > ~~~
> > >
> > > 1차원의 랜덤 값을 입력한다.
> > >
> > > ~~~python
> > > Hypothesis = x_train * w + b
> > > ~~~
> > >
> > > Hypothesis는 cost(W, b) 값을 얻기 위해 사용된다.

<br/>
<br/>

> ![](C:\Users\jkl81\Desktop\사진7.PNG)	
>
> > ~~~python
> > # cost/Loss function
> > cost = tf.reduce_mean(tf.square(hypothesis - y_train))
> > ~~~

<br/>
<br/>

> ~~~
> GradientDescent
> ~~~
>
> > ~~~python
> > # Minimize
> > optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
> > train = optimizer.minimize(cost)
> > ~~~
> >
> > > cost를 가장 작은 값을 구해야 하기 때문에 GradientDescent를 사용한다.

<br/>
<br/>

> ~~~
> Run/update graph and get results
> ~~~
>
> > ~~~python
> > sess = tf.Session()
> > sess.run(tf.global_variables_initializer())
> >
> > for step in range(2001):
> > 	sess.run(train)
> > 	if step % 20 == 0:
> > 		print(step, sess.run(cost), sess.run(W), sess.run(b))
> > ~~~
> >
> > > 실행하기 위해서 Session을 만들고 for문을 사용해서 2000번을 반복한다. 그리고 중간에 진행도를 알기 위해서 if문으로 20번 마다 cost, W, b를 출력하게 만들었다.

<br/>
<br/>

> ~~~
> Placeholders Full source
> ~~~
>
> > ~~~python
> > W = tf.Variable(tf.random_normal([1]), name = 'weight')
> > b = tf.Variable(tf.random_normal([1]), name = 'bias')
> > X = tf.placeholder(tf.float32, shape=[None])
> > Y = tf.placeholder(tf.float32, shape=[None])
> >
> > hypothesis = X * W + b
> > cost = tf.reduce_mean(tf.square(hypothesis - Y))
> > optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
> > train = optimizer.minimize(cost)
> >
> > sess = tf.Session()
> > sess.run(tf.global_variables_initializer())
> >
> > for step in range(2001):
> > 	cost_val, W_val, b_val, _ = \
> > 		sess.run([cost, W, b, train],
> > 			feed_dict={X: [1, 2, 3], Y: [1, 2, 3]})
> > if step % 20 == 0:
> > 	print(step, cost, val, W val, b val)
> > ~~~
> >
> > > ~~~python
> > > x_train = [1, 2, 3]
> > > y_train = [1, 2, 3]
> > > ~~~
> > >
> > > 이 아닌
> > >
> > > ~~~python
> > > X = tf.placeholder(tf.float32)
> > > Y = tf.placeholder(tf.float32)
> > > ~~~
> > >
> > > 으로 바꿔 사용할 수 있다.
> > >
> > > Placeholder를 사용하면 train을 실행 시킬 때 x, y를 넘겨 줄 수 있다.

<br/>
<br/>

## [출처]

1. 모두를 위한 머신러닝/딥러닝 강의 https://hunkim.github.io/ml/
