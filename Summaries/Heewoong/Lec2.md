# 2018/4/11 Lec 2#

데이터를 가지고 학습을 하는 것이 Training이며, 데이터가 Training Data 이다.



 Regression(회귀분석) 학습을 할 때 가설을 세워야 하며, 가설을 세우는 것이 Linear Regression(선형 회귀)이다. 선형으로 가설을 세우고, 데이터에 적합한 선을 찾는 과정이 학습이다.

H(x) = Wx + b

H(x) = 가설

선들이 생성되면 어떤 선이 데이터에 가장 일치하는지 찾아야 한다. 데이터와 가설로 만들어진 선의 거리를 측정하여, 실제 데이터 값과 일치하는지를 구하는 과정을 Cost Function(비용 함수)라고 한다.

H(x)  - y 를 이용한다. 

그러나 음수일 경우는 결과가 이상하기 때문에

(H(x) - y)^2 를 이용한다.

 ![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/Lec2.jpg?raw=true)

다음과 같다.


