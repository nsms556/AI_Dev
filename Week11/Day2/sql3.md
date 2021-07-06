# [Week11 - Day2] SQL 3

## 1. AWS Redshift
  - 예제 테이블
    - 웹서비스 사용자/세션 정보
      - 사용자 ID : 등록된 사용자마다 부여하는 유일한 ID
      - 세션 ID : 세션마다 부여되는 ID
        - 세션 : 사용자의 방문을 논리적인 단위로 분할
          - 처음 접속 시 생성
          - 세션 만료후 재접속시 생성
        - 한 사용자 - 여러 세션 가능
        - 세션이 생성된 경유지를 채널이란 이름으로 기록
          - 마케팅 기여도 분석 가능
        - 세션 생성 시간 역시 기록
      - 다양한 데이터 분석, 지표 설정
        - 마케팅, 트래픽
        - DAU, WAU, MAU등 액티브 유저 차트
        - 마케팅 채널 속성 분석
      
## 2. SQL
### 2-1 기본
  - 다수의 SQL -> ; 으로 분리 필요
  - 주석
    - -- : 인라인 주석, 한줄
    - /\*--\*/ : 여러줄
  - 키워드
    - 대문자 등 나름대로의 포맷팅이 필요
    - 팀 프로젝트인 경우 공통 포맷 사용
  - 테이블/필드의 명명 규칙 중요
    - 단수 / 복수
    - _ / CamelCasing

### 2-2 DDL - 데이터 정의어
  - CREATE TABLE
    - primary key 지정 가능
      - primary key uniqueness로 인해 무시
    - CTAS : CREATE TABLE table_name AS SELECT
      - vs. CREATE TABLE and the INSERT
  - DROP TABLE
    - 없는 테이블인 경우 에러
      - IF EXISTS 를 통해 존재하는 경우로 한정
    - vs. DELETE FROM
      - 조건에 맞는 레코드를 삭제 -> 테이블 삭제 X
  - ALTER TABLE
    - 새 컬럼 추가
      - ADD COLUMN field_name field_type
    - 컬럼 이름 변경
      - RENAME old_field_name to new_field_name
    - 컬럼 제거
      - DROP COLUMN field_name
    - 테이블 이름 변경
      - RENAME to new_table_name

### 2-3 DML - 데이터 조작어
  - SELECT
    - 테이블에서 레코드와 필드를 읽어오는데 사용
    - WHERE : 조회할 데이터의 조건 지정
    - GROUP BY : 그룹으로 묶어서 조회
    - ORDER BY : 조회할 레코드의 정렬 순서
    - 다수의 테이블을 조인해서 사용하기도 함  
  - 데이터 수정
    - INSERT INTO : 레코드 추가
    - UPDATE FROM : 레코드의 필드 값 수정
    - DELETE FROM : 레코드 삭제
      - vs. TRUNCATE -> 트랜잭션 불가능