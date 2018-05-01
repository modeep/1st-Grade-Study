# 2018/05/01 lec 3#

가설의 값과 실제 값 차이를 제곱하여 평균을 구하는 것을 Cost함수라고 한다.  Cost 값을 최소화하는 값들을 찾는 것을 선형 회귀라고 한다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec3-1.PNG?raw=true)

간략히 하기 위해 b를 0으로 한다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec3-2.PNG?raw=true)

Cost 함수의 모양은 다음과 같다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec3-3.PNG?raw=true)

데이터로 그래프를 이런 형태로 만들어진다. 

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec3-4.PNG?raw=true)

목적은 cost가 가장 작아지는 점을 찾는 것이다.

이 점을 기계적으로 찾아 내는 것이 Gradient descent algorithm(경사를 따라 내려가는 알고리즘)이다.

Cost 함수의 값들에서 최소의 Cost를 찾는 과정이다. 랜덤 값에서 경사도를 내리면서 경사도가 0이 되면 최소값이 된다. 항상 최저점에 도달할 수 있다.

미분을 적용할 때 쉽게 하기 위해서  m에 2를 붙인다. 그러나 똑같은 의미를 지니게 된다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec3-6.PNG?raw=true)

cost(W) Function을 미분값을 곱해준다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec3-7.PNG?raw=true)

생략 과정.

여러번 반복하면 W값이 변하게 되는데 그 값이 cost를 Minimize하는 과정이 만들어지게 된다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec3-8.PNG?raw=true)

Cost 함수를 이렇게 그릴 수도 있다. 시작점에 따라 2가지의 경로와 같이 도착지점이 달라질 수 있다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec3-9.PNG?raw=true)

그래서 Convex Function(볼록함수)을 사용한다. 어디서 시작하든 도착지점은 같다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec3-10.PNG?raw=true)
