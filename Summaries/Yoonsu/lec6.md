# 2018/07/03 정리 : Lec6
## Softmax Regression 개념
## Softmax classifier의 cost함수

Softmax classification은 여러개의 클래스가 있을때 예측하는 Multinomial classification 중 가장 많이 사용되는 것이다.

각각의 class를 구분하는 binary classification을 만들어서 합치면 Multinomaial classification을 구현할 수 있다.
![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec6-1.PNG?raw=ture)

그런데 각각의 가설 함수들을 만들면 복잡하기 때문에 합쳐서 Matrix multiplication를 사용해 한번에 가설 함수를 만들어 낸다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec6-2.PNG?raw=true)

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec6-3.PNG?raw=ture)


Rogistic classifier에 넣어서 나온 y값들을 softmax에 넣으면 0~1사이의 값으로 나오고 전체 합이 1이 된다는 특징이 있다. 고로 이 값은 확률로도 볼 수 있다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec6-4.PNG?raw=ture)

그리고 하나만 골라서 말할 때는 one-hot encoding이라는 기법을 이용해서 제일 큰 값을 1로 만들고 나머지는 다 0으로 만들 수 있다. 

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec6-5.PNG?raw=ture)

Cross-Entropy라는 함수를 통해서 차이를 구하는 cost함수를 얻게 된다.
![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec6-6.PNG?raw=ture)

예측한 값의 차이가 적을수록 0에 수렴하고 차이가 클 경우 무한에 수렴한다.
![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec6-7.PNG?raw=ture)

Logistic cost와 cross entropy는 같은 식이다.
![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec6-8.PNG?raw=ture)
왜냐하면 cross entropy에서 one-hot encoding을 사용하면 값이 0과 1로 변환 되기 때문에 같은 결과 값이 나오기 때문이다.

여러개의 training set이 있을 경우 전체의 차이를 구한 후 평균을 내주면 된다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec6-9.PNG?raw=ture)

Gradient descent algorith는 이전과 같이 함수를 미분하는 것이다.
내려가는 값을 알파로 둔다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec6-10.PNG?raw=ture)
