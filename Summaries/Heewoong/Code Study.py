import tensorflow as tf

x_train = [1, 2, 3]                                                      #x_train 데이터 입력
y_train = [1, 2, 3]                                                      #y_train 데이터 입력

W = tf.Variable(tf.random_normal([1]), name='weight')                   #W를 Variable(텐서플로우가 자체적으로 변경하는 값)으로, 랭크 1의 값으로 정의
b = tf.Variable(tf.random_normal([1]), name='bias')                     #b를 Variable로 랭크 1의 값으로 정의

hypothesis = x_train * W + b                                             #hypothesis 정의

cost = tf.reduce_mean(tf.square(hypothesis - y_train))                   #cost함수 정의 reduce_mean 은 평균을 내는 값.

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)                                         #cost 함수를 minimize 하라고 정의.

sess = tf.Session()                                                      #세션 만들기

sess.run(tf.global_variables_initializer())                              # variable을 실행하기 전에는 global_variables_initializer()를 넣어야만 한다.

for step in range(2001):                                                #2000번 반복.
    sess.run(train)                                                      #노드 실행
    if step % 20 == 0:                                                   #20번마다 출력.
        print(step, sess.run(cost), sess.run(W), sess.run(b))            #cost, W, b의 값을 보이게 함.



import tensorflow as tf
W =tf.Variable(tf.random_normal([1]),name='weight')                     #변수 선언.
b =tf.Variable(tf.random_normal([1]),name='bias')                       #변수 선언.
X = tf.placeholder(tf.float32, shape=[None])                            #placeholder로 변수에 대한 틀을 만들기. 나중에 값 입력 가능.
Y = tf.placeholder(tf.float32, shape =[None])                           #나중에 feed_dict로 변수에 대한 값을 넘겨 줄 수 있음.
hypothesis = W*X+b      #가설 = W*X + b
cost = tf.reduce_mean(tf.square(hypothesis - Y))                         #cost 함수 정의. reduce_mean은 값의 평균을 구하는 것.

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)                                         #cost 함수를 minimize 하라고 정의.

sess = tf.Session()                                                      #세션 만들기.

sess.run(tf.global_variables_initializer())                              #variable을 실행하기 전에는 global_variables_initializer()를 넣어야만 한다.

for step in range(2001):                                                #2000번 반복.
    cost_val, w_val, b_val, _ = sess.run([cost,W,b,train],               #cost_val, w_val등의 값은 각각 cost,W를 학습한 값과 같음.
        feed_dict={X: [1,2,3,4,5],
                   Y: [2.1, 3.1, 4.1, 5.1, 6.1]})
    if step % 20 == 0:                                                   #20번마다 출력.
        print(step,cost_val, w_val, b_val)