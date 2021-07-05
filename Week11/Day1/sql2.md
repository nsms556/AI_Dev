# [Week11 - Day1] SQL 2

## 1. 데이터 웨어하우스
  - 회사에 필요한 모든 데이터를 저장
  - SQL 기반의 관계형 DB
    - 프로덕션 DB와 분리 필수
    - AWS의 Redshift, 구글의 Big Query 등
  - 고객이 아닌 내부 직원을 위한 DB
    - 처리속도 < 처리 데이터의 크기
  - ETL or 데이터 파이프라인
    - 외부의 데이터를 읽어서 웨어하우스로 저장
  - 데이터 인프라
    - 데이터 엔지니어 관리
    - Spark 등 대용량 분산처리 시스템이 추가됨

## 2. 클라우드, AWS
  - 정의
    - 컴퓨팅 자원을 네트워크를 통해 서비스 형태로 사용
    - 자원을 필요한만큼 실시간으로 할당하여 사용한 만큼 비용 지불
      - 탄력적으로 필요한만큼의 자원을 유지하는것이 중요
  - 없다면?
    - 서버/네트워크/스토리지 직접 관리
    - 데이터센터 공간 확보, 관리
    - 피크 기준으로 캐패시티 플래닝 필요
  - 장점
    - 초기 투자 비용이 큰폭으로 감소
    - 리소스 준비를 위한 대기시간 감소
    - 유휴 리소스 제거
    - 글로벌 확장이 용이
    - SW 개발 시간 단축
  - EC2
  - S3
  - 기타 (AI & ML)
    - SageMaker
    - LEX
    - Polly
    - Rekognition
  - 기타 서비스
    - Alexa
    - Connect
    - Lambda

## 3. Redshift
  - Scalable SQL 엔진
    - 2 페타바이트까지 지원
    - Still OLAP
      - 응답속도 느림 -> 프로덕션 DB로 사용 불가
    - Columnar 스토리지
      - 컬럼별 압축가능
      - 컬럼 추가/삭제가 빠름
    - 벌크 업데이트
      - 레코드가 들어있는 파일을 S3로 복사 후 COPY 커맨드를 통해 일괄복사
    - 고정 용량/비용
    - 기본키 uniqueness 보장 X
  - PostgreSQL 8.x 와 호환
    - 모든 기능을 지원하는 것은 아님
    - PostgreSQL 8.x 지원 툴, 라이브러리로 액세스 가능
    - SQL이 메인
      - 테이블 디자인이 중요
  - Schema 구성
    - DEV
      - raw_data
      - analytics
      - adhoc
  - 액세스
    - Google Colab
    - PostgreSQL 8.x 호환툴, 언어
      - SQL Workbench, Postico
      - Python - Psycopg2
      - Looker, Tableau 등 시각화