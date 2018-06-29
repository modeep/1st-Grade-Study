# Lec 6 06/28

### Softmax classification: multinomial classification##

A or not, B or not, C or not 세개의 함수로 이루어진다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec6-1-1.PNG?raw=true)

이렇게 나타내기는 복잡하다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec6-1-2.PNG?raw=true)

그래서 이렇게 나타낸다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec6-1-3.PNG?raw=true)

그렇다면, sigmoid는 어디에서 적용될까?

이제 x를 하나 주면 a, b, c순으로 값이 세개 나온다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec6-2-1.PNG?raw=true)

그러나 이건 우리가 원하는 방식이 아니다. 

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec6-2-2.PNG?raw=true)

이렇게 1에서 0사이의 값이 나와야 한다.

그리고 a, b, c의 값을 모두 더하면 1이 된다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec6-2-3.PNG?raw=true)

이게 softmax 이다. 2.0, 1.0, 0.1 의 큰 값들을 적절히 변환시켜준다.

softmax는 값이 1에서 0 사이, 모든 값들을 더하면 1이라는 특징을 가지고 있다.

그리고 여기서 한 값만 정하는 것을 ONE-HOT Encoding 이라고 한다.

cost 함수는 이렇게 나온다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec6-2-4.PNG?raw=true)

-를 *log* 앞에 붙여서 옆의 함수 모양이 되도록 한다. 

저 함수에서는 0~1의 값에만 집중하면 된다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec6-2-5.PNG?raw=true)

값을 옳게 예측한 경우에는 당연히 cost 값이 0이 되고, 그렇지 않을 경우에는 엄청나게 커진다.

![](https://github.com/MoDeep/1st-Grade-Study/blob/master/Summaries/Heewoong/Images/lec6-2-6.PNG?raw=true)

여기서 Logistic cost = cross entropy 이다.

logistic에서 y값 0, 1을 one-hit encoding 을 이용하면 

0 = [1, 0] 1 = [0, 1]

logistic 을 풀면 
-log(H(x))   

 y = 1 => [0, 1]

-log(1-H(x)) 

 y = 0 => [1, 0]

cross entropy 를 풀면
sigma(Li * -log(Si))

y = L, H(x) = S 이므로

L:[0, 1], S:H(x)
sigma([0, 1] ( * ) -log[0, 1]) = 0

L:[1, 0], S:1-H(x)
sigma([1, 0] ( * ) -log[1-0, 1-1]) = sigma([1,0] ( * ) -log[1,0]) = 0

이렇게 두 함수가 같다는 것이 증명되었다.

