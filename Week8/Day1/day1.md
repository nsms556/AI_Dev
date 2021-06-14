# [Week8 - Day1] 선형분류 2

## 1. 확률적 식별 모델
### 1-1 에러함수의 **w** 에 대한 미분(Gradient)
  - 에러함수 *E*<sub>*n*</sub>(**w**)
    - ![image](image/1.png)
    - ![image](image/3.png)
  - *dE*(**w**)
    - ![image](image/2.png)

### 1-2 다중클래스 로지스틱 회귀
  - ![image](image/4.png)
  - 우도 함수
    - 특성벡터 \phi<sub>*n*</sub>을 위한 목표벡터 **t**<sub>*n*</sub>는 클래스에 해당하는 하나의 원소만 1, 나머지는 0인 1-of-K 인코딩
      - ![image](image/5.png)
    - 음의 로그 우도
      - ![image](image/6.png)
    - **w**<sub>*j*</sub>에 대한 미분
      - 하나의 샘플 \phi<sub>*n*</sub>에 대한 에러
        - ![image](image/7.png)
      - *dE* / *d***w**<sub>*j*</sub>
        - ![image](image/8.png)
      - *E*<sub>*n*</sub>와 **w**<sub>*j*</sub>의 관계는 오직 *a<sub>nj</sub>* 에만 의존
      - *E<sub>n</sub>*은 *y*<sub>*n*1</sub> ~ *y*<sub>*nK*</sub> 의 함수
      - *y<sub>nk</sub>*은 *a*<sub>*n*1</sub> ~ *a*<sub>*nK*</sub> 의 함수
      - ![image](image/9.png)
