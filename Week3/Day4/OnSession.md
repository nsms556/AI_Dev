# 인공지능 기술 동향

## 인공지능
  - 머신러닝
    - 엔지니어가 값을 선정해 모델에 입력하면 그 값을 바탕으로 학습을 진행
  - 딥러닝
    - 머신러닝이 더 발전하여 엔지니어 없이 자체적으로 학습

## 머신러닝
  - 지도학습(Supervised Learning)
    - 분류, 회귀
  - 비지도학습(Unsupervised Learning)
    - 군집분석, 차원축소
  - 강화학습(Reinforcement Learning)
    - 에이전트의 액션에 대해 점수를 매기고 점수를 높게 획득하는 에이전트를 찾아내는 방향

## 인공지능 분야
  - Computer Vision : 시각적 세계를 해석하고 이해하도록 컴퓨터를 학습
    - Image Classification : 이미지 분류
    - Object Detection : 물체 검출
    - Semantic Segmentation : 동일한 객체 클래스에 속하는 이미지의 일부를 함께 클러스터링
      - 분류 : 이미지에 물체가 하나
      - 검출 : 이미지에 있는 모든 물체를 탐색
      - Segmentation : 이미지에 있는 객체들에 대해 해당 영역을 클러스터링
        - EX) MRI
    - Image Generation : 이미지를 원하는 목표에 맞게 생성
      - 지폐위조 VS 금감원
      - GAN -> styleGAN
    - Pose Estimation : 사람의 행동을 검출
      - 모션 캡쳐
      - 행동 인식
      - AR
    - 기타
      - Domain Adaptation
      - Domain Generalization
        - 현재 CV의 단점인 학습되지 않은 데이터들에도 적용할 수 있도록 적응, 일반화
      - Super-Resolution
        - DLSS

  - Natural Language Process (자연어 처리) : 인간의 언어 현상을 기계가 묘사할 수 있도록 연구, 구현  
    - 세부 분야
      - 감정 분석
        - 입력 텍스트의 감정 분류
        - 기업에서 리뷰 분석에 주로 활용
          - 관련 데이터 다수 공개
      - 기계 번역
      - 질의 응답
        - 챗봇
    - 주요 모델
      - ELMo
      - BERT
        - 양방향 인코더
      - GPT (Generative Pretrained Transformer)
        - 디코더
        - 생성에 관련

  - Time Series (시계열 분석) : 시계열을 해석하고 이해하는 데 쓰이는 다양한 방법을 연구
      - 주식 시장 예측
      - Human Activity Recognition : 센서, 비디오를 활용하여 사람의 행동 인식
        - 애플워치 운동 인식
      - Anomaly Detection, Change Point Detection : 이상 감지, 변화 지점 감지
      - Spatio-temporal forecasting : 시공간적 데이터를 분석하여 예측
        - 교통 예측, 날씨 예측
        - 비디오 영상에서 주로 사용
        - 카카오택시 등

  - Recommendation System (추천 시스템) : 사용자를 위한 추천 목록 생성
    - 기업에서 소비자를 대상으로 상품을 추천하기 위해 사용
      - 넷플릭스, 아마존, 유고리즘 등
  
  - Speech/Audio
    - Dialog Generation/Voice Conversation
      - 시리, 알렉사, 빅스비 등 가상 비서의 기본 요소
      - 강화학습, GPT 등을 통해 응답 생성
    - Audio Classification/Speech Recognition
      - 음성을 인식한 후 텍스트로 변경
      - 인공지능 스피커(기가지니, 헤이카카오)
    - Emotion Recognition
      - 음성신호로부터 감정을 평가
      - 콜센터 등에서 고객의 감정을 감지
    - Music/Audio Generation
      - 원시 오디오를 생성
      - OpenAI Jukebox
      - 가수나 작곡가의 특성을 반영, 화자의 특성을 반영하여 생성 가능