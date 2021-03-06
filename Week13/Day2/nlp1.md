# [Week13 - Day2] NLP 1

## 1. 자연어 처리 소개
  - 자연어의 의미를 컴퓨터로 분석해서 특정 작업을 위해 사용할 수 있도록 하는 것
  - 분야
    - 기계번역, 감성분석, 문서분류, 질의응답
    - 챗봇, 언어생성, 음성인식, 추천시스템
  - 컴퓨터 비전 모델을 NLP에 적용하면서 성능이 상승
  - 최근 NLP에 딥러닝을 적용하면서 생긴 NLP 모델들이 역으로 컴퓨터 비전에서 활용되기 시작

## 2. 텍스트 전처리
  - 단어
    - 문장이 가진 단어의 갯수
      - 문장부호의 포함 여부
    - 구어체 문장
      - fragments, filled-pauses(uh, um 등)
    - 표제어 : 여러단어가 공유하는 뿌리단어
    - 표제어를 공유하는 다양한 단어형태가 나타남 (cat, cats)
    - Vocabulary : 단어의 집합
    - Type : Vocabulary의 한 원소
    - Token : 문장 내에 나타나는 한 단어
  - 말뭉치 (Corpus)
    - 대용량의 문서들의 집합
    - 특성은 요소에 따라 달라짐
      - 언어 (세계적으로 7097개의 언어 존재)
      - 방언
      - 장르 (뉴스, 소설, 기술문서 등)
      - 글쓴이의 인구통계적 속성 (나이, 성별, 인종 등)
    - 말뭉치에 적용할 수 있는 NLP 알고리즘이 바람직
  - 텍스트 정규화
    - 모든 NLP는 텍스트 정규화가 필요
      - 토큰화 (Tokenizing words)
      - 단어 정규화 (Normalizing Word Formats)
      - 문장 분절화 (Segmenting Sentences)
  - Unix 명령어를 통한 토큰화
    - tr -sc 'A-za-z' '\n' < *.txt
    - 문제점
      - 문장부호를 항상 무시할 수 없음
        - 단어 안에 나타나는 문장부호, 화폐단위, 날짜 등
        - Ph.D., AT&T, $12.50, 2021/07/27 등
      - 문장부호가 단어의 의미를 명확하게 하는 경우는 제외시키면 안됨
      - 접어 : 다른 단어에 붙어서 존재하는 형태
        - we're -> we are
      - 여러 개의 단어가 붙어야 의미가 있는 경우
        - New York, rock'n'roll
  - 중국어
    - 단어의 기준이 애매모호함
  - 한국어
    - 토큰화가 복잡함
    - 띄어쓰기가 잘 지켜지지 않고 띄어쓰기가 제대로 되어도 한 어절이 하나 이상의 의미 단위가 가능
    - 형태소(Morpheme) : 뜻을 가진 가장 작은 말의 단위
      - 자립 형태소 : 명사, 대명사, 부사 등
      - 의존 형태소 : 다른 형태소와 결합하여 사용되는 형태소, 접사, 조사, 어미 등
    - 단어보다 작은 단위(subword)로 토큰화가 필요
  - Subword Tokenization
    - 학습데이터에 나타나지 않은 새로운 단어
    - 알고리즘
      - Byte-Pair Encoding
      - WordPiece
      - Unigram Language Modeling
    - 구성요소
      - Token learner : 말뭉치에서 vocabulary를 생성
      - Token Segmenter : 새로운 문장을 토큰화
    - Byte-Pair Encoding (BPE)
      - Voca를 단일 문자의 집합으로 초기화
      - 과정
        - 말뭉치에서 연속적으로 가장 많이 발생하는 두개의 기호들을 탐색
        - 두 기호를 병합, 새로운 기호로 voca에 추가
        - 말뭉치에서 두 기호들을 병합된 기호로 모두 교체
      - 위 과정을 k번의 병합이 생길때까지 반복
      - 기호 병합은 단어안에서만 수행
      - 이를 위해 단어끝을 나타내는 특수기호(_)를 단어 뒤에 추가, 각 단어를 문자 단위로 쪼갬
      - Token Segmenter
        - 새로운 단어에 대한 토큰화 방법
        - Greedy 적용 : 병합을 학습한 순서대로 적용
        - 자주 나타나는 단어가 하나의 토큰으로 병합
        - 드문 단어는 subword로 분할
    - WordPiece
      - 기호들의 쌍을 찾을때 빈도수 대신 Likelihood를 최대화시키는 쌍을 탐색
    - Unigram
      - 확률모델 사용
      - 학습 데이터 내의 문장을 관측 확률변수로 정의
      - 토큰화를 잠재 확률변수로 정의
      - 데이터의 주변 우도를 최대화 시키는 토큰화를 탐색
        - Expecation Maximization
        - Maximization step에서 Viterbi 알고리즘 사용
  - 단어정규화
    - 단어들을 정규화된 형식으로 표현
    - 검색엔진에서 문서들을 추출할때 유용
    - Case Folding
      - 모든 문자들을 소문자화 함
        - 일반화에 유용 : 학습/테스트 데이터간 불일치 문제에 도움
        - 정보검색, 음성인식 등에 유용
        - 감성분석 등 문서분류 문제에서는 오히려 방해가 될 수 있음(US vs us)
    - Lemmantization
      - 어근을 사용해서 표현
        - are, is -> be
    - 필요성
      - 단어 사잉의 유사성 이해
      - 같은 의미를 가진 여러 형태의 단어들을 하나로 대응
    - 경향
      - 단어를 voca로 정의된 공간(고차원 희소 벡터)이 아닌 저차원 밀집 벡터로 대응
        - 단어 임베딩을 사용하면 단어정규화의 필요성이 줄어듬