# [Week12 - Day5] Mission Log
  - 타이베이 주택 가격 예측

## 보스턴과 동일 방법
  - X1 ~ X6 을 VectorAssembler 사용하여 features로 통합
  - randomSplit으로 7:3 분할
  - LinearRegression 모델 적용
  - RMSE 측정 -> 8.988568117087084

## 다른 모델 사용
  - RandomForestRegressor
  - GBTRegressor
  - RMSE 측정
    - RandomForest : 7.198784017933859
    - GBT : 8.44532447110716

## 데이터 스케일링 후 다시 성능 평가
  - MinMaxScaler, ML Pipeline 적용
  - X1~X6을 각각 벡터로 변경 (X1_vec ~ X6_vec)
  - X1_vec ~ X6_vec에 각각 MinMaxScaler 적용 (X1_scaled ~ X6_scaled)
  - 필요없는 컬럼 제거하여 보기 좋게 정리 (select)
  - X1_scaled ~ X6_scaled 까지 VectorAssembler 사용하여 features로 통합
  - randomSplit으로 7:3 분할
  - 3가지 모델 학습후 RMSE 측정
    - |스케일링|Linear|RandomForest|GBT|
      |----|--------|--------|--------|
      |이전|8.988568|7.198784|8.445324|
      |이후|7.984950|6.443968|7.509495|