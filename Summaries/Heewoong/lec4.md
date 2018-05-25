## 2018/05/24 lec4##

선형함수를 설계하기 위해선 

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/Lec4-1.PNG?raw=true)

1. Hypothesis(가설)
2. Cost function(비용함수)
3. Gradient descent algorithm(경사를 따라 내려가는 알고리즘)

하나의 입력값이 있을 시에는 전의 방법대로 하면 된다.

그러나 여러개의 입력값이 있을 때는 방법이 조금 바뀐다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/Lec4-2.PNG?raw=true)

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/Lec4-3.PNG?raw=true)

더욱 더 많은 값이 주어지더라도 방법은 같다.

그러나 입력값이 100, 1000개쯤이 되면 매우 비효율적이게 된다.

그래서 이용하는 것이 Matrix(매트릭스)이다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/Lec4-5.PNG?raw=true)

이 계산법을 응용해서 간단하게 나타낼 수 있다.

이렇게 나타낼 때는 주로 X를 W앞에 놓는다. 

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/Lec4-6.PNG?raw=true)

그리고 다시 문제가 나타난다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/Lec4-7.PNG?raw=true)

X의 Instance 가 많으면 많을수록, 이 방법은 효율성이 떨어진다.

그렇기 때문에  매트릭스를 수정한다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/Lec4-8.PNG?raw=true)

이 매트릭스들은 각각 [5, 3], [3, 1], [5, 1] 이라고 말한다.

여기서 W매트릭스의 값은 X매트릭스의 뒷값, H(x)의 뒷값으로 알 수 있다.

 결국 [n, x], [x, y], [n, y] 의 형태가 된다.

강의에선 H(x) = Wx + b 같이 나타내지만,

실제에서는 H(X) = XW로 나타낸다.