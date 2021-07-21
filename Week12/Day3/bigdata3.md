# [Week12 - Day3] Big Data 3 - SparkSQL

## 1. 커리어
  - 지난 이야기  
    - 남과 비교 금지
    - 하나를 파도 6개월은 파기
    - 일을 시작해보기
  - 점진적인 발전
    - 평생 직장이 존재하던 시절 -> 폭포수 커리어
    - 이제는 계속해서 발전해야 하는 시대
  - 새로운 시작 - 첫 90일이 중요
    - 자기검열 X, 매니저 스타일 파악, 피드백 요청
    - 과거 상처를 갖고 있지 말것
    - 남과 비교하지 않기
    - 열심히 하되 서두르지 말것
  - 기술의 습득이 아닌 기술을 통한 결과에 초점
    - 담당 업무를 잘하기 위한 기술을 습득
    - 맡은 일의 성공/실패를 어떻게 결정할지 생각
      - 매니저와 소통이 중요
    - 왜 일이 필요한지 그림을 그리면서 하기

## 2. [SQL 다시보기](https://github.com/nsms556/AI_Dev/blob/main/Week11/Day1/sql1.md#week11---day1-sql-1)
  - 구조화된 데이터를 다루는 한 SQL은 어디서든 사용
  - 관계형 DB
    - MySQL, PostgreSQL, Oracle, ...
    - Redshift, Snowflake, BigQuery, Hive, ...
  - 소개
    - Structured Query Language
    - 구조화된 데이터 질의 언어
  - 종류
    - DDL : 데이터 정의어
    - DML : 데이터 조작어
  - [자세히 보기](https://github.com/nsms556/AI_Dev/tree/main/Week11)

## 3. [SQL 실습 다시보기](https://github.com/nsms556/AI_Dev/blob/main/Week11/Day2/sql4.md#1-%EC%8B%A4%EC%8A%B5%EC%97%90-%EC%95%9E%EC%84%9C)
  - AWS Redshift + Google Colab
  - SELECT

## 4. SparkSQL
  - 소개
    - 구조화된 데이터 처리를 위한 Spark 모듈
    - 대화형 쉘 제공
    - Hive 쿼리를 변경없이 5배 이상 빠른 성능
      - 하둡의 데이터 기반 기준
    - 데이터프레임을 SQL로 처리 가능
      - RDD는 데이터프레임으로 변환후 처리 가능
      - 외부 데이터를 데이터프레임으로 변환 후 처리 가능
      - 데이터프레임은 특정함수를 통해 테이블이 되고 이후 SQL 함수 사용 가능
  - 사용
    - 외부 DB 연결
      - SparkSession 생성시 외부 DB에 맞는 JDBC jar 지정
      - `SparkSession.read()` 호출
        - 결과가 데이터프레임으로 리턴
    - SQL 사용
      - 데이터프레임을 기반으로 테이블 뷰 생성
        - `createOrReplaceTempView()` : 세션이 살아있으면 존재, 세션이 죽으면 같이 사라짐
        - `createGlobalTempView()` : Spark 드라이버가 살아있으면 존재, 세션이 죽든 말든 사라지지 않음
      - SparkSession의 sql 함수로 SQL 결과를 데이터프레임으로 받음

## 5. 실습
  - Redshift -> SparkSQL로 다시 하기
  