# 2018/05/07 정리 : Lec4
## multi-variable linear regression

multi-variable linear regression : 여러개의 변수를 사용하는 linear regression


![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec4-1.PNG?raw=true)

여러개의 x변수들을 입력 받아 y값을 찾아내는 것이다.

multi-variable linear regression의 Hypothesis는
![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec4-6.PNG?raw=true)
의 형태로 나타내진다.

가설의 형태를 간단히 하기 위해 matrix를 사용한다.

우리는 matrix의 곱셈만을 사용한다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec4-2.PNG?raw=true)


그렇게 되면 다음과 같은 형태로 가설을 표시할 수 있다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec4-3.PNG?raw=ture)

X는 x1 x2 x3들을 나타낸것이고 W는 w1 w2 w3들을 나타낸 것이다.

입력받는 데이터의 수를 인스턴스라 부른다.  
인스턴스의 수대로 매트릭스를 준다.
![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec4-7.PNG?raw=ture)

위의 그림에서 [5,3] [3,1] [5,1]을 각각 [x,y] [y,z] [x,z]라 명하겠다.

여기서 x는 인스턴스의 수,y는 변수의 수, z는 가설에서 요구하는 y값의 수 이다.



![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec4-5.PNG?raw=ture)
위의 말들을 요약해 적용하면 실제 공식으로는 위에 식처럼 나오지만 실제로 코드를 짤 때는 밑의 식처럼 짜야한다는 결론이 나온다.

