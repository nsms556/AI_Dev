# [Week4 - Day6] 세션 : Kaggle

## Kaggle
  - 역사
    - 2010, 호주에서 시작
    - 2019, 구글에서 인수

  - 소개
    - 머신러닝 경진대회를 위한 플랫폼
      1. 기업에서 문제를 낸다
      2. 참가자들이 문제를 풀며 논의
      3. 입상하면 상금 (보통 5위 이내)

  - 성적 분류
    - Competitions : 경진대회
    - Datasets : 데이터셋 공유
    - Notebooks : 데이터 보고서 공유
    - Discussion : 토론 커뮤니티

  - Notebook 필사
  - Progression

## 예제 Competition
  - Titanic - Machine Learning from Disaster
    - Start here! Predict survival on the Titanic and get familiar with ML basics
    - https://www.kaggle.com/c/titanic
  - Natural Language Processing with Disaster Tweets
    - Predict which Tweets are about real disasters and which ones are not
    - https://www.kaggle.com/c/nlp-getting-started

## 해로운새 NLP 진행해보기
  - 데이터 로딩 + 아이디어 수집
    - 데이터셋의 분류 비율 확인
      - 비슷한 비율 -> ??? -> Profit!!!
      - 극단적인 비율 -> 부족한 데이터의 생성이나 기존 데이터의 분할 등
  - 클래스 분류
  - EDA
    - 단어 수
    - 평균 단어 길이
    - Stopword (불용어)
      - 조사, 접미사 같은 단어들은 문장에서는 자주 등장하지만 실제 의미 분석을 하는데는 거의 기여하는 바가 없는 경우\
    - 구두점 분석
    - 많이 등장하는 단어
    - 단어간 조합
  - Data Cleaning
    - url 제거
    - html 태그 제거
    - 이모지 제거
    - 구두점 제거
    - 철자 체크
  - GloVe For Vectorization
    - Word Embedding : 모델 입력을 위해 단어를 숫자화
  - Baseline Model
    