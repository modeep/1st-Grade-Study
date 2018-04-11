# 2018/04/11 정리 : Lec2 
## linear regression

regression을 학습할 때 일차 함수 형태의 가설을 가지게 된다.  (linear Hypothesis)  
데이터값에 부합하는 선형 함수(일차방정식)가 존재

가설 : H(x)=Wx+b

여러 가설 중 가장 데이터 값과 부합하는 가설을 찾아야한다.
즉 여러 W와 b값 중 가장 데이터와 근접한 값을 찾아야 함

여러 가설들 중에서 가장 좋은 가설을 찾으려면 그 가설의 값과 실제 값 사이의 차이를 구해서 그 차가 가장 적은 가설을 찾아야 한다.

**cost function/loss funstion**  
더 좋은 가설을 구하기 위한 함수로 H(x) - y의 형태이다.  
하지만 위의 식의 경우 값이 양수가 나오기도 하고 음수가 나오기도 한다. 그래서 {H(x)-y}^2의 식을 사용한다.  

 제곱을 하는 이유 
 - 차의 값이 무조건 적으로 양수가 되기 때문이다.  
- 가설과 데이터 간의 차이가 클 때 더 많은 패널티를 받는다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/Image1.jpg?raw=true)  
cost Function은 결과적으로 W와 b의 function이된다.  

그러므로 가장 작은 값을 가지는 W와 b를 구하는 것이 학습의 목표이다.
 


