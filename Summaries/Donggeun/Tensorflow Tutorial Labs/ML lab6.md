# lec 07-1: 학습 rate, Overfitting, 그리고 일반화 (Regularization)

Gradient descent알고리즘에서 경사를 내려갈때 한번의 스탭이 클경우에는 U자 경사를 왔다 갔다 반복하다보면 Cost가 줄어들지 않고 큰 값이 나오는 오버 슈팅현상(overshooting)이 발생할 수 있다. 하지만 스탭이 작을 경우에는 매우 느리게 내려가다가 원하는 점에 도달 할 수도 있지만 중간에 멈출 수도 있다는 단점이 있다.
