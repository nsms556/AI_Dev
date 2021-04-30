# [2주차 - Day4] 14강 몇 가지 확률분포

## 1. 이항분포
  - 이항확률변수의 확률분포

  - 베르누이 시행
    - 정확히 2개의 결과만을 가지는 실험
    - 성공확률 : *p*
  - 이항확률변수
    - n번의 베르누이 시행에서 성공의 횟수

  - ![image](image/18.png)

  - 평균
    - *E(X)* = *np*
  - 분산
    - *V(X)* = *np*(1-*p*)
  - 표준편차
    - SD(*X*) = {*np*(1-*p*)}<sup>1/2</sup>

## 2. 정규분포
  - 연속확률변수의 확률분포
    - 확률밀도함수
    - 그래프 아래 부분의 넖이 = 확률
      - ![image](image/19.png)

  - 정규분포의 확률밀도함수
    - ![image](image/20.png)
    - ![image](image/21.png)

  - 표준정규분포
    - 평균이 0, 편차가 1인 정규분포
    - 표준정규확률변수
      - ![image](image/22.png)
    - *Z~N*(0, 1)

## 3. 포아송 분포
  - 일정한 시간단위 또는 공간단위에서 발생하는 이벤트의 수의 확률분포
    - EX) 하루동안 어떤 웹사이트의 방문자 수
  - 확률분포함수(확률질량함수)
    - ![image](image/23.png)
      - 평균 : <img src="https://latex.codecogs.com/png.latex?\dpi{120}&space;\bg_white&space;\large&space;\lambda" title="\large \lambda" />
      - 분산 : <img src="https://latex.codecogs.com/png.latex?\dpi{120}&space;\bg_white&space;\large&space;\lambda" title="\large \lambda" />

## 4. 지수분포
  - 포아송 분포에 의해 어떤 사건이 발생할때, 한 시점에서 사건이 발생할 때까지 걸리는 시간에 대한 확률분포
  - 함수
    - ![image](image/24.png)
  - 평균
    - *E(T)* = 1 / lambda
  - 분산
    - *V(T)* = 1 / lambda<sup>2</sup>
    