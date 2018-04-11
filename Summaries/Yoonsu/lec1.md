# Lec1
## 머신러닝의 용어와 개념 설명
### 머신러닝
- 프로그램이 데이터를 보고 학습하는 프로그램  
ex)자동주행, 스팸메일  
- 1959년 Arthur Samuel 생각
개발자의 명령에 따른 프로그램-explicit programming

### 머신러닝의 종류 (supervised/unsupervised)

**supervised**

- 정해져있는 데이터(training set-레이블이 달려있는 데이터)를 사용한 학습  
이미 정의가 되어있는 데이터를 가지고 다른 데이터를 예측  
ex)사진인식프로그램, 스팸메일분류 


training data set : x와 y가 정의 되어 있는 학습 레이블  
ex)알파고  


- 결과(y)에 따른 종류   
--regression : 시험예측(범위 내에서 결과 예측)   
--binary classification : 성공여부(분류 0/1)   
--multi-label classification : 성적 등급(분류 범위 넓음)

data set example

binary classification  
x | y
:--:|:--:
10 | P
5 | F


regression  
x | y
:--:|:--:
10 | 100
7 | 80

multi-label classification  
x | y
:--:|:--:
10 | A
7 | B


**Unsupervised**

- 데이터를 보고 스스로 학습하는 것/우리가 일일이 레이블을 줄 수 없는 경우  
ex)구글 뉴스(자동적으로 유사한 뉴스 그룹지음)  
Word clustering(유사한 단어 그룹지음)