# [Week12 - Day4] Online Session
  - 한기용 멘토님

## 1. Spark
  - Spark = Pandas + SQL + Scikit-learn + Streaming
  - Airflow
    - 다양한 ETL 관리를 위한 프레임워크
    - 파이썬으로 작성, 아파치 오픈소스
    - ETL 스케줄링, 코드작성 지원
    - 웹서버, 스케줄러, 워커로 구성
  
### 1-1 과제
  - 타이베이 주택 가격 예측
    - Spark 사용, 어려우면 sckit-learn 사용 가능
    - 회귀 모델 vs 분류 모델
      - RMSE로 정확성 측정
    - VectorAssembler 적용, MinMaxScaler 적용
      - ML Pipeline 추천
    - 선형회귀 등 간단한 ML로 시작
      - 후에 Random Forest, Gradient Boosted Trees 등 복잡한 모델 시도
    - Feature Engineering을 통해 새로운 Feature 생성 가능
      - Feature간 사칙연산을 통해 새로운 Feature 생성
      - 주요 Feature 선택

## 2. 마케팅
### 2-1 마케팅
  - 마케팅에서의 데이터
    - 디지털 마케팅 -> 데이터 기반 마케팅
      - 기본적으로 디지털 미디어를 통해 진행, 다양한 종류 존재
        - 검색엔진, 온라인 비디오, 이메일, 디스플레이, 소셜 미디어 등
    - 디지털 마케팅 -> 자연스럽게 빅데이터 생성
      - 데이터 수집 -> 마케팅 성능 측정 -> 마케팅 방법 개선
      - 데이터의 수집과 분석이 중요해짐
      - 데이터 인프라 없이 불가능
    - 모바일 등장 -> 데이터 수집이 더 복잡해짐
      - 웹과 모바일을 통합하는 마케팅 데이터 수집의 중요성 대두
        - 관련 서비스를 제공해주는 다수의 회사들 존재
  - 분석 필수 데이터
    - ① 접점 데이터 수집 및 저장
      - 최종전환 기록
        - 물건 구매나 회원가입, 앱 설치 등 마케팅의 목표
      - 보조전환 기록
        - 방문시의 행동을 자세하게 기록
          - 물건의 상세정보 확인
          - 쇼핑카트에 담기 등
        - 작은 행동이 모여서 더 의미있는 행동으로 변화 -> 보조전환이 최종전환의 징조
      - 방문 정보들이 계속해서 추출되어야 함
        - 내부 DB에 저장
        - 데이터 수집활동과 수집된 데이터를 저장하는 DB가 마케팅 데이터 인프라의 핵심
    - ② 채널 기여도
      - 효과적인 마케팅 채널, 플랫폼 탐색
        - 접점과 최종 이벤트 등을 기록하여 채널별 기여도 계산 가능
        - 마케팅 실험 가능
          - 효과적인 채널을 찾아 남은 예산의 추가 투자
      - 채널 기여도 측정
        - 마지막 터치
          - 최종 구매전 마지막 채널
        - 마지막 비직접방문 터치
          - 최종 구매전 마지막 채널에 주되 마지막이 직접방문인 경우 이전에 직접방문이 아닌 채널
        - 첫 터치
          - 첫 방문 채널
        - 리니어 (Linear)
          - 모든 채널
        - 타임 디케이 (Time Decay)
          - 접속순서에 따라 기여도 감소
    - ③ 고객 가치
      - 고객의 평생 가치
        - 유저의 초기 행동을 보고 미래의 평생 가치 예측
      - 고객 이탈률 예측
        - 유저가 서비스 사용을 그만 둘지 예측
        - 고객의 여러가지 행동을 모두 기록 필요
  - 경로 데이터 수집의 어려움
    - 로그인 여부에 따라 정보 수집에 제약
    - 개인정보 관련 법률에 따른 제약
    - 대기업들의 개인정보 수집 정책 변경
  - 쿠키
    - Re-Targeting
      - 사이트 방문시 광고가 유저의 다른 방문을 따라다님
    - 쿠키
      - 사이트에서 방문자 식별
      - 퍼스트 파티 쿠키
      - 서드 파티 쿠키
        - 개인정보 유출 위협
  - UTM - 마케팅 채널 기여도 계산 표준
  - 딥링크
    - 앱의 특정 컨텐츠로 링크 가능
    - 링크를 클릭하면 웹사이트가 아닌 앱의 컨텐츠로 연결
    - 검색엔진에서 인덱싱이 가능해짐
    - 표준 존재 X -> 구글과 애플의 방식이 다름

### 2-2 마케팅 데이터 인프라
  - 데이터 인프라
    - 접점과 보조/최종전환 데이터 수집 필요
    - 웨어하우스
    - 수집활동 (ETL)
  - 장점
    - 채널 기여도 계산 자동화
      - ROAS (Return On Advertising Spend)
      - DB가 구축되고 데이터 수집 프로세스가 구현되면 관련 지표 계산이 간단, 에러율 감소
      - 마케터가 계산 X -> 마케팅 본연의 업무에 집중

## 3. QnA
  - pandas가 아닌 spark를 사용해야하는 데이터의 크게에 대한 경험칙이 있을까요. 어느 정도 규모부터 spark를 사용하는지 어림을 알고싶습니다.
    - 대부분 Pandas에서 처리 가능
    - 메모리 문제가 생긴다면 구조 최적화를 통해 가볍게 만들어볼 것
    - 그래도 문제가 생긴다면 시스템의 물리적인 성능(메모리, CPU등)을 높여서 시도 (Scale Up)
    - 스펙을 높이는 것으로 한계가 온다면 분산 시스템등이 필요해진 시점이므로 Spark 사용 (Scale Out)
  - 데이터 엔지니어로서의 취업준비는 어떻게 해야하는지 궁금합니다. ML, DL 지식보단 순수 코딩 실력이 더 중요할까요?
    - 순수 SW 엔지니어보다는 약함 -> 몰라도 된다가 아님
  - Airflow를 공부하려면 어떻게 시작해야할지 막막합니다. 조언 부탁드립니다!
    - 굳이 따로 공부할 정도는 아님
    - 해보고 싶다면 Udemy 추천
    - 프로그래머스 강의 있음