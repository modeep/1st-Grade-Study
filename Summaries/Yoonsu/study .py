import tensorflow as tf

x_train = [1, 2, 3]                                                       #x_train 데이터 입력
y_train = [1, 2, 3]                                                       #y_train 데이터 입력

W = tf.Variable(tf.random_normal([1]), name='weight')                    #W를 Variable(텐서플로우가 자체적으로 변경하는 값)으로, 랭크 1의 값으로 정의
b = tf.Variable(tf.random_normal([1]), name='bias')                      #b를 Variable로 랭크 1의 값으로 정의

hypothesis = x_train * W + b                                              #hypothesis 정의

cost = tf.reduce_mean(tf.square(hypothesis - y_train))                    #cost함수 정의 reduce_mean 은 평균을 내는 값.

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)                                          #cost 함수fmf 최소값으로 최적화 하라고 정의.

sess = tf.Session()                                                       #session에서 graph실행

sess.run(tf.global_variables_initializer())                               #session에서 사용될 변수 초기화

for step in range(2001):                                                 #2000번 반복
    sess.run(train)
    if step % 20 == 0:                                                    #20번 마다 한 번 씩 출력
        print(step, sess.run(cost), sess.run(W), sess.run(b))



import tensorflow as tf
W =tf.Variable(tf.random_normal([1]),name='weight')                     #variable 선언
b =tf.Variable(tf.random_normal([1]),name='bias')
X = tf.placeholder(tf.float32, shape=[None])                            #placeholder로 변수에 대한 틀을 만들고 나중에 변수에 값을 입력
Y = tf.placeholder(tf.float32, shape =[None])                           #나중에 feed_dict로 변수에 대한 값을 넘겨 줄 수 있다.
hypothesis = W*X+b      #가설 = W*X + b
cost = tf.reduce_mean(tf.square(hypothesis - Y))                         #cost Funstion를 정의 reduce_mean은 텐서가 주어졌을때 그 값을 평균 내주는 것이다.

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)        #어떠한 값의 최소값을 찾는 것   optimization = 최적화
train = optimizer.minimize(cost)                                         #train = cost의 최소값

sess = tf.Session()                                                      #session에서 graph실행

sess.run(tf.global_variables_initializer())                              #session에서 사용될 변수 초기화

for step in range(2001):                                                #2000번 정도 실행을 시켜라
    cost_val, w_val, b_val, _ = sess.run([cost,W,b,train],               #cost_val, w_val등의 값은 각각 cost,W를 학습한 값과 같다.
        feed_dict={X: [1,2,3,4,5],
                   Y: [2.1, 3.1, 4.1, 5.1, 6.1]})
    if step % 20 == 0:                                                   #20번에 한 번 씩 값을 출력해봄
        print(step,cost_val, w_val, b_val)