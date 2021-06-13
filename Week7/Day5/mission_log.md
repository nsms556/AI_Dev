# [Week7 - Day5] Mission Log

## Mission 1
### Memory Error
  - 가상메모리 26기가 할당하여 해결
  
### L2 Regularization
  - `lambda_value * np.sum(np.square(W))`
  
### validation
  - train 데이터에서 55000개를 잘라 새로운 train으로
  - 나머지 5000개를 valid 데이터로 분할
  - cost 출력 대신 tqdm을 통해 진행도를 추적하는 new_batch_gd
  - test 데이터 대신 valid 데이터를 사용해 accuracy 계산
  - 사용한 람다 값과 계산된 점수를 데이터프레임으로 생성하여 점수순으로 정렬하여 리턴


## Mission 2
  - `plt.contourf()`의 리턴 객체(`contourSet`)에서 `path`를 가져옴
  - `path.vertices`에서 원하는 직선의 좌표를 추출하여 `points`로 저장
  - `points`를 `x_train, y_train`으로 나누어 `LinearRegression` 모델의 입력데이터로 사용
  - 학습된 모델에서 `coef_`와 `intercept_`를 사용한 직선을 `plot()` 함수로 그림
  - *y* = *ax* + *b* 형태의 각 함수들을 출력
