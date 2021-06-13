## 발표 자료
  - 7시 반

## 데이터
  -
    |Columns|Description|
    |-----------|----------------|
    |SalePrice         |부동산의 판매 가격 (달러) |
    |MSSubClass        |건물 등급
    |MSZoning          |일반 구역 분류
    |LotFrontage       |부동산에 연결된 거리의 선형 피트
    |LotArea           |평방 피트 단위의 부지 크기
    |Street            |도로 접근 유형
    |Alley             |골목 접근 유형
    |LotShape          |속성의 일반적인 모양
    |LandContour       |부동산의 평탄도
    |Utilities         |사용 가능한 유틸리티 유형
    |LotConfig         |로트 구성
    |LandSlope         |재산의 경사
    |Neighborhood      |에임스시 경계 내의 물리적 위치
    |condition 1       |주요 도로 또는 철도와의 근접성
    |condition 2       |주요 도로 또는 철도와의 근접성 (두개 이상인 경우)
    |BldgType          |주거 유형
    |HouseStyle        |주거 스타일
    |OverallQual       |전체 재료 및 마감 품질
    |OverallCond       |전체 상태 등급
    |YearBuilt         |원래 건설 날짜
    |YearRemodAdd      |리모델링 날짜
    |RoofStyle         |지붕 유형
    |RoofMatl          |지붕 재료
    |Exterior1st       |집 외부 커버
    |Exterior2nd       |집의 외피 (하나 이상의 재료 인 경우)
    |MasVnrType        |벽돌 베니어 유형
    |MasVnrArea        |벽돌 베니어 면적 (평방 피트)
    |ExterQual         |외장재 품질
    |ExterCond         |외장재의 현황
    |Foundation        |기초 유형
    |BsmtQual          |지하 높이
    |BsmtCond          |지하실의 일반 상태
    |BsmtExposure      |워크 아웃 또는 정원 수준의 지하 벽
    |BsmtFinType1      |지하실 마감 면적의 품질
    |BsmtFinSF1        |유형 1 완성 평방 피트
    |BsmtFinType2      |두 번째 완성 된 영역의 품질 (있는 경우)
    |BsmtFinSF2        |유형 2 마감 평방 피트
    |BsmtUnfSF         |미완성 된 지하실 면적
    |TotalBsmtSF       |지하 총 평방 피트
    |Heating           |난방 유형
    |HeatingQC         |난방 품질 및 상태
    |CentralAir        |중앙 에어컨
    |Electrical        |전기 시스템
    |1stFlrSF          |1 층 평방 피트
    |2ndFlrSF          |2 층 평방 피트
    |LowQualFinSF      |저품질 마감 평방 피트 (모든 층)
    |GrLivArea         |지상 (지상) 생활 면적 평방 피트 위
    |BsmtFullBath      |지하 전체 욕실
    |BsmtHalfBath      |지하 반 욕실
    |FullBath          |등급 이상의 전체 욕실
    |HalfBath          |학년 이상의 절반 목욕
    |Bedroom           |지하층 이상의 침실 수
    |Kitchen           |주방 수
    |KitchenQual       |주방 품질
    |TotRmsAbvGrd      |학년 이상의 총 방 (화장실 제외)
    |Functional        |홈 기능 등급
    |Fireplace         |벽난로 수
    |FireplaceQu       |벽난로 품질
    |GarageType        |차고 위치
    |GarageYrBlt       |차고 건설 연도
    |GarageFinish      |차고 내부 마감
    |GarageCars        |차량 수용 가능 차고 크기
    |GarageArea        |차고 크기 (평방 피트)
    |GarageQual        |차고 품질
    |GarageCond        |차고 상태
    |PavedDrive        |포장 된 진입로
    |WoodDeckSF        |목재 데크 면적 (평방 피트)
    |OpenPorchSF       |평방 피트 단위의 열린 현관 영역
    |EnclosedPorch     |닫힌 현관 영역 (평방 피트)
    |3SsnPorch         |평방 피트 단위의 3 계절 현관 면적
    |ScreenPorch       |스크린 현관 영역 (평방 피트)
    |PoolArea          |수영장 면적 (평방 피트)
    |PoolQC            |수영장 품질
    |Fence             |울타리 품질
    |MiscFeature       |다른 카테고리에서 다루지 않는 기타 기능
    |MiscVal           |기타 기능의 달러 가치
    |MoSold            |월 판매
    |YrSold            |판매 연도
    |SaleType          |판매 유형
    |SaleCondition     |판매 조건

### `DataFrame.info()`
<class 'pandas.core.frame.DataFrame'>  
RangeIndex: 1460 entries, 0 to 1459  
Data columns (total 81 columns):

|#|Column|Non-Null Count|Dtype|Thinking|
|--|-------|----------------|-------|------|
|0 |Id           |1460 non-null|int64  ||
|1 |MSSubClass   |1460 non-null|int64  ||
|2 |MSZoning     |1460 non-null|object ||
|3 |LotFrontage  |1201 non-null|float64||
|4 |LotArea      |1460 non-null|int64  ||
|5 |Street       |1460 non-null|object ||
|6 |Alley        |91 non-null  |object |Null 데이터가 너무 많음|
|7 |LotShape     |1460 non-null|object ||
|8 |LandContour  |1460 non-null|object ||
|9 |Utilities    |1460 non-null|object ||
|10|LotConfig    |1460 non-null|object ||
|11|LandSlope    |1460 non-null|object ||
|12|Neighborhood |1460 non-null|object ||
|13|Condition1   |1460 non-null|object ||
|14|Condition2   |1460 non-null|object ||
|15|BldgType     |1460 non-null|object ||
|16|HouseStyle   |1460 non-null|object ||
|17|OverallQual  |1460 non-null|int64  ||
|18|OverallCond  |1460 non-null|int64  ||
|19|YearBuilt    |1460 non-null|int64  ||
|20|YearRemodAdd |1460 non-null|int64  ||
|21|RoofStyle    |1460 non-null|object ||
|22|RoofMatl     |1460 non-null|object ||
|23|Exterior1st  |1460 non-null|object ||
|24|Exterior2nd  |1460 non-null|object ||
|25|MasVnrType   |1452 non-null|object ||
|26|MasVnrArea   |1452 non-null|float64||
|27|ExterQual    |1460 non-null|object ||
|28|ExterCond    |1460 non-null|object ||
|29|Foundation   |1460 non-null|object ||
|30|BsmtQual     |1423 non-null|object ||
|31|BsmtCond     |1423 non-null|object ||
|32|BsmtExposure |1422 non-null|object ||
|33|BsmtFinType1 |1423 non-null|object ||
|34|BsmtFinSF1   |1460 non-null|int64  ||
|35|BsmtFinType2 |1422 non-null|object ||
|36|BsmtFinSF2   |1460 non-null|int64  ||
|37|BsmtUnfSF    |1460 non-null|int64  ||
|38|TotalBsmtSF  |1460 non-null|int64  ||
|39|Heating      |1460 non-null|object ||
|40|HeatingQC    |1460 non-null|object ||
|41|CentralAir   |1460 non-null|object ||
|42|Electrical   |1459 non-null|object ||
|43|1stFlrSF     |1460 non-null|int64  |1stFlrSF와 2ndFlrSF를 묶어서 TotalFlrSF으로 사용해보기|
|44|2ndFlrSF     |1460 non-null|int64  |1stFlrSF와 2ndFlrSF를 묶어서 TotalFlrSF으로 사용해보기|
|45|LowQualFinSF |1460 non-null|int64  |TotalFlrSF 대비 마감 퀄리티가 떨어지는 비율|
|46|GrLivArea    |1460 non-null|int64  ||
|47|BsmtFullBath |1460 non-null|int64  ||
|48|BsmtHalfBath |1460 non-null|int64  ||
|49|FullBath     |1460 non-null|int64  ||
|50|HalfBath     |1460 non-null|int64  ||
|51|BedroomAbvGr |1460 non-null|int64  ||
|52|KitchenAbvGr |1460 non-null|int64  ||
|53|KitchenQual  |1460 non-null|object ||
|54|TotRmsAbvGrd |1460 non-null|int64  ||
|55|Functional   |1460 non-null|object ||
|56|Fireplaces   |1460 non-null|int64  ||
|57|FireplaceQu  |770 non-null |object ||
|58|GarageType   |1379 non-null|object ||
|59|GarageYrBlt  |1379 non-null|float64||
|60|GarageFinish |1379 non-null|object ||
|61|GarageCars   |1460 non-null|int64  ||
|62|GarageArea   |1460 non-null|int64  ||
|63|GarageQual   |1379 non-null|object ||
|64|GarageCond   |1379 non-null|object ||
|65|PavedDrive   |1460 non-null|object ||
|66|WoodDeckSF   |1460 non-null|int64  ||
|67|OpenPorchSF  |1460 non-null|int64  ||
|68|EnclosedPorch|1460 non-null|int64  ||
|69|3SsnPorch    |1460 non-null|int64  ||
|70|ScreenPorch  |1460 non-null|int64  ||
|71|PoolArea     |1460 non-null|int64  ||
|72|PoolQC       |7 non-null   |object |Null 데이터가 너무많음|
|73|Fence        |281 non-null |object ||
|74|MiscFeature  |54 non-null  |object |Null 데이터가 너무많음|
|75|MiscVal      |1460 non-null|int64  ||
|76|MoSold       |1460 non-null|int64  ||
|77|YrSold       |1460 non-null|int64  ||
|78|SaleType     |1460 non-null|object ||
|79|SaleCondition|1460 non-null|object ||
|80|SalePrice    |1460 non-null|int64  ||

dtypes: float64(3), int64(35), object(43)

## 이상치
