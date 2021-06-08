# [Week7 - Day2] 확률분포 2

## 1. 가우시안 분포
  - 정보 이론에서 엔트로피를 최대화시키는 확률분포
  - 중심극한 정리
  - ![image](image/1.png)
  - 기하학적인 형태 
    - *D* 차원 벡터 **x**
      - ![image](image/2.png)
    - \mu는 *D* 차원의 평균 벡터, \Sigma는 *D* * *D*  크기의 공분산 행렬
      - 파라미터로 주어진 확률밀도함수의 평균과 공분산
    - **x** 에 대한 함수적 종속성
      - 이차형식 ![image](image/3.png)
    - \Sigma - 대칭행렬로 간주 가능
      - \Sigma = *U<sup>T</sup>*\Lambda *U*
      - ![image](image/4.png)
      - 이차형식
        - ![image](image/5.png)
        - 벡터식으로 확장 : **y** = *U*(**x** - **\mu**)
          - **y**를 벡터들 *u<sub>i</sub>*에 의해 정의된 새로운 좌표체계의 점으로 해석 (기저 변환)
          - **x** - **\mu** : standard basis 좌표
          - **y** : *u<sub>i</sub>* basis 좌표
  - 정규화 증명
    - 야코비안 **J**
      - **y**의 확률밀도함수 계산에 필요
      - ![image](image/6.png)
    - 행렬식 |\Sigma|를 고유값의 곱으로 표현가능
      - ![image](image/7.png)
    - **y** 의 확률밀도 함수
      - ![image](image/8.png)
    - **y**의 정규화
      - ![image](image/9.png)
  - 기댓값 : *E*(**x**) = **\mu**
    - 다변량(Multivariate) 확률변수의 기댓값을 통해 증명
  - 공분산 : cov(**x**) = \Sigma
    - 2차 적률 (Second order moments) 계산
      - *E*(**xx**<sup>*T*</sup>)
      - **x** = (**z** + **\mu**)로 치환
    - **z** 를 *U<sup>T</sup>* **y** 로 치환
    - *i* >< *j* 인 모든 경우 -> 영행렬
      - ![image](image/11.png)
    - *E*(**xx**<sup>*T*</sup>) = **\mu** **\mu**<sup>*T*</sup>
    - cov(**x**) = *E*{(**x** - *E*(**x**))(**x** - *E*(**x**))<sup>*T*</sup>}

## 2. 조건부 가우시안 분포
  - *D* 차원 확률변수 벡터 **x**가 가우시안 분포 *N*(**x**|\mu, \Sigma)를 따름
    - 두 그룹으로 나누었을 때 한 그룹에 대한 나머지 그룹의 조건부 확률도 가우시안 분포를 따름
      - 공분산의 역행렬(정확도 행렬) 이용
      - 완전제곱식 방법
        - *p*(**x**<sub>*a*</sub>, **x**<sub>*b*</sub>) = *g*(**x**<sub>*a*</sub>)\alpha로 표현
        - ![image](image/12.png)
        - 이를 통해 *g*(**x**<sub>*a*</sub>)를 탐색
        - ![image](image/13.png) ![image](image/14.png)
          - const는 **x** 와 독립된 항들을 모아서 치환
          - 따라서 어떠한 함수라도 위와 같은 형태를 가지게 되면 \Sigma와 \mu를 가지는 가우시안 분포
  - 공분산
    - ![image](image/15.png)
  - 평균벡터
    - ![image](image/16.png)

## 3. 주변 가우시안 분포
  - ![image](image/17.png) ![image](image/18.png)
  - 파티션을 위한 이차형식
    - ![image](image/19.png)
  - **x**<sub>*b*</sub> 를 포함한 항을 *f*(**x**<sub>*b*</sub>, **x**<sub>*a*</sub>), 그 외에서 **x**<sub>*a*</sub>를 포함한 항을 *g*(**x**<sub>*a*</sub>)로 묶음
  - *f*(**x**<sub>*b*</sub>, **x**<sub>*a*</sub>)를 완전제곱식으로 변형
  - \tau = 1/2 * *m*<sup>*T*</sup> * \Lambda<sub>*bb*</sub><sup>-1</sup>*m*
    - ![image](image/20.png)
    - 이 값은 공분산 \Lambda<sub>*bb*</sub>에만 종속, **x**<sub>*a*</sub>에 독립
    - ![image](image/18.png)의 지수부에만 포커싱
  - \tau + *g*(**x**<sub>*a*</sub>) + const
    - ![image](image/21.png)
    - 공분산 
      - \Sigma<sub>*a*</sub> = ![image](image/22.png)
      - Schur Complement에 의해 
        - ![image](image/22.png) = \Sigma<sub>*aa*</sub>
    - 평균벡터
      - ![image](image/23.png)

## 4. 가우시안 분포를 위한 베이즈 정리
  - *p*(**x**), *p*(**y**|**x**), *p*(**y**|**x**)의 평균은 **x**의 선형함수, 공분산은 **x**와 독립적
    - *p*(**y**), *p*(**x**|**y**) 계산 -> 선형회귀에 유용
      - **z** = [ **x** \ **y** ]를 위한 결합확률분포 계산
      - **z**의 이차항 계산
        - -1/2 * **z**<sup>*T*</sup>**Rz**
        - ![image](image/24.png)
      - 공분산
        - ![image](image/25.png)
      - 평균벡터를 찾기 위해 **z**의 1차항 정리
      - 평균벡터
        - ![image](image/26.png)
      - **y**를 위한 주변확률분포 - 주변 가우시안 분포 적용
        - 평균 : *E*(**y**) = **A**\mu + **b**
        - 공분산 : cov(**y**) = **L**<sup>-1</sup> + **A** \Lambda<sup>-1</sup>**A**<sup>*T*</sup>
      - *p*(**x**|**y**) - 조건부 가우시안 분포 적용
        - ![image](image/27.png)

## 5. 가우시안 분포의 최대우도
  - 가우시안 분포에 의해 생성된 데이터 **X**에 대해 우도를 최대화하는 파라미터를 탐색
    - 로그우도 함수
      - ![image](image/28.png)
    - 우도를 최대화하는 평균벡터 **\mu**<sub>*ML*</sub>
      - **y** = (**x** - **\mu**)로 치환
      - ![image](image/29.png)
    - 우도를 최대화는 공분산행렬 \Sigma<sub>*ML*</sub>
      - ![image](image/30.png)
    - (\Lambda<sub>*ML*)<sup>-1</sup> = \Sigma*ML*, *h*(**X**) = **Y**가 일대일
      - *h*<sup>-1</sup>(**Y***) = **X*** 을 적용
        - \Lambda<sub>*ML*</sub> = argmin *l*(\Lambda)

## 6. 가우시안 분포를 위한 베이즈 추론
  - MLE법은 파라미터들의 하나의 값만을 계산
  - 베이지안법을 파라미터의 확률분포 자체를 게산
  - 우도함수
    - ![image](image/31.png)
  - 사전확률
    - ![image](image/32.png)
  - 사후확률
    - ![image](image/33.png)