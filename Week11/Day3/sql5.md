# [Week11 - Day3] SQL 5

## 1. GROUP BY, AGGREGATE
  - 테이블의 레코드를 그룹핑하여 그룹별로 정보를 계산
    1. 그룹핑할 필드를 결정
      - 하나 이상 가능
    2. 그룹별로 계산할 내용을 결정
      - aggregate 사용
      - count, sum, avg, min, mx, listagg
  - 월별 세션수 계산
    - raw_data.session_timestamp를 사용
  - 가장 많이 사용된 채널?
    - 가장 많이 사용되었다의 정의
    - 필요한 정보 - 채널 정보, 유저 정보, 세션 정보
    - 어느 테이블을 사용해야 하는지
      - user_session_channel
      - session_timestamp
  - 가장 많은 세션을 만든 사용자?
    - 필요한 정보 - 세션정보, 유저 정보
    - 필요 테이블
      - user_session_channel
  - 월별 유니크 사용자
    - MAU
    - 필요한 정보 - 시간, 유저
    - 필요 테이블
      - user_session_channel (userId, *sessionId*, channel)
      - session_timestamp (*sessionId*, ts)
      - 테이블 조인 필요

## 2. CTAS, CTE
  - SELECT를 통한 테이블 생성
    - 간단하게 새로운 테이블 생성
    - 자주 조인하는 테이블은 CTAS를 사용한 조인을 하면 편리
  - 데이터 품질 확인
    - 중복 레코드
    - 최근 데이터 존재
    - primary key uniqueness
    - 값이 없는 컬럼

## 3. 과제
  - 새로운 테이블
    - session_transaction (sessionId, refunded, amount)
    - channel (channelName)
  - 채널별 월 매출액 테이블 (본인 스키마 밑에 CTAS 사용)
    - session_timestamp, user_session_channel, session_transaction 사용
    - 필드
      - month
      - channel
      - uniqueUsers (전체 방문 사용자)
      - paidUsers (구매 사용자, refund 포함)
      - conversionRate(구매 사용자 / 전체 방문 사용자)
      - grossRevenue (refund 포함)
      - netRevenue (refund 제외)