# 2018/05/ 정리 : Lec5
## Logistic Classification의 가설 함수 정의

Classification의 종류 중 binary classification에 대해 강의가 진행되었다.

binary classification은 x에 대해 y값이 0 또는 1로 2개로 분류 되는 것이다.  
그래서 가설의 형태도 다르다.  
왜냐하면 0과 1로 구분 될때 이를 2차원 좌표에 놓고 linear regression의 가설을 그리면 y값이 잘못 판단될 수도 있고 또한 반드시 값이 0과 1사이 값으로 나와야 하는 데 linear regression의 가설일 경우 값이 0과 1 사이를 벗어나는 경우도 생기게 된다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec5-4.PNG?raw=true)

그래서 따로 Logistic Hypothesis의 형태의 가설을 지니게 된다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec5-5.PNG?raw=ture)

가설의 형태는 위와 같은 함수이다.  
이 함수의 이름은 sigmoid로 logistic function라고도 한다.
이 함수는 z값이 매우 커지거나 작아져도 y값이 0과 1사이를 벗어 나지 않는다.
이를 식의 형태로 만든 것이 아래의 Hypothesis이다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec5-1.PNG?raw=ture)

위에 식에서 WTX는 linear 모형의 함수 WX값을 넣어 놓은 것이다.

##Logistic classification의 cost함수

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec5-7.PNG?raw=ture)

logistic 함수의 cost함수의 형태는 linear regression의 cost함수와는 다르게 구불구불한 모양의 형태가 나온다.
그래서 우리가 최종적으로 찾아야하는 값은 global minimum인데 local minimum에서 멈추어 버릴수도 있기 때문에 cost함수도 바뀌어야 한다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec5-6.PNG?raw=ture)

다음과 같이 logistic의 cost함수를 정의 하는데 여기서 c함수를 2가지 케이스에 나누어 정의한다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec5-8.PNG?raw=ture)

이렇게 나누어 정의하면 예측을 잘 못 했을 경우 값이 무한에 가깝게 커지는 오류가 발생하고 알맞게 예측하면 제대로된 값이 나온다. 

하지만 이렇게 되면 프로그래밍을 할 때 if문을 쓰게 된다. 그래서 두 개의 케이스를 하나의 수식으로 만든 것이 아래와 같은 수식이다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec5-9.PNG?raw=ture)

이제 cost함수를 찾았으니 경사를 따라 내려가는 gradient decent algorithm을 구하면 된다. 
지난 번에 한 것과 같이 미분을 해주면 되고 내려가는 발자국의 크기를 알파로 놓으면 된다. 

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec5-10.PNG?raw=ture)
