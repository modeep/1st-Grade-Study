# lec 08-1: 딥러닝의 기본 개념: 시작과 XOR 문
뉴런에 x * W 으로 들어오는 신호를 전부 합치고 bios가 합쳐저 어떤 값 이상이 되면 활성화가 되고 어떤 값 이하가 되면 비활성화가 되는 형태이다.

![](https://raw.githubusercontent.com/MoDeep/1st-Grade-Study/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab8%20Image/Image1.png)

이러한 뉴런 구조를 발견했을 때는 소프트웨어적으로 구현하지 못하기 때문에 하드웨어적으로 구현했다. 이를 구현한 프랭크는 미래에 학습하여 스스로 걷고 이야기하고 글을 쓰는 등을 할 수 있으 것이라고 예측하였다.

## XOR

![](https://raw.githubusercontent.com/MoDeep/1st-Grade-Study/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab8%20Image/Image2.png)

OR, AND는  Linear하게 선을 그으면 x1, x2 Input으로도 충분히 100%로 구분을 할 수 있다. 그러나 XOR은 최대 50%로 밖에 구분을 할 수 없다. 게다가 1969년에 MIT AI Lab의 Minsky 교수가 현재의 기술로 XOR 문제를 풀 수 없다고 정의 하였다
Minsky 교수는 뉴럴 네트워크를 구현하지 못하 것이라고 하였다.

![](https://raw.githubusercontent.com/MoDeep/1st-Grade-Study/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab8%20Image/Image3.png)

하지만 Paul Werbos이라는 사람이 구현 방법을 찾았다.

![](https://raw.githubusercontent.com/MoDeep/1st-Grade-Study/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab8%20Image/Image4.png)

Lecun 교수가 고양이를 대상으로 일정한 모양의 사진을 보여주었는데 고양이의 일부분의 뉴런이 반응 하는 것을 발견하였다. 그래서 뉴럴 네트워크로 구현하였다.

![](https://raw.githubusercontent.com/MoDeep/1st-Grade-Study/master/Summaries/Donggeun/Tensorflow%20Tutorial%20Labs/ML%20lab8%20Image/Image5.png)

뉴럴 네트워크에서는 사진의 일부분 씩을 잘라서 신경망에 Input 하는 형식이었다.

# lec 08-2: 딥러닝의 기본 개념2: Back-propagation 과 2006/2007 '딥'의 출현

## CIFAR

인공지능 연구센터이다. 어떠한 활용할 곳이 없어도 연구 하라고 밀어주었다. 지금의 딥러닝이 발전할 수 있었던 발판이 되었다.

2006, 2007년에 Hiton, Bengio 교수가 논문을 발표한다.
지금까지의 큰 신경망은 학습이 어려웠는데 우리가 지금까지 초기 값을 잘못줬다.
신경망을 현재와 같이 잘 구현하면 어려운 문제도 해결할 수 있을 것을 증명하였다.

2010년도에는 26.2%였던 에러율을
2012년에 Hiton교수의 제자가 15%까지 줄였다.
2015년에 MSRA에 있던 연구자가 만든 딥러닝 기반의 시스템으로 3%대의 에러율로 줄였다.

두바이에서는 통화를 할때 주변 소음을 90%까지 줄여주는 시스템을 개발하였다
게임도 강화학습을 통해서 스스로 학습하는 모델도 개발하였다.
