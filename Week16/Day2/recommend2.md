## [Week16 - Day2] Recommendation System 2

## 1. 넷플릭스 프라이즈
  - 넷플릭스의 추천 엔진 경진대회, 2006년부터 3년간 진행
  - 넷플릭스의 추천 시스템 품질을 10% 이상 개선하는 팀에게 100만 달러 수여
    - RMSE를 통해 품질 평가
  - 결과
    - 넷플릭스 브랜드 인지도 상승
    - 프라이버시 이슈 제기
    - Kaggle 등 머신러닝 경진대회 플랫폼들이 등장
  - 최종 우승 : BellKor's Pragmatic Chaos
  - 이 대회를 통해 협업 필터링이 발전
    - SVD++는 이후 많은 분야에서 활용
    - 앙상블 방식의 모델들이 가장 좋은 성능
      - 실행시간의 문제로 실제 프로덕션에 적용 불가능
    - 다양한 알고리즘들이 논문으로 발표

## 2. 발전
  - 2001 아마존에서 아이템 기반 협업 필터링 논문 발표
  - 2006 ~ 2009 넷플릭스 프라이즈
    - SVD를 이용한 유저의 아이템 평점 예측 알고리즘
    - 앙상블 알고리즘 보편화
    - Restricted Boltzman Machine (RBM)이 단일 모델로 최고의 성능
      - 딥러닝의 추천 분야 가능성을 보임
  - 2010 딥러닝이 아이템 기반 음악 추천에 사용되기 시작
  - 2016 딥러닝 기반 추천이 상승세 시작
    - 오토인코더 기반으로 복잡한 행렬 계산을 단순화
    - 아이템 관련 유저 정보를 시간순으로 인코딩하는 RNN 사용
    - 아마존에 DSSNTE 알고리즘을 오픈소스화 -> 이후 SageMaker로 통합

## 3. Udemy 추천 엔진
  - 문제 : 학생들이 관심있을 만한 강의를 먼저 노출
  - UI
    - 격자 기반 UI
    - 다양한 추천 유닛
      - 유닛의 순서 결정 -> 유닛 선택과 랭킹
      - 페이지 생성 시간-사용자 만족도는 반비례 관계 -> 많은 유닛은 역효과
  - 온라인 강의 메타 데이터
    - 분류 체계, 태그, 클릭 키워드 분석
  - 다양한 행동 기반 추천
    - 클릭, 구매, 소비 등
  - 기본 아이디어
    - 하이브리드 방식
      - 협업 필터링 + 유저 행동 기반 + 머신러닝 모델 기반
    - 사용자별로 등록 확률을 기준으로 2000개의 탑 강의 목록
      - 배치 -> 실시간으로 변경
    - 홈페이지에서의 추천 -> 개인화
      - 유닛 후보 생성
      - 유닛 후보 랭킹
    - 특정 강의 세부 페이지 -> 아이템 중심
      - 이 강의를 들은 학생들이 구매한 강의 (아이템 기반 협업 필터링)
      - 이 강의와 함께 자주 구입된 강의 (별도의 동시발생 행렬 계산)
      - 각 유닛에서의 강의 랭킹은 개인별 등록 확률 기준

## 4. 인기도 기반 추천 유닛 개발
  - Cold Start 없음
  - 인기도 기준 : 평점? 매출? 판매량?
  - 유저 정보에 따라 확장
    - 서울 지역 인기 아이템, 20대 인기 아이템 등
  - 개인화 X
  - 아이템 분류 체계 존재 여부에 따라 확장
    - 특정 카테고리의 인기 아이템
    - 분류 체계를 갖는것이 유리
  - 인기도의 기준을 바꿔 다양한 추천 유닛 생성 가능
  - Cold Start 문제가 없는 추천 유닛
    - 현재 유저들이 구매한 아이템
    - 현재 유저들이 보고 있는 아이템