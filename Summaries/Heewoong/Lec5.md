## Lab 5-1

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/Lec5-1-1.PNG?raw=true)

Classification: 이전의 Regression이 숫자를 예측하는 것이었으면, 이것은 둘 중 하나를 구분하는 

것이기 때문에 Binary Classification 이라고 할 것이다. 

스팸메일과 햄메일을 구분하는 등의 것이 예시가 된다.

보통은 1과 0로 예측을 한다. 

주식을 예측할 수도 있고, 호감적인 이미지인지 비호감적인 이미지인지 구분도 할 수 있다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/Lec5-1-2.PNG?raw=true)

그러나 이런 상황에서는 문제가 발생할 수 있다.

만약 학생이 50 시간을 공부했다고 쳤을 때, 앞에서 정해놓은 0.5 이하라는 

합격값 이하에서 합격의 결과가 나올 수 도 있는 것이다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/Lec5-1-3.PNG?raw=true)

이렇게 H(x) = Wx + b 같은 모양의 식으로 계산을 하면, 0에서 1 사이의 값이 아닌 

그를 훨씬 초과하는 결과가 나올 수도 있는 것이다.

그래서 사람들이 찾은 함수가 바로 g(z)이다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/Lec5-1-4.PNG?raw=true)

이걸 logistic function, sigmoid function 이라고도 한다. 

이 함수에선 z 값이 어느정도 이상으로 크거나 작더라 되더라도, 0과 1에 수렴한다.

결국 우리의 Logistic Hypothesis는

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/Lec5-1-5.PNG?raw=true)

이렇게 나온다.

## Lab 5-2

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/Lec5-2-1.PNG?raw=true)

우리의 이전 cost 함수는 이런 형태였다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/Lec5-2-2.PNG?raw=true)

그러나 이 새로운 cost 함수의 형태는 결과값의 심각한 오차를 발생시킬 수 있다.

그래서 1와 0 일때, 두가지의 함수를 만든다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/Lec5-2-3.PNG?raw=true)

e와 상극인 *log*를 사용했다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/Lec5-2-4.PNG?raw=true)

y=1일때, 예측을 옳게 했으면 0에 가까운 값이므로 cost=0이 된다. 

그러나 그 반대의 경우에는 무한대가 되기 때문에,  cost 값도 ∞이 된다.

y=0일때도 예측과 실패했을때의 cost 값은 같다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/Lec5-2-5.PNG?raw=true)

텐서플로우에서 코드를 직접 짜기엔 위의 식이 어렵기 때문에, 하나로 합쳤다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/Lec5-2-6.PNG?raw=true)

여기서 a는 learning rate와 비슷한 작용을 한다.

밑의 식은 이미 함수로 구현되어 있기 때문에, 따로 만들 필요가 없다.
