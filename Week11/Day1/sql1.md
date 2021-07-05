# [Week11 - Day1] SQL 1

## 1. SQL의 중요성
  - 데이터 관련 3개 직군
    - 데이터 엔지니어
      - 파이썬, 자바/스칼라 
      - SQL(DB)
      - ELT/ETL
      - Spark, Hadoop
    - 데이터 분석가
      - SQL, 비즈니스 도메인 지식
      - 통계
    - 데이터 과학자
      - 머신러닝
      - SQL
      - 통계

## 2. 관계형 데이터베이스
  - 구조화된 데이터를 저장, 질의할 수 있도록 하는 스토리지
    - 스프레드시트 형태의 테이블로 데이터를 정의, 저장
      - 컬럼과 레코드가 존재
  - SQL : 관계형 DB를 조작하는 언어
    - 테이블 정의를 위한 DDL
    - 테이블의 데이터 조작/질의을 위한 DML

### 2-1 대표
  - 프로덕션 DB
    - MySQL, PostgreSQL, Oracle
    - OnLine Transaction Processing (OLTP)
    - 빠른 속동 집중, 서비스에 필요한 정보 저장
  - 데이터 웨어하우스
    - Redshift, Snowflake, Bigquery, Hive
    - OnLine Analytical Processing (OLAP)
    - 처리 데이터의 크기에 집중, 데이터 분석, 모델 빌딩 등을 위한 데이터 저장
      - 보통 프로덕션 DB를 복사하여 웨어하우스에 저장

### 2-2 구조
  - 2단계로 구성
    - 최하위에는 테이블들이 존재
    - 테이블들은 DB 혹은 Schema 라는 폴더 밑으로 구성
  - 테이블의 구조
    - 테이블은 레코드들로 구성 (행, row)
    - 레코드는 하나 이상의 필드로 구성 (열, column)
    - 필드는 이름과 타입과 속성(primary key)으로 구성

## 3. SQL
  - Structured Query Language
  - 70년대 IBM 개발
  - 두 종류로 구성
    - DDL
    - DML
  - 구조화된 데이터를 다루는 한 SQL은 데이터 규모와 상관없이 사용
    - Spark, Hadoop, 웨어하우스 등등
  - 단점
    - 구조화된 데이터에 최적화
      - 비구조화된 데이터에는 제약이 심함
      - 많은 관계형 DB 들이 플랫형 구조만 지원
      - 비구조화된 데이터 -> Spark, Hadoop 등 분산 컴퓨팅 환경 필요
    - 관계형 DB 마다 SQL 문법이 상이
  - Star Schema
    - 데이터를 논리적 단위로 나눠 저장, 필요시 조인
    - 스토리지 낭비를 줄이고 업데이트 용이
  - Denormalized Schema
    - 데이터 웨어하우스에서 사용
      - 단위 테이블로 나눠서 저장 X -> 별도의 조인 필요 X
    - 스토리지 사용 증가
    - 조인 X -> 빠른 계산
    