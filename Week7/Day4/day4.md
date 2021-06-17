# [Week7 - Day4] 선형분류

## 1. 목표와 방법들
  - 목표
    - 입력벡터 **x**를 *K*개의 가능한 클래스 중에서 하나로 할당
  - 결정이론
    - 확률적 모델
      - 생성모델 *p*(**x**|*C<sub>k</sub>*)와 *p*(*C<sub>k</sub>*)를 모델링, 베이즈 정리를 사용해서 클래스의 사후 확률 *p*(*C<sub>k</sub>*|**x**) 계산, 또는 결합확률 *p*(**x**, *C<sub>k</sub>*)를 직접 모델링
      - 식별 모델 
        - *p*(*C<sub>k</sub>*|**x**)를 직접 모델링
    - 판별함수
      - 입력 **x**를 클래스로 할당하는 판별함수를 탐색, 확률 계산 X

## 2. 판별함수
  - 입력 **x**를 클래스로 할당하는 판별함수를 탐색
  - 이진 분류
    - 선형 판별함수
      - *y*(**x**) = **w**<sup>T</sup>**x** + *w*<sub>0</sub>
      - *y*(**x**) >= 0 인 경우 *C*<sub>1</sub> 아닌 경우 *C*<sub>2</sub>으로 판별
    - 결정 경계
      - *y*(**x**) = 0
      - *D* - 1 차원의 hyperplane(**x** 가 *D*차원의 입력벡터)
  - 결정 경계면의 두점 **x**<sub>*A*</sub>, **x**<sub>*B*</sub>
    - *y*(**x**<sub>*A*</sub>) = *y*(**x**<sub>*B*</sub>) = 0
    - **w**<sup>*T*</sup>(**x**<sub>*A*</sub> - **x**<sub>*B*</sub>) = 0 -> **w**는 결정 경계면에 수직
    - 벡터 **w**<sub>ㅗ</sub>
      - 원점에서 결정 경계면에 대한 사영
      - r * **w** / ||**w**|| = **w**<sub>ㅗ</sub>
      - *y*(**w**<sub>ㅗ</sub>) = 0
      - r = - *w*<sub>0</sub> / ||**w**||
    - *w*<sub>0</sub>는 결정 경계면의 위치를 결정
      - *w*<sub>0</sub> < 0 : 경계면이 원점에서 **w** 방향으로 멀어짐
      - *w*<sub>0</sub> > 0 : 경계면이 원점에서 **w** 반대 방향으로 멀어짐
  - *y*(**x**)값은 **x**와 결정 경계면 사이의 부호화된 거리와 비례
    - **x** 의 결정 경계면에 대한 사영 **x**<sub>ㅗ</sub>
      - **x** = **x**<sub>ㅗ</sub> + r * **w** / ||**w**||
      - r = *y*(**x**) / ||**w**||
      - *y*(**x**) > 0 : **x**는 경계면 기준으로 **w** 진행방향에 존재
      - *y*(**x**) > 0 : **x**는 경계면 기준으로 -**w** 진행방향에 존재
      - *y*(**x**)의 절대값이 클 수록 거리 증가
    - 더미 인풋 *x*<sub>0</sub> = 1 을 통해 식을 단순화
      - ![image](image/1.png)
  - 다중 분류
    - ![image](image/2.png)
    - j >< k 일때 *y*<sub>*k*</sub>(**x**) > *y*<sub>*j*</sub>(**x**) 를 만족하면 *C<sub>k*</sub> 로 판별

## 3. 분류를 위한 최소제곱법
  - ![image](image/2.png)
    - 행렬 \Tilde{*W*}를 사용한 표현
      - \Tilde{*W*} = {*w*<sub>1</sub>, *w*<sub>2</sub>, ..., *w*<sub>*k*</sub>}
      - ![image](image/3.png)
    - \Tilde{*W*}의 k번째 열
      - ![image](image/4.png)
  - 제곱합 에러함수
    - 학습데이터 {**x**<sub>*n*</sub>, **t**<sub>*n*</sub>}로 이루어진 행렬 **T** (**t**<sub>*n*</sub><sup>*T*</sup>), \tilde{**X**} (\tilde{**x**<sub>*n*</sub><sup>*T*</sup>})
      - ![image](image/5.png)
      - ![image](image/6.png)
    - \tilde{**W**} 에 대한 *E*<sub>*D*</sub>(\tilde{**W**}) 의 최소값
      - ![image](image/7.png)
    - 판별함수
      - ![image](image/8.png)
  - 단점
    - 극단치에 민감
      - 데이터가 결정 경계에서 멀리 있을수록 영향이 큼
    - 목표값의 확률분포에 대한 잘못된 가정에 기초
      - 목표값이 가우시안 분포를 따를 경우에만 적용가능

## 4. 퍼셉트론 알고리즘
  - *y*(**x**) = *f*(**w**<sup>*T*</sup>\phi(**x**))
    - *f*는 활성함수, 퍼셉트론에서는 계단형 함수 사용
      - ![image](image/9.png)
      - \phi(**x**) = 1
    - 에러함수
      - ![image](image/10.png)
      - *t* \in {-1, 1}
      - if *t*<sub>*n*</sub> = 1 -> **w**<sup>*T*</sup>\phi<sub>*n*</sub> > 0, else *t*<sub>*n*</sub> = -1 -> **w**<sup>*T*</sup>\phi<sub>*n*</sub> < 0
          - **w**<sup>*T*</sup>\phi<sub>*n*</sub>*t*<sub>*n*</sub> > 0
      - *M* 은 잘못 분류된 데이터들의 집합
  - Stochastic Gradient descent 적용
    - ![image](image/11.png)
    - 업데이트 시 잘못 분류된 샘플에 미치는 영향
      - ![image](image/12.png)
      - ![image](image/13.png)
  - 차후 뉴런 모델의 기초

## 5. 확률적 생성 모델
  - 분류 문제의 확률적 관점에서 풀이
    - *p*(**x**|*C*<sub>*k*</sub>)와 *p*(*C<sub>k</sub>*)를 모델링한 후 베이즈 정리를 통해 클래스의 사후확률 *p*(*C*<sub>*k*</sub>|**x**)를 계산
    - 판별함수 : 에러함수를 최소화시키는 최적의 파라미터 탐색
    - 확률적모델 : 데이터의 분포를 모델링하면서 문제를 해결
    - ![image](image/14.png)
  - Logistic Sigmoid
    - \delta(-*a*) = 1 - \delta(*a*)
    - *a* = ln(\delta / (1 - \delta))
    - ![image](image/15.png)
  - 연속적 입력
    - *p*(**x**|*C*<sub>*k*</sub>)가 가우시안 분포를 따름, 모든 클래스에 대해 공분산이 동일
      - ![image](image/16.png)
    - 클래스가 2개인 경우
      - *p*(*C*<sub>1</sub>|**x**) = \delta(*a*)
      - *a* 를 전개, **x** 에 관한 선형식으로 정리
        - ![image](image/17.png)
    - 클래스가 *K* 개인 경우
      - ![image](image/18.png)
  - 최대 우도해 (클래스가 2개인 경우)
    - 데이터
      - {**x**<sub>*n*</sub>, **t**<sub>*n*</sub>}, **t**<sub>*n*</sub> = 1 -> *C*<sub>1</sub>, **t**<sub>*n*</sub> = 0 -> *C*<sub>2</sub>
    - 파라미터들
      - *p*(*C*<sub>1</sub>) = \pi -> 구해야 하는 파라미터 \mu<sub>1</sub>, \mu<sub>1</sub>, \Sigma, \pi
    - 우도식 유도
      - *t*<sub>*n*</sub> = 1
        - ![image](image/19.png)
      - *t*<sub>*n*</sub> = 0
        - ![image](image/20.png)
      - 우도함수
        - ![image](image/21.png)
    - \pi 구하기
      - 로그우도함수에서 \pi 관련항만 정리
        - ![image](image/22.png)
      - \pi 에 관해 미분, 0으로 놓고 정리
        - ![image](image/23.png)
        - *N*<sub>1</sub> = *C*<sub>1</sub>에 속하는 샘플 수, *N*<sub>2</sub> = *C*<sub>2</sub>에 속하는 샘플 수
    - \mu<sub>1</sub>, \mu<sub>2</sub> 구학;
      - \mu<sub>1</sub> 관련항 정리
        - ![image](image/24.png)
      - \mu<sub>1</sub> 에 관해 미분, 0으로 놓고 정리
        - ![image](image/25.png)
      - 유사한 과정을 \mu<sub>2</sub> 에 적용
        - ![image](image/26.png)
    - \Sigma 구하기
      - ![image](image/27.png)
      - 가우시안 분포의 최대우도를 구하는 방법을 적용
        - \Sigma = **S**
  - 입력이 이산값일 경우
    - 각 특성 *x*<sub>*i*</sub> 가 0, 1 중 하나만 가질 수 있는 경우
    - 특성들이 조건부독립이라는 가정 -> 문제 단순화 (Naive-Bayes 가정)
      - *p*(**x**|*C*<sub>*k*</sub>)를 분해
        - ![image](image/28.png)
        - ![image](image/29.png)
  - *p*(*C*<sub>*k*</sub>|**x**)를 **x**의 선형함수가 Logistic Sigmoid 또는 Softmax를 통과하는 형태로 표현
    - 파라미터 계산을 위해 확률분포의 파라미터를 MLE로 계산
  - 대안법
    - *p*(*C*<sub>*k*</sub>|**x**)를 **x** 에 관한 함수로 파라미터화, 직접 MLE를 계산
    - 이를 위해 입력벡터 **x** 대신 기저함수 \phi(**x**) 사용
  - 로지스틱 회귀
    - *C*<sub>1</sub>의 사후확률은 특성벡터 \phi의 선형함수가 Logistic Sigmoid를 통과하는 함수로 표현
      - ![image](image/31.png)
    - \phi 가 *M*차원일 때 구해야 할 파라미터의 수는 *M*
      - 생성모델에서는 *M*(*M* + 5) / 2 + 1
    - 최대우도해
      - ![image](image/32.png)
      - 우도함수
        - ![image](image/33.png)
      - 음의 로그 우도
        - ![image](image/34.png)
        - ![image](image/35.png)
      - 이를 크로스 엔트로피 에러함수 (Cross-Entropy Error Function)라 칭함
    - 크로스 엔트로피
      - 주로 정보이론에서 사용
      - 일반적 정의
        - ![image](image/36.png)
      - 이산확률변수의 경우
        - ![image](image/37.png)
      - 크로스 엔트로피의 최소화 -> 두 확률분포의 차이 최소화
        - 에러함수 *E*(**w**) 의 최소화
          - 우도의 최대화
          - 모델의 예측값과 목표변수의(or 두개의 분포의) 차이를 최소화 
        

    