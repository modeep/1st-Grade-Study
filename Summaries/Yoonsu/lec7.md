# 2018/07/05 정리 : Lec7
##학습 rate,Overfitting,Regularization
##Training/Testing 데이타 셋

너무 큰 learning rate를 설정할 경우 가장 작은 값이 아니라 더욱 큰 값으로 튕겨 나갈 수 있다.(=overshooting)

그렇다고 너무 작은 learning rate를 설정할 경우 최솟값으로 내려가지 못 할 수도 있다. 이때는 learning rate을 조금 올려야 한다.

learning rates의 조절은 각각 데이터와 환경에 따라 달라져야 한다.

tip : 0.01부터 시작해서 조절해 나가기

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec7-1.PNG?raw=true)

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec7-2.PNG?raw=true)

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec7-3.PNG?raw=true)

x1과 x2의 값이 있는데 이 들의 값이 큰 차이가 난다면  균등한 모양의 등고선이 아니라 한 쪽으로 왜곡된 형태의 등고선이 나타난다.

이때 알파값을 잡았을 때 알파값이 좋음에도 불구하고 잘 못 하면 밖으로 튀어나가게 된다. 이처럼 데이터 값에 큰 차이가 있을 때 이를 Nomalize라고 한다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec7-4.PNG?raw=true)

보통 zero-centered data라고 data의 중심이 0으로 갈 수 있도록 하는 방법을 쓰기도 하고 어떤 데이터가 특정 범위 안에 들어갈 수 있도록 하는 방법(normalized data)도 있다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec7-5.PNG?raw=true)

x의 값을 평균과 분산을 가지고 나누어주면 된다. 이 형태의 normalization을 Standardization이라 한다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec7-6.PNG?raw=true)

 학습 데이터에 너무 잘 맞는 모델을 만들면 학습 데이터를 돌리면 결과가 잘 나오겠지만 실제적으로 사용하면 잘 안 맞는 경우가 생긴다 이를 Overfitting 이라고 한다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec7-7.PNG?raw=true)

 overfitting을 해결하는 방법은 많은 데이터 셋을 가지면 된거나 features의 갯수를 줄이는 방법, Regularization으로 해결하면 된다.

 Regularization은 일반화이다.
 weight의 값을 줄이는 것

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec7-8.PNG?raw=true)

 cost 함수의 뒤에 텀이라는 것을 추가시켜준다.
W를 제곱하고 그것을 합하고 이것을 최소화 시키는 것을 상수로 둘 수 있다. 이것을 regularization sltength라고 하는데 이 값이 큰 값이 되면 이것을 중요하게 여긴다는 것이다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec7-9.PNG?raw=true)

모든 데이터를 학습시키는 것이 아니라 몇 개는 학습을 시키고 그 학습된 모델에 테스트 셋을 돌려서 값이 제대로 나오는 지를 확인하면 된다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec7-10.PNG?raw=true)

Traning으로 학습을 시키고 Validation set으로 알파나 람다의 값이 어떤것이 좋을지 튜닝한다. 즉 모의시험을 하는 것이다. 여기서 완벽하게 된다면 Testing set으로 실전을 돌리면 된다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec7-11.PNG?raw=true)

데이터 셋이 많을 경우 한 번에 학습시키기가 힘드므로 Online learning이라는 학습 방법을 사용하기도 한다.

Online learning은 데이터 셋을 잘라서 돌리는 방식으로 이때 그 전에 학습된 값이 모델에 계속 남아있어야 한다.

이 방식의 장점은 나중에 데이터가 추가되어도 기존의 데이터를 다시 학습시키지 않아도 된다는 것이다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec7-12.PNG?raw=true)

모델의 정확도를 예측하는 것은 실제 데이터의 Y값과 모델이 예측한 값을 비교하면된다.