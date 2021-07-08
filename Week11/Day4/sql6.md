# [Week11 - Day4] SQL 6

## 1. JOIN
  - 2개 이상의 테이블들을 공통 필드를 통해 하나로 통합
  - Star Schema로 분산된 테이블들의 데이터를 통합
  - 조인 방식에 따라 선택할 레코드, 조회할 필드가 달라짐
    - INNER
      - 테이블 들의 공통내용만 출력
    - FULL
      - 테이블에서 공통 내용이 아닌것도 출력
    - CROSS
    - LEFT
      - 첫번째 테이블에서만 공통 내용이 아닌것도 출력
    - RIGHT
      - 두번째 테이블에서만 공통 내용이 아닌것도 출력
    - SELF
  - 고려해야할 점
    - 중복 레코드가 없고 primary key uniqueness 보장 체크
    - 테이블간의 관계를 명확히 정의
      - 1 to 1
      - 1 to M
        - 중복인 경우 문제가 커짐
      - M to 1
        - 1 to M에서 방향만 변경
      - M to M
        - 가능하다면 1 to 1이나 1 to M으로 변환하여 조인
    - 베이스로 잡을 테이블을 결정

### 1-1 다양한 JOIN
  - LEFT / RIGHT
    - 베이스 테이블의 모든 레코드를 리턴
    - 반대 테이블은 매칭되는 데이터가 있으면 필드를 만들어서 리턴 
  - FULL
    - 양쪽 테이블의 모든 레코드를 리턴
    - 매칭되는 레코드만 모든 필드들이 채워진 상태로 리턴
  - CROSS
    - 양쪽 테이블의 모든 레코드 조합을 리턴
    - 레코드 3개 * 레코드 4개 -> 레코드 12개를 가진 테이블 리턴
  - SELF
    - 동일한 테이블을 alias만 달리해서 자기 자신과 조인

## 2. boolean 처리 / NULL 처리
  - boolean
    - True or False
    - 실제 데이터에는 NULL인 경우도 있음에 주의
  - NULL
    - 비교는 항상 IS, IS NOT으로 수행
    - =, != 등을 사용하면 잘못된 결과가 출력
  - NULLIF
    - 0 으로 나누면 Divided by zero 에러 발생
    - NULLIF(A, B)
      - A, B의 값이 같으면 NULL을 리턴, 다르면 A를 리턴
  - COALESCE
    - NULL을 다른 값으로 변경
    - COALESCE(exp1, exp2, exp3, ...)
    - exp1 부터 인자를 하나씩 살펴서 NULL이 아닌 값이 발견되면 리턴
    - 발견 못하면 NULL을 리턴
  - 공백 혹은 예약어를 필드명으로 사용
    - ""으로 둘러싸서 사용

## 3. 숙제
  - 사용자별로 처음 채널과 마지막 채널 검색
    - 시간순으로 봤을때 251번 유저의 첫번째 채널과 마지막 채널
    - ROW_NUMBER 사용
  - Gross Revenue가 가장큰 userid 10개
  - raw_data.nps 테이블을 바탕으로 월별 NPS 계산
    - 고객들이 0 에서 10 점수 매김 (의향 없음 ~ 매우 높음)
    - detractor : 0 ~ 6
    - passive : 7, 8
    - promoter : 9, 10
    - NPS = promoter 퍼센트 - detractor 퍼센트