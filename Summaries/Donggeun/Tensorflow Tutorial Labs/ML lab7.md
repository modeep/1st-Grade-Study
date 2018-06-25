# lec 07-1: 학습 rate, Overfitting, 그리고 일반화 (Regularization)
## Gradient descent
우리는 Gradient descent에서 Learning_rate를 임의로 정해주었다.
그러나 Learning_rate의 값이 매우 크게 설정하면 오버슈팅(Overshoting)이 발생할 수 있다. 오버슈팅은 쉽게 말해서 Cost가 줄어들지 않고 값자기 증가하는 현상을 말한다.
Learning_rate를 작게 설정하면 매우 느리게 내려가서 우리가 반복을 설정한 값이 끝날때 우리가 원하는 Cost에 도달하기도 전에 끝날 수도 있다.

## Data(X) preprocessing for gradient descent
여기에서는 그래프가 동고선과 같은 형태로 나타난다.
여기서도 Gradient descent와 같이 오버슈팅이 발생할 수 있다.
데이터의 범위가 클 경우에는 zero-centered data나 Normalize를 하여 중심점을 중앙으로 잡아주고 전체적인 분포도를 줄여준다.
</br>
### Standardization
x_std[:, 0] = (x[:, 0] - X[:, 0].mean()) / X[:, 0].std()

## Overfitting
우리가 머신러닝의 학습을 통해서 모델을 만들어 갈때 우리가 학습데이터에 맞는 모델을 만들어 낼 수 있다. 하지만 실행해보면 잘 맞지 않을 때가 있다.
오버슈팅을 줄일 수 있는 방법...
1. 최대한 많은 트레이닝 데이터를 사용한다.
2. 우리가 가지고 있는 features의 중복을 줄인다.
3. Regularization을 사용.

### Regularization
가중치(Weight)를 최대한 일반화 시킨다는 것이다.
우리가 기존에 사용했던 Cost Function에서 뒤에 regularization straight를 더해준다.
파이썬에서는...
~~~
l2reg = 0.001 * tf.reduce_sum(tf.square(W))
~~~
