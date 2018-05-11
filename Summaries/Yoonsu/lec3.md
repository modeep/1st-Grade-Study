# 2018/05/07 정리 : Lec3
## cost function

cost function으로 W와 b의 값을 최소화로 찾는 것이 linear regression의 목적이다.
![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec3_1.PNG?raw=true)

이때 cost의 값은 이차함수의 형태로 나타나게 된다.
(매번 완벽히 이차함수의 형태로 나타나는 것은 아니다. 
그렇기에 learning rate를 조절하여 최저점에 도달해야 한다./피드백 후 수정) 


![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec3_2.PNG?raw=ture)

여기서 cost의 최소값을 찾기 위해 많이 사용되는 알고리즘이 gradient descent algorithm이다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec3_4.PNG?raw=ture)

gradient descent algorithm은 경사도를 따라서 내려가는 역할을 하는 함수이다.


![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec3_3.PNG?raw=ture)

주어진 그래프에서 경사도를 구하는 것이 미분이고 그 미분을 하는 함수가 formal definition이다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec3_5.PNG?raw=ture)

convex function는
입체 좌표 위에 면의 형태로 값이 나오는 것이고 이 면이 
밥그릇 모양의 형태로 나타날 경우 무조건 최소의 cost값으로 가까이 가게 된다.


