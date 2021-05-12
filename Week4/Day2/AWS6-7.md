# [Week4 - Day2] 6-7강 AWS를 활용한 인공지능 모델 배포 6-7

## Flask 기반 감성분석 API 개발

### 네이버 영화리뷰 감성분석 개요
  - 네이버 영화리뷰 데이터로 학습한 ML/DL 모델 활용
    - Naive-Bayes 모델, 딥러닝 모델로 학습한 두개의 모델을 서빙하여 0은 부정, 1은 긍정

### 감성분석 API 개발 방향
  - AWS EC2와 Python Flask 기반 모델 학습 및 추론을 요청/응답하는 API 서버 개발

### API 정의
  - key:value 형태의 json 포맷으로 요청
  - text index 별로 key:value로 결과를 저장한 json 포맷으로 결과 반환
    - POST 방식으로 predict 요청
    - do_fast
      - True : 속도가 빠른 Naive-Bayes 모델
      - False : 속도는 느리지만 정확성이 높은 딥러닝 모델

### 딥러닝 모델 핸들러 추가
  - 사전 학습한 딥러닝 모델을 활용하여 머신러닝 모델 핸들러와 동일한 입력에 대해 동일한 결과를 반환하는 핸들러 개발

  - 사전 학습 모델은 Hugging Face에서 제공하는 외부 저장소에서 다운로드

### unittest model handlers
  - 개발한 핸들러가 원했던 대로 동작하는지에 대한 테스트 진행

### Flask API 개발 & 배포
  - 모델을 전역변수로 불러오고 요청된 텍스트에 대해 예측 결과를 반환

### Test API on Remote
  - 원격에서 서버로 API에 요청하여 테스트 수행

  - host : 퍼블릭 IP or 할당한 탄력적 IP
  - port : 미리 설정한 추가 포트 번호 (5000)
  
### ML 모델 학습 요청 API
  - http://host:port/train 으로 모델 학습을 요청
