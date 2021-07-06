# [Week11- Day2] SQL 4

## 1. 실습에 앞서
  - 현업에 깨끗한 데이터란 존재하지 않음
    - 데이터의 신뢰성에 대해 의심할 것
    - 실제 데이터를 보는 것만한 방법이 없음
  - 데이터 품질을 의심하고 체크하는 습관이 필요
    - 중복 레코드 체크
    - 최근 데이터의 존재 여부 확인
    - primary key uniqueness 만족여부
    - 값이 없는 컬럼
    - 유닛테스트 형태로 만들어 쉽게 체크 가능
  - 어느 시점을 넘어가는 순간 너무 많은 테이블이 존재
    - 회사 성장과 관련
    - 주요 테이블과 메타정보의 관리가 중요
  - Data Discovery 문제
    - 내가 원하고 신뢰할 만한 데이터가 어느 테이블인가?
    - 테이블에 대해 질문하고 싶은데 누구에게 해야 하는가?
    - 문제 해결을 위한 다양한 서비스
      - DataHub(링크드인), Amunsen(Lyft)
      - Select Star, DataFrame

## 2. SELECT
  - 테이블에서 레코드들을 조회
  - WHERE를 통해 조건 지정
    ``` SQL
    SELECT field_name1, field_name2, ...
    FROM table_name
    WHERE condition
    GROUP BY field_name3
    ORDER BY field_name4 [ASC/DESC]
    LIMIT N;
    ```
  - CASE WHEN
    - 필드 값의 변환을 위해 사용 가능
      - CASE WHEN condition THEN true_value ELSE false_value END field_name
    - 여러 조건을 사용하여 변환도 가능
  - NULL
    - 값이 존재하지 않음 -> 0이나 ""과 다름
      - 휴지심만 있는 경우 vs 휴지심이 아예 없는 경우 <del>ㄹㅇ 반박 불가 팩트</del>
    - 필드 지정시 값이 없는 경우
    - NULL 비교에는 특수한 문법 필요
      - field1 is NULL or field1 in not NULL
    - 사칙연산에 사용시 결과는 전부 NULL
  - COUNT
    - 테이블에서 조건을 만족하는 레코드의 수를 반환
  - WHERE
    - 조회할 데이터의 조건 지정
    - IN
      - WHERE channel in ('Google', 'Youtube')
    - LIKE and ILIKE
      - 와일드카드 문자 사용
      - LIKE : 완전 일치
      - ILIKE : 대소문자 구분 X 등 완전 일치 X
    - BETWEEN
      - 범위 지정
    - CASE WHEN에도 사용 가능
  - STRING function
    - LEFT : 왼쪽부터 N 만큼 잘라냄
    - REPLACE
    - UPPER
    - LOWER
    - LEN
    - LPAD, RPAD
    - SUBSTRING
  - ORDER BY
    - 기본값은 오름차순
    - DESC 적용시 내림차순
    - NULL
      - 오름차순 기준으로 마지막에 위치
      - NULLS FIRST, NULLS LAST를 통해 위치 변경 가능

## 3. 타입 변환
  - DATE Conversion
    - Timezone 관련
      - CONVERT_TIMEZONE
    - DATE, TRUNCATE
    - DATE_TRUNC
    - EXTRACT or DATE_PART
      - 날짜에서 특정 부분 추출
    - DATEDIFF
    - DATEADD
      - 날짜에서 며칠 후 계산
    - GET_CURRENT
  - TO_CHAR, TO_TIMESTAMP
  - 타입 캐스팅
    - :: operator 사용
      - category::float
    - cast 함수 사용
      - cast(category as float)
