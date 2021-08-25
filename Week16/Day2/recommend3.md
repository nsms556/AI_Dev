# [Week16 - Day2] Recommendation System 3

## 1. 유사도 측정
  - 다양한 유사도 측정 알고리즘
    - 유사도 측정 : 벡터들간의 유사도 판단
      - 대표 : 코사인 유사도, 피어슨 유사도
    - 코사인 유사도 : N차원 공간에 있는 두 벡터간의 각도를 보고 유사도를 판단
    - 피어슨 유사도 : 평점처럼 방향 + 벡터 크기의 정규화가 중요할 때 사용
  - 피어슨 유사도
    - 벡터 A, B의 값을 보정
      - 각 벡터 내 셀들의 평균을 구해 각 셀에서 평균값을 빼줌
    - 이후 코사인 유사도와 동일하게 계산
      - 중앙 코사인 유사도, 보정된 코사인 유사도
    - 장점
      - 모든 벡터가 원점을 중심으로 이동 -> 벡터간 비교가 더 쉬워짐
        - 까다로운 사용자와 아닌 사용자를 정규화하는 효과

## 2. TF-IDF
  - 텍스트를 벡터로 표현하는 법
    - 여러가지 방법 존재
      - 기본적으로 단어를 행렬의 차원으로 표현
      - Bag of Words 방식은 문서들에 나타나는 단어수가 N개이면 N차원으로 문서 표현
    - 원핫 인코딩 + Bag of Words (카운팅)
      - 단어의 수를 카운팅
      - Stopword 제외 -> 단어 수 계산 -> 단어별로 차원 배정
      - `sklearn.feature_extraction.text.CountVectorizer`
    - 원핫 인코딩 + Bag of Words (TF-IDF)
      - 단어를 TF-IDF 알고리즘으로 계산된 값으로 표현
  - TF-IDF
    - 한 문서에서 중요한 단어 대신 문서군 전체를 보고 판단
    - 어떤 단어가 한 문서에서 자주 나오면 중요 -> 이 단어가 다른 문서들에서 자주 등장하지 않는다면 더 중요
    - 카운트 기반 Bag of Words에 단어 카운트 대신 TF-IDF 사용
      - TF-IDF = TF(t,d) * IDF(t)
    - `sklearn.feature_extraction.text.TfidfVectorizer`
    - 문서간 유사도 계산
      - `sklearn.metrics.pairwise.cosine_similarity`
    - 문제점
      - 정확하게 동일한 단어가 나와야 유사도 계산 가능
        - 동의어 처리 X
      - 단어 수, 아이템 수가 늘어나면 계산이 오래 걸림
      - 결국 Word Embedding이 더 좋음
        - 아니면 LSA 등 차원 축소 방식을 적용