# Lec 7

## Gradient descent

learning rate를 정하는 것은 매우 중요하다.

overshooting 은 learning rate 가 너무 커서, cost 함수의 값이 매우 커지게 되는 현상이다.

이 rate가 더 크게 된다면,  그래프를 벗어나게 될 수도 있다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec7-1-1.PNG?raw=true)



반면에 learning rate를 너무 작게 설정하면, 반복이 완료될때까지 원하는 cost에 도달하지 못할수도 있다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec7-1-2.PNG?raw=true)



적절한 learning rate를 정하기 위해 여러번의 테스트를 시도해야 한다.



Weight를 두개 준 뒤 위에서 바라본형태로 그래프를 나타낼수도 있다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec7-1-3.PNG?raw=true)



그런데 x1과 x2데이터 사이에 차이가 크다면, 그래프는 한쪽으로 치우치게 된다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec7-1-4.PNG?raw=true)



이럴 경우에는 데이터의 중심을 0으로 옮기는 zero-centered 방식, 

어떤 값이 항상 범위 안에 들어가도록 하는 normal-zed방식을 사용한다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec7-1-5.PNG?raw=true)



## Standardization(표준화)

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec7-1-6.PNG?raw=true)

일반화의 방식 중 하나이다.

값을 구한 평균 값으로 뺀 뒤, 분산 값으로 나눈다. 

파이썬으로는 한 줄로 나타낼 수 있다.



## Over fitting(과학습)

학습을 너무 많이 시키면, 학습 데이터에 딱 맞는 모델을 만들 수 있다.

가지고 있는 데이터에만 정확한 결과를 내기 때문에, 실제 데이터에는 효과가 없게 된다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec7-1-7.PNG?raw=true)

이렇게 -와 +가 섞여있는 경우에는, 둘 사이를 그어서 model2같은 모델을 만들 수도 있지만, 

그 정도로 정확히 만들려고 하면 모델이 비선형이 되어버린다.

그래서 model1이 더 일반적이고, 성능이 좋다.

model2같은 데이터를 바로 overfitting 이라고 한다.



데이터가 많을수록  ,feature이 적을수록 오버피팅은 줄어든다.

정규화(Regularization)를 시키는 것 역시 Overfitting의 해결책이 된다.

### Regularization

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec7-1-8.PNG?raw=true)

loss에 값을 하나 더한다. 

각각의 엘리먼트들을 제곱하여 더한 값인데, 그 앞에 상수가 하나 더 있다.

상수는 regularzation strengt 라고 하는데, regularization의 중요도를 정한다.

텐서플로우로는 간단히 구현 가능하다.

### Training/Testing Data Set

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec7-2-1.PNG?raw=true)

우린 training set으로 학습을 시킨다. 그런데 학습 뒤 training set을 넣어 확인을 해보는 것은 좋지 않다.

그래서 우린 training set의 70%를 training set으로, 나머지를 testing set으로 만든다.

training set에서도 일부를 Validation로 만드는데, 이는 학습된 모델에 값을 조정하기 위한 것이다.

### Online learning

100만 가량의 데이터가 있을 때, 100만개의 데이터를 10만개씩 나누어 학습시키는데,

처음 학습한 10만개가 그 뒤 학습할 10만개에 반영되게 한다는 방법이다.

### MNIST dataset

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec7-2-3.PNG?raw=true)

사람들이 적어놓은 숫자를 판별하게 하기 위한 데이터 셋이다.

미국의 사람들이 날려적은 우편번호를 컴퓨터가 알아보게 하기 위해서 나온 방법이다.
