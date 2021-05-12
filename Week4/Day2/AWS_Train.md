# [Week4 - Day2] AWS를 활용한 인공지능 모델 배포 실습 파트

## 4강
### Serialization & De-Serialization
  - joblib

  - vectorization (벡터화)
    - 행렬을 세로 벡터로 바꾸는 선형변환의 하나
    - vectorizer

  - joblib으로 Serialization을 진행한 모델을 pickle로 De-Serialization 불가능

## 5강
### Define inference
  - ModelHandler
    - initialize : 데이터 처리, 모델, 설정 등 초기화
      1. 설정 등을 초기화
      2. 신경망 구성 및 초기화
      3. 사전 학습 모델이나 전처리기 로딩 (De-Serialization)
    - preprocess : Raw input을 전처리 및 모델 입력 형태로 변환
      1. Raw input의 전처리
          - 데이터 클린징과 학습된 모델의 당시 스케일링이나 처리 방식과 동일하도록 변경이 필요
      2. 모델에 입력가능한 형태로 변환
          - vectorization, converting to id
    - inference : 입력에 대한 예측/추론
      1. 각 모델의 predict 방식으로 예측 확률분포 값 반환
    - postprocess : 모델의 예측값을 응답에 맞게 후처리
      1. 예측 결과에 대한 후처리
      2. 응답에서 받아야 하는 정보로 처리하는 역할
    - handle : 요청정보를 받아 적절한 응답을 반환  
      1. 정의된 양식으로 데이터의 입력 여부 확인
      2. 입력 값에 대한 전처리 및 모델 입력 형태로 변환
      3. 모델 추론
      4. 반환값의 후처리
      5. 결과 반환

## 6강
### Flask 기반 감성분석 API 개발
  - unittest

  - curl -d {"text" : [], "use_fast" : \<True or False\> } -H "Content-Type : application/json" -X POST http://host:port/predict


