# [Week8 - Day3] Deep Learning 3

## 1. 기계학습 요소
  - 카드 승인 예제
    - 요소
      - input, output, target distribution, data, hypothesis
    - 설정
      - 지도 학습
        - 데이터, 목적함수, 가설의 최적화로 구분 가능
        - 데이터를 받아 계산을 하고 목적함수를 통해 가설을 최적화

## 2. 모델 선택
### 2-1 Underfitting - Overfitting (과소적합-과잉적합)
  - Underfitting
    - 모델의 용량이 작아서(구조가 너무 단순해서) 데이터에 내재된 규칙을 따라가지 못하는 경우
  - Overfitting
    - Training Set에 대해 완벽하게 근사화함
    - 새로운 데이터를 예측할 때 문제 발생
    - 모델의 용량이 커서 학습과정에서 노이즈까지 수용하여 학습
    - 적절한 용량의 모델을 선택하는 작업이 필요
  - 규제를 통해 모델의 용량이 커지는 것을 억제

