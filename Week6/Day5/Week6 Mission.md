# [Week6 - Day5] Mission - ML 기초 실습

## 1. 요약
### 1-1 데이터 셋
  - train_test_split을 통해 전체 데이터셋을 학습셋과 테스트셋으로 분리
    - 테스트셋에 20 % 할당
  - 전체 데이터 개수 : 11094 rows × 9 columns
  - 학습 셋 개수 : 8875 rows × 9 columns
  - 테스트 셋 개수 : 2219 rows × 9 columns

### 1-2 사용 모델
  - 선형회귀 모델
  - 랜덤 포레스트 모델 
  - 학습 테스트 결과 랜덤 포레스트 모델의 오차가 더 적으므로 채택

### 1-3 하이퍼파라미터
  - RandomizedSearchCV를 통해서 탐색
    - n_estimators : 91
    - max_features : 6

### 1-4 평가
  - Mean Absolute Error (평균 절대 오차)
    - 4.342045966651645
  - Under Prediction 비율
    - 약 18.03 %

## 2. 데이터셋
  - predict_delivery_time.csv

### 2-1 데이터 훑어보기
|#|Column|Non-Null Count|Dtype|  
|---|-------------|--------------|--------|  
|0  |Restaurant   |8875 non-null|object |
|1  |Location     |8875 non-null|object |
|2  |Cuisines     |8875 non-null|object |
|3  |AverageCost  |8875 non-null|object |
|4  |MinimumOrder |8875 non-null|int64  |
|5  |Rating       |7908 non-null|object |
|6  |Votes        |7209 non-null|float64|
|7  |Reviews      |7022 non-null|float64|
|8  |DeliveryTime |8875 non-null|int64| 

#### 2-1-1 Average Column
  - 천 단위 구분자 포함
  - 특이값 'for' 존재
#### 2-1-2 Rating Column
  - 숫자형이 아닌 'NEW', 'Opening Soon', 'Temporarily Closed' 존재

### 2-2 숫자형 정보 요약
#### 2-2-1 Describe
|list|MinimumOrder|Votes|Reviews|DeliveryTime|
|----|------------|-----------|------------|-----------|
count| 8875.000000| 7209.000000|7022.000000 |8875.000000|
mean | 53.434817	 | 244.562907 |124.258901  |37.063099|
std  | 19.078793	 | 562.290962 |327.547527  |12.458969|
min  | 0.000000	 | 3.000000	  |1.000000    |10.000000|
25%  | 50.000000	 | 19.000000  |7.000000    |30.000000|
50%  | 50.000000	 | 62.000000  |26.000000   |30.000000|
75%  | 50.000000	 | 211.000000 |90.000000   |45.000000|
max  | 500.000000 |9054.000000 |6504.000000 |120.000000|

#### 2-2-2 상관계수
|list|MinimumOrder|	Votes|	    Reviews|    DeliveryTime|
|------------|----------|------------|---------|--------|
MinimumOrder|1.000000	 |   0.126582|	0.125373|	0.258347|
Votes	    |   0.126582	 |   1.000000|	0.965128|	0.201321|
Reviews	    |   0.125373	 |   0.965128|	1.000000|	0.173577|
DeliveryTime|0.258347	 |   0.201321|	0.173577|	1.000000|

### 2-3 나머지 데이터
  - Cuisines : 음식종류, 총 100가지
  - Restaurant : 음식점 ID
  - Location : 음식점 위치

## 3. 데이터 전처리
### 3-1 AverageCost
  - `replace()`를 통해 천 단위 구분자(',') 제거
  - 특이값을 `np.NaN`으로 치환
  - `astype()`을 적용하여 숫자형으로 변환
  - `interpolate()`를 통해 보간법 적용
    - `method='pad'` : 해당 데이터프레임에 존재하는 값을 보간에 사용
  - 'averageCost_clean()` 메서드로 생성

### 3-2 Rating
  - `replace()`를 통해 숫자가 아닌 데이터들을 `np.NaN`으로 치환
  - `astype()` 적용하여 숫자형으로 변환
  - `interpolate()`를 통해 보간법 적용
    - `method='pad'` : 해당 데이터프레임에 존재하는 값을 보간에 사용
  - 'rating_clean()` 메서드로 생성

### 3-3 Location
  - 비슷한 지명간에 비슷한 값을 갖도록 주소 표기를 역순으로 변경
  - Location과 DeliveryTime 평균이 유의미한 상관관계를 갖도록 딕셔너리 생성
  - `map()` 을 적용하여 Column이 숫자형 데이터를 가지도록 변환
  - 'location_clean()` 메서드로 생성

### 3-4 Cuisines
  - 전체 데이터셋에서 음식 리스트만을 추출
  - `Series.str.replace()`를 적용하여 공백을 제거
  - `Series.str.split()`를 적용하여 리스트 형태로 변환
  - `CountVectorizer` 사용을 위해 ' '문자로 구분된 스트링 형태로 변환
  - `CountVectorizer.fit_transform()` 으로 데이터를 `np.array` 형태로 변환
  - `np.array` 형태를 `pd.DataFrame` 형태로 변환
    - columns 파라미터에 `CountVectorizer.vocabulary_`를 정렬된 상태로 전달
    - index 파라미터에 기존 인덱스를 그대로 전달
  - 생성한 데이터프레임에 `dropna()`를 통해 더미 데이터 제거
  - 'cuisines_transform()` 메서드로 생성

### 3-5 Votes, Reviews
  - Rating Column을 기준으로 데이터프레임을 정렬
  - `interpolate()`를 통해 보간법 적용
  - 'votes_reviews_clean()` 메서드로 생성

### 3-6 dataset_transform()
  - 2-1 ~ 2-5 을 모두 적용
  - 학습에 사용할 데이터셋과 목표값으로 분리하여 리턴

### 3-7 학습에 사용되는 데이터 속성
|Column|Type|Description|
|------|-------|-----------|
|Location|float64|음식점의 위치 속성|
|AverageCost|float64|주문당 평균 가격|
|MinimumOrder|float64|최소 주문 가격|
|Rating|float64|음식점의 평점
|Votes|float64|음식점의 투표 수|
|Reviews|float64|음식점의 리뷰 수|
|(Cuisines)|int64|음식점에서 판매하는 음식의 종류를 벡터 형태로 표시|

## 4. Features
### 4-1 사용 모델
  - 선형회귀 모델
  - 랜덤 포레스트 모델 (채택)

### 4-2 하이퍼파라미터 탐색
  - RandomizedSearchCV
    - n_estimators : 1 ~ 100
    - max_features : 1 ~ 8
    - n_iter : 50
    - cv : 5
    - 결과 최상위 10개
      |Mean Score|	N-Estimators|	Max Features|
      |--------|----|----|
      |11.175174|	91.0|	6.0|
      |11.185630|	71.0|	7.0|
      |11.186637|	90.0|	7.0|
      |11.187392|	80.0|	6.0|
      |11.199346|	95.0|	7.0|
      |11.215683|	63.0|	7.0|
      |11.244028|	98.0|	4.0|
      |11.247284|	75.0|	3.0|
      |11.257173|	83.0|	3.0|
      |11.267178|	94.0|	4.0|

### 4-2 사용 오차 함수
  - MSE (평균 제곱 오차) : scikit-learn에서는 scoring이 클 수록 좋으므로 음수값으로 된 MSE를 사용
    - Linear Regression
      - Scores: [11.4878355  10.37769492 10.91353984 11.81660232 10.98560712 11.1935818 11.68686357 12.72200682 12.67238164 12.00606435]
      - Mean: 11.586217787815928
      - Standard deviation: 0.7174151359822029      
    - Random Forest
      - Scores: [11.87870378  9.99014154 10.90370422 11.47117421 10.37310712 10.95882424 10.92920748 12.18978078 10.69986145 11.34550157]
      - Mean: 11.074000638314562
      - Standard deviation: 0.6319166095688389

## 5. 최종 평가
  - RMSE (평균 제곱근 편차)
    - 10.77286076523536
  - Mean Absolute Error (평균 절대 오차)
    - 4.342045966651645
  - Under Prediction
    - 테스트 데이터 사이즈(df_size) : 2219
    - Under Prediction 개수(under_count) : 400
    - 비율(under_count / df_size)
      - 약 18.03 %