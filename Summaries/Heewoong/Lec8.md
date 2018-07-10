## Lec 8

대신하여 생각하는 기계를 만들자는 의도에서 딥러닝이란 개념이 생겨났다.                 
![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec8-1-1.PNG?raw=true)

사람들은 뇌의 구조가 매우 복잡하고,  그 복잡한 구조는 오히려 매우 단순한 뉴런이라는 구조로 이루어진 것을 발견함.  											
![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec8-1-2.PNG?raw=true)                                                                      									X * W 형태의 모든 값이 합쳐진 뒤 bias를 더한 값이 일정 이상이면 활성화되고, 그렇지 않으면 활성화되지 않는다.

사람들은 이를 모방하여 X에 가중치 W를 곱하고, 그 값을 모두 더한 다음 bias를 더하여 activation function으로 1과 0으로 신호를 구분하여 보내는 형태의 모델을 만듬.																		![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec8-1-3.PNG?raw=true)

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec8-1-4.PNG?raw=true)																		1960년대쯤, 사람들은 이런식의 구조로 여러개의 출력을 동시에 내는 기계를 만들었고 자아를 인지까지 할 수 있는 컴퓨터를 만들었다고 허황된 말을 함. 

그러다 문제가 하나 생기게 된다. 1969년, XOR연산을 학습하는것이 불가능하다며 한 교수가 발표를 한 것이다. 이 교수는 XOR연산은 하나만으로 해결하는 것은 불가능하고 여러개를 합처야만 풀 수 있다는 말을 했다. 그러나 동시에 두 개 이상의 가중치를 동시에 학습시키는 것은 불가능하다고 주장했다.								
![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec8-1-5.PNG?raw=true) 																			그리고 이 사람의 주장 때문에, 딥러닝 기술은 10~20년정도 후퇴하게 된다.

그리고 1974년에 Paul Werbos 가 이 문제의 해결법을 알아냈다.					
![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec8-1-6.PNG?raw=true)																	네트워크에 각각의 W와 b가 있으면,  이것들을 이용해서 출력을 만들고 가진 정답과 비교해 에러를 찾고, 거꾸로 진행하면서 각각의 값을 조정한다는 답을 냈다. 그러나 아무도 관심을 자지지 않았다.

1986년에 Hinton이란 사람이 독자적인 방법을 발견했다. 이 사람은 고양이에게 그림을 보여주어, 그림의 형태에 따라서 일부의 뉴런만 활성화된다는 것을 알아낸 것이다. 그리고 이 사실에서 그림을 조금씩 잘라서 학습하고, 그것을 합치는 방법을 개발했다.																	![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec8-1-7.PNG?raw=true) 																	1990년, 미국은 이 방법을 이용해 자동으로 책을 읽는 기계를 개발해내었다. 1984년에서 1994년까지 자동주행차량을 연구하기도 했었다.

그러나 1995년, 다시 큰 문제가 나타났다. 복잡한 문제를 풀기 위해서는, 10개가 넘는 레이어를 다시 돌아가 에러를 전달해야 하는데, 뒤로 가는 과정에서 에러가 거의 전달되지 않던 것이었다.													![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec8-8.PNG?raw=true)

2006년, 2007년에 각각 Hinton과 Bengio교수가 초기값을 잘 준다면, 많은 레이어를 가지는 학습도 할 수 있다고 했다. 그리고 이 사람들은 논문에서 뉴럴 네트워크가 아닌, 이름을 Deep Nets, Deep Learning 으로 바꾸었다. 사람들은 이 새로운 이름에 흥미를 가지고 딥러닝을 연구하게 되었다.									
![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec8-2-1.PNG?raw=true)

그리고 진짜로 주목을 받게 한 곳은 IMAGENET이라는 곳이다. 이 사이트에서  사진을 보고 알아맞히는 학습을 하게 했는데, 한 학생이 무려 오답률 26%에서 15%로 완화시키면서 큰 화제가 된다.

그리고 계속하여 딥러닝이 발전하게 되면서, 딥러닝은 일상생활 여러 곳에서 응용되고 있다. 