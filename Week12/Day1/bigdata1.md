# [Week12 - Day1] Big Data 1

## 1. 데이터 팀의 역할
  - 미션
    - 신뢰할 수 있는 데이터를 바탕으로 부가가치를 생성
  - 목표
    - 고품질의 데이터 제공 -> 정책 결정에 사용
    - 결정과학
      - 데이터 참고 결정 (Data Informed Decisions)
      - 데이터 기반 결정 (Data Driven Decisions)
    - 고품질 데이터를 필요할 때 제공 -> 유저의 서비스 경험 개선
      - 머신 러닝과 같은 데이터 기반 알고리즘을 통해 개선
      - 개인화 바탕 추천, 검색 기능
      - 사람의 개입이 반드시 필요
        - 데이터 수집 -> 데이터 팀 -> 비즈니스 인사이트 -> 서비스 개선 -> 개선된 서비스의 데이터 수집
  - 발전
    - 데이터 인프라 구축
      - 웨어하우스와 ETL(Extract, Transform, Load)
        - 웨어하우스
          - 회사에 필요한 모든 데이터를 모은 중앙 DB (SQL)
          - Redshift, BigQuery, Snowflake, Hadoop, Spark 등
          - 프로덕션 DB와 별개의 DB
          - 진정한 데이터 조직이 되는 첫 단계
        - ETL
          - 다른 곳에 존재하는 데이터를 가져와서 웨어하우스에 로드
          - Airflow
            - 에어비앤비에서 시작, 파이썬 3 기반
            - AWS, GCP 지원
            - SaaS 사용 가능
      - 데이터 엔지니어가 수행
    - 데이터 분석 수행
      - 분석
        - 회사와 팀별 중요 지표를 정의 -> 대시보드 형태로 시각화
          - 대시보드
            - 주요 지표를 시간의 흐름과 함께 보여주는 것이 일반적
            - 3A(Accessible, Actionable, Auditable) 지표가 중요
            - 구글 Looker, MS PowerBI, Apache Superset
        - 데이터와 관련된 다양한 분석, 리포팅 수행
      - 데이터 분석가가 수행
    - ML/AI 적용

## 2. 데이터 팀 구성원
  - 데이터 엔지니어
    - 소프트웨어 엔지니어
      - 파이썬, 자바, 스칼라 등
    - 데이터 웨어하우스 구축
      - 웨어하우스 생성, 관리 -> 최근 추세는 클라우드
        - AWS, GCP 등
      - 주요 작업 : ETL 코드의 작성과 주기적인 실행
        - 스케줄러, 프레임워크 필요 -> Airflow가 대세
    - 분석가, 과학자 지원
      - 협업을 통해 필요한 툴이나 데이터를 제공
  - 데이터 분석가
    - 웨어하우스 데이터를 기반으로 지표를 만들고 시각화
    - 비즈니스 인텔리전스 담당
      - 주요 지표를 정의 -> 대시보드 시각화
      - 비즈니스 도메인에 대한 깊은 지식 필요
    - 내부 직원들의 데이터 관련 질문 응답
      - 임원, 팀리더들의 결정을 도와줌
      - 질문이 많고, 반복적 -> 셀프서비스화
    - 필요 스킬
      - SQL, 통계
      - 비즈니스 도메인 지식
      - 직접적인 코딩 X
    - 딜레마
      - 많은 수의 긴급한 질문에 시달림
      - 현업팀에 소속되는 경우 많음
        - 커리어의 혼란
        - 고과 기준 불분명
  - 데이터 과학자
    - 과거 데이터를 기반으로 머신러닝 모델을 만들어 고객들의 서비스 경험을 개선
      - 가설을 세우고, 데이터를 수집 -> 모델을 만들어 테스트
        - 많은 시간 필요 -> 짧은 사이클로 시작하여 고도화하는 것이 좋음
        - A/B 테스트 수행
    - 필요 스킬
      - ML/AI에 대한 깊은 지식, 경험
      - 프로그래밍 (파이썬 + SQL)
      - 통계, 수학
      - 끈기, 열정 -> 박사 학위 (노예...)

## 3. ML 모델링 사이클
  - 가설 -> 데이터 수집 -> 분석 -> 모델 개발 -> 런칭 -> 테스트 -> 데이터 수집
  - 방법론
    - Waterfall VS Agile
  - A/B 테스트
    - 온라인 서비스에서 새로운 기능의 효과를 객관적으로 측정
      - 의료 : 무작위 대조 시험
    - 새로운 기능을 런칭함으로써 생기는 위험부담 감소
      - 전체가 아닌 일부에게 시작 -> 관찰 후 범위 결정
    - 유저를 두 ㄱ룹으로 나눠 시간을 두고 관련 지표를 비교
    - 가설과 영향받는 지표를 미리 정하고 시작
      - 성공/실패의 기준 지표 생각 필요

## 4. 조직구조
  - 중앙집중 구조 : 모든 데이터 팀원이 하나의 팀으로 존재
    - 우선 순위는 중앙팀에서 결정
    - 팀원들간 지식, 경험 공유가 쉬워지고 커리어 경로 탐색 쉬움
    - 현업 부서들의 만족도 떨어짐
  - 분산 구조 : 데이터 팀이 부서별로 존재
    - 우선 순위는 각 팀에서 결정
    - 팀원들간 지식, 경험 공유 힘듬
    - 인프라, 데이터 공유 어려움
    - 현업 부서들의 만족도는 높으나 데이터 인력 물갈이가 잦음
  - 하이브리드 구조
    - 가장 이상적인 구조
    - 팀원의 일부는 중앙팀에서 인프라 작업 수행, 일부는 현업팀에 파견되어 작업

## 5. 모델 개발시 고려할 점
  - 개발된 모델의 인수인계 -> 잦은 마찰 발생
    - 많은 수의 과학자들은 R 등 다양한 툴을 사용
    - 그러나 프로덕션 환경은 다양한 모델 지원 X
  - 모델 개발부터 런칭까지 책임자가 필요
    - 개발은 프로젝트의 시작일뿐, 최종 목표는 런칭
    - 참여자들이 같이 크레딧을 받아야 협업이 쉬움
  - 개발 초기부터 소통, 개발/런칭 과정을 구체화
    - 모델 검증법, 인수인계시 모델의 형태, A/B 테스트
  - 개발된 모델을 바로 프로덕션에 런칭해주는 프로세스/프레임워크 필요
    - 트위터 : 특정 파이썬 라이브러리로 모델개발 정책화
      - 툴이 통일되어 제반 개발과 런칭 프레임워크 개발이 쉬워짐
    - AWS SageMaker
      - ML 모델 개발, 검증, 런칭 프레임워크
  - 첫번째 런칭은 시작일 뿐
    - 런칭에서 끝이 아닌 운영을 통해 점진적인 개선이 중요
  - 피드백 루프 필요
    - 운영에서 생기는 데이터를 통해 개선점 탐색
    - 주기적으로 모델을 리빌딩

## 6. 관련 교훈
  - 데이터를 통해 매출이 생겨야 한다
    - 회사는 결국 이익 집단
      - 어떤 조직이던 매출을 창조하거나 경비를 절감해야함
      - 데이터 인프라와 데이터 팀원의 비용은 상대적으로 높음
      - 회사 수익에 직간접적으로 긍정적인 영향을 만들어야함
    - 데이터 팀 수장의 역할이 중요
      - 수직/수평적으로 관리를 잘 해야함
      - 인프라 구성이 첫번째이지만 단기적으로 좋은 결과를 낼 방법 탐색 필요
  - 데이터 인프라가 첫 단계
    - 인프라 없는 분석이나 모델링 불가능
      - 매우 작은 회사는 생존이 더 중요
      - 데이터 인력으로 인프라 구축 외에 약간의 분석/모델링 스킬이 있는 사람이 최적
    - 클라우드 VS 로컬
    - 배치 VS 리얼타임
  - 데이터의 품질이 중요
    - 쓰레기에서는 쓰레기만 나온다
    - 과학자가 가장 많은 시간을 쓰는 분야는 데이터 클린업
    - 중요 데이터는 퀄리티 유지에 노력이 필요
      - 데이터의 위치
      - 문제 발생에 대한 모니터링
  - 지표부터 생각
    - 어떤 일이든지 성공 척도를 먼저 생각
      - 가설을 세우는 것이 시야를 넓히는데 도움
    - 지표의 계산에 객관성 중요
      - 지표가 신뢰성이 없으면 큰 문제
      - 어떻게 계산하고 어떻게 설명할지를 고려
  - 간단한 솔루션에서 시작
    - 모든 문제를 딥러닝으로 해결 X
      - 간단한 논리로 해결 가능한지 부터 고민
      - 딥러닝으로 해결한 경우는 드뭄
      - 동작에 대한 설명도 힘들고, 개발과 런칭에 오래 걸림
    - 점진적인 개발 VS 한번에 모델 생성
      - 후자의 경우 시간은 오래 걸리고 결과는 안 좋을 확률이 높음
      - 전자로 가면서 원하는 결과가 나올때 중단, 개선 필요 X