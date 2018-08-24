# lec10-1: Sigmoid 보다 ReLU가 더 좋아

이와 같이 레이어 사이에 있는 함수들을 Activation function이라고 한다.

![](https://raw.githubusercontent.com/MoDeep/1st-Grade-Study/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab10%20Image/1.png)



![](https://raw.githubusercontent.com/MoDeep/1st-Grade-Study/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab10%20Image/2.png)

- W1은 Input Layer이고 2 크기로 들어오고 5 크기로 내보낸다.

- W2는 Hidden Lyaer이고 5 크기로 들어오고 4 크기로 내보낸다.

- W3는 Hidden Lyaer이고 4 크기로 들어오고 1 크기로 내보낸다.
- b1은 bias로 5크기를 가진다.
- b2은 bias로 4크기를 가진다.
- b3은 bias로 1크기를 가진다.
- L2는 X와 W1을 행렬 연산을 한후 b1을 더해 시그모이드로 계산한다.
- L3는 L2와 W2을 행렬 연산을 한후 b2을 더해 시그모이드로 계산한다.

- hypothesis는 L3과 L3를 행렬 연산후 b3을 더해 시그모이드로 계산한다.





![](https://raw.githubusercontent.com/MoDeep/1st-Grade-Study/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab10%20Image/3.png)

이와 같이 with을 사용하여 레이어를 만들면 Tensorboard에서 그래프를 시각화 할 수 있다.

![](https://raw.githubusercontent.com/MoDeep/1st-Grade-Study/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab10%20Image/4.png)



이 코드를 돌려보면 Accuracy가 0.5 밖에 되지 않는다. 그리고 Cost는 더 떨이지지 않는다.

![](https://raw.githubusercontent.com/MoDeep/1st-Grade-Study/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab10%20Image/5.png)

![](https://raw.githubusercontent.com/MoDeep/1st-Grade-Study/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab10%20Image/6.png)



Layer가 2~3개면 학습이 잘 됬지만 9개 정도가 되면 학습이 잘 되지 않는다.

![](https://raw.githubusercontent.com/MoDeep/1st-Grade-Study/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab10%20Image/7.png)

 이런 문제가 발생한 이유는

![](https://raw.githubusercontent.com/MoDeep/1st-Grade-Study/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab10%20Image/8.png)

Hidden Layer 즉 중간 항이 많아질수록 Input된 X의 미분이 너무 작아 영향을 주기 힘들다는 것이다.

그래서 이 문제를 해결하기 위해 생각하던중 Layer의 중간에 있는  Sigmoid를 사용을 잘 못했다는 것을 알게 되었다. Sigmoid 연산을 하게 되면 1보다 작은 수를 곱하기 때문에 최종적인 값은 매우 매우 작은 값이 된다는 것이다. 그래서 ReLU(Rectified Linear Unit)라는 함수를 만들었는데 0보다 작을 때는 0, 0보다 클때는 그대로 값을 넘겨준다.

~~~python
tf.sigmoid()
tf.nn.relu()
~~~



sigmoid대신 relu를 사용하면 이 처럼 accuracy는 거의 1에 가까워지고, cost도 0에 매우 근접해지는 것을 확인 할 수 있을 것이다.

![](https://raw.githubusercontent.com/MoDeep/1st-Grade-Study/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab10%20Image/9.png)

![](https://raw.githubusercontent.com/MoDeep/1st-Grade-Study/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab10%20Image/10.png)



추가로 Leaky ReLU는 0보다 작으면 0.1을 곱하고 0보다 크면 그대로 값을 넘겨준다. ELU, Maxout 등 ReLU를 응용한 다양한 함수들이 있다.



![](https://raw.githubusercontent.com/MoDeep/1st-Grade-Study/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab10%20Image/11.png)