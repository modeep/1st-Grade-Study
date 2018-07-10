# 2018/07/05 정리 : Lec8
##딥러닝의 기본 개념: 시작과 XOR 문제
##Back-propagation과 2006/2007 '딥'의 출현

Deep Neural Net 
뉴럴의 구조를 본따 만든 함수 activation functions

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec8-1.PNG?raw=ture)

값이 들어와서 x와 w의 곱으로 나타나고 이들의 합을 cell body에서 다 더한 후 bias로 합한다. 그 후 activaion functions으로 합한 값이 어떠한 일정 값을 넘으면 1이라는 신호를 주고 아닐 경우 0이라는 신호를 준다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec8-2.PNG?raw=true)

이들을 모으면 오른쪽 처럼 여러개의 출력을 동시에 낼 수 있는 기계가 될 수 있다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec8-3.PNG?raw=true)

Marvin Minsky가 수학적으로 XOR은 한 번의 알고리즘으로 구현할 수 없다고 증명했다. 정확히는 하나로는 불가능하고 여러개를 합쳐서 구현이 가능하다고 하였다.

여기서 여러개를 합치는 것을 MLP라 하고 multilayer perceptrons이라 한다.

하지만 여기서 사용되는 각각의 w와 b들을 학습시킬 수가 없어 불가능하다고 하였다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec8-4.PNG?raw=true)

이에 대한 해결책으로 1974년에 Paul Werbos라는 사람이 Backpropagation이란 알고리즘을 가지고 해결해 냈다.

Backpropagation은 에러를 찾아서 이를 뒤로 보내 각각을 바꾸는 것이다. 

이 외에도 LeCun이라는 교수가 convolutional Neural Networks이라는 것을 만들어 냈다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec8-5.PNG?raw=true)

이것은 하나를 부분부분으로 자른 후 나중에 합치는 방법이다. (알파고도 이 방법을 사용했다)

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec8-6.PNG?raw=true)

하지만 이도 커다란 문제점에 도달하게 된다.
수가 적은 레이어에서는 가능했지만 수가 많아지자 에러가 앞으로 전달되면서 의미가 옅여진 것이다.
그래서 레이어가 많을 수록 성능이 떨어졌다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec8-7.PNG?raw=true)

2006에 Hinton과 Bengio가 초깃값을 잘 주면 학습이 될 수 있다고 말했다.
2007년 에는 신경망을 깊게 구축하면 복잡한 문제를 풀 수 있다고 논문에서 말했다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec8-8.PNG?raw=true)

imagenet이라는 챌린지로 이미지를 주고 이 사진을 맞추는 것으로 이의 에러율은 26.2%고 조금씩 줄어들었기에 10년 정도 후에 쓸 수 있다고 예상했지만 2년 후 알렉스라는 사람이 논문을 내서 에러율이 15%로 뚝 떨어졌다.

왜 이전에는 딥러닝이 잘 안 됬던 것인가?
밑의 4가지로Hinton이 정리했다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec8-9.PNG?raw=true)

왜 우리가 딥러닝을 해야하는지

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Yoonsu/images/lec8-10.PNG?raw=true)
