# Lec 7#

##Gradient descent

overshooting 은 learning rate 가 너무 커서, cost 함수의 값이 매우 커지게 되는 현상이다.

반면에 learning rate를 너무 작게 설정하면, 반복이 완료될때까지 원하는 cost에 도달하지 못할수도 있다.

적절한 learning rate를 정하기 위해 여러번의 반복을 시도해야 한다.



등고선의 형태로 그래프를 나타낼수도 있는데,

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec7-1-1.PNG?raw=true)

이럴 경우에는 데이터의 중심을 0으로 옮기는 zero-centered 방식, 

어떤 값이 항상 범위 안에 들어가도록 하는 normal-zed방식을 사용한다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec7-1-2.PNG?raw=true)


##Standardization

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec7-1-3.PNG?raw=true)

일반화의 방식 중 하나이다.

값을 구한 평균 값으로 뺀 뒤, 분산 값으로 나눈다. 

파이썬으로는 한 줄로 나타낼 수 있다.

## Over fitting##

학습을 너무 잘 해버린 것을 의미한다.

가지고 있는 데이터에만 학습을 해서, 실용성이 없게 된다.

데이터가 많을수록  ,feature이 적을수록 오버피팅은 줄어든다.

### Regularization###

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec7-1-4.PNG?raw=true)

loss에 값을 하나 더한다. 

각각의 엘리먼트들을 제곱하여 더한 값인데, 그 앞에 상수가 하나 더 있다.

상수는 regularzation strengt 라고 하는데, regularization의 중요도를 정한다.

텐서플로우로는 간단히 구현 가능하다.

### Training/Testing Data Set###

우린 training set으로 학습을 시킨다. 그런데 학습 뒤 training set을 넣어 확인을 해보는 것은 좋지 않다.

그래서 우린 training set의 일부를 training set으로, 나머지를 testing set으로 만든다.

training set에서도 일부를 Validation로 만드는데, 이는 학습된 모델에 값을 조정하는 것이다.

### Online learning###

데이터가 매우 많을 때, 데이터를 나누어서 학습한다.

이때 학습 모델은 바로 전의 학습 데이터를 기억하고 있어야 한다.

이 데이터 모델을 Online 모델이라고 한다.



