#2018/4/11 Lab 1#

텐서플로우: 구글에서 만든 오픈소스 라이브러리.

​		     텐서플로우가 머신러닝 라이브러리 중 최고이다.

만들어놓은 그래프 속에서 데이터(*tens*)가 흐른다 하여 *tensorflow* 이다.



1.그래프 정의.

2.sess.run으로 그래프 실행.

3.내부 필요성을 업데이트.

의 순서로 실행괸다.



import tensorflow as tf (**선언**)

hello = tf.constant("hello")

sess = tf.Session()

print(sess.run(hello))

result : b'hello' (**b 는 bytes lterals 의 약자이다.**)



그래프에서 값을 넣은 뒤 프린트 값을 정상적으로 출력하려면 sess.run 을 사용해야 한다.



*Ranks.*

0  : *scalar*. ex)485

1 : *vector*.  ex)[1. 1, 2. 2, 3. 3]

2 :*matrix*   ex)[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

3 :*3-tensor*

이렇게 한 차원씩 늘어난다.



*Shapes*

0: []

1: [D0]

2: [D0, D1]

3: [D0, D1, D2]

4: [D0, D1, ... Dn-1]



*Type*

float, double, int8~64 등이 있다.





