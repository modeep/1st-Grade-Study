# lec 07-1: 학습 rate, Overfitting, 그리고 일반화 (Regularization)
## Gradient descent
우리는 Gradient descent에서 Learning_rate를 임의로 정해주었다.
그러나 Learning_rate의 값이 매우 크게 설정하면 오버슈팅(Overshoting)이 발생할 수 있다. 오버슈팅은 쉽게 말해서 Cost가 줄어들지 않고 값자기 증가하는 현상을 말한다.
Learning_rate를 작게 설정하면 매우 느리게 내려가서 우리가 반복을 설정한 값이 끝날때 우리가 원하는 Cost에 도달하기도 전에 끝날 수도 있다.
