# [Week4 - Day2] 3강 AWS를 활용한 인공지능 모델 배포 3

## API to serve ML model
  - 목표
    - AWS EC2와 Python Flask 기반 모델 학습 및 추론 요청/응답하는 API 서버

## 인터페이스
  - 사용자는 기계와 SW를 제어하기 위해 인터페이스를 정해진 매뉴얼에 따라 활용하여 원하는 경험 획득
  - 상호 합의된 매뉴얼에 따라 적절한 입력을 받아 기대되는 출력을 제공

  - API (Application Programming Interface)
    - 노드와 노드 간 데이터를 주고 받기 위한 인터페이스
    - 사전에 정해진 정의에 따라 입력을 받고 적절한 출력을 전달

  - RESTful API for ML/DL model inference
    - REST 아키텍쳐를 따르는 API
    - HTTP URI를 통해 자원을 명시하고 HTTP Method를 통해 필요한 연산을 요청하고 반환
    - RESTful API
      - 데이터의 교환/요청 등을 위한 인터페이스를 REST 아키텍처를 따라 구현
    - 일반적으로 데이터 값을 담아 요청, 모델이 추론한 결과를 json 형태로 리턴하도록 설계
    - 요청 메시지만 봐도 어떤 내용으로 되어있는지 알 수 있도록 표현

## Model Serving
  - 학습된 모델을 REST API 방식으로 배포하기 위해 학습된 모델의 Serialization과 웹 프레임워크를 통한 준비 필요
  - serving할 때 학습 시의 데이터 분포나 처리방법의 연속성 유지 필요
  - 배포 환경에 따라 다양한 프레임워크를 고려하여 활용

## Serialization & De-serialization
  - 모델의 재사용 및 배포를 위해 세이브 & 로드
  - Serialization
    - 모델 객체를 디스크에 저장하여 어디든 전송하고 불러올 수 있는 형태로 변환
  - De-serialization
    - 모델을 불러와 추론/학습에 사용
  - 배포 환경을 고려하여 올바른 방법으로 Serialization을 해야 De-Serialization 가능

## 다양한 프레임워크
  - TensorFlow Serving, TorchServe, TensorRT
  - Flask 같은 웹 프레임워크는 클라이언트로부터의 요청을 처리하기 위해 주로 사용
  - 모델 추론을 위한 AP 서버를 운용하여 내•외부 통신을 통해 예측/추론 값 리턴
  - 대용량 데이터 배치처리, 딥러닝 모델의 활용이 늘면서 멀티 노드, 멀티 GPU환경에서의 안정적인 모델 서빙