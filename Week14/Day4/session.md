# [Week14 - Day4] Online Session
  - 이석호 강사님
  - Computer Vision

## 1. 실습관련
  - OpenCV Face Detection
  - 주말 실습
    - 폐렴 영상 전이학습
      - 데이터 400~500개 이상
    - Pix2Pix, Cycle GAN을 다른 데이터셋으로 학습
      - CycleGAN maps, summer2winter
    - 잘되면 전이학습 추가해보기

## 2. 강의내용 리뷰 + 질문
  - Anchor box
    - 학습이 좀 더 쉽게 될 수 있는 곳에서 객체 탐색을 시작
  - 사진에서 박스를 만들게 되는 과정에서 타겟 구획이 오브젝트일 가능성이 높을때 앵커박스들을 만든다고 들었는데 배경과 오브젝트를 구분하는 원리가 궁금합니다. 주변과 비교해 튄다던지... 뒷배경이 조금 튀는경우는 배경도 오브젝트로 인식을 할지...
    - 오브젝트 같은 것에 앵커박스 적용 X
    - 모든 곳에 앵커박스를 써서 오브젝트 같은 것을 선별
  - anchor box 설명 중에서 노란 박스 60%넘으면 objectness 벡터가 객체가 존재함을 표시하는데, 만약 그 바로 옆에 노란박스도 60% 넘으면 어떤 좌표로 저장되나요?? 가장 정확도가 높은 x,y좌표로 저장되나요??
    - 둘 다 오브젝트를 찾은것으로 판별
    - 이후에 Non-Max Supression으로 하나만 선별
  - IoU Threshold 보편적인 값
    - 0.6 or 0.7
  - 미세조정 단계에서 IoU Threshold 변경?
    - 필요하면 해야함
  - 제가 아직 오늘 강의를 중간 밖에 못봐서 그런데 Faster RCNN을 배우면 그전의 RCNN, Fast RCNN을 이해하기 쉽나요??
    - RCNN -> Region Proposal 사용
    - Fast RCNN -> Network
  - 지금 object detection이 어느 정도의 성능을 가지고 있는지 실제로 어떤 모델들이 자주 쓰이는지 궁금합니다.
    - 현재는 YOLO
    - 과거엔 속도 우선, 정확도 우선 여부에 따라 달랐음
      - 속도는 YOLO
      - 정확도는 여러 모델
  - 격자 사이즈가 다른 이유
    - Pooling Layer의 차이
  - Deep Neural Network
  - AI 기만 공격
  - 얼마전에 cutmix, mixup 등의 image classification에서의 image augmentation 기법들을 배웠었는데, image recognition이나 segmentation 기법에서는 효율적인 augmentation기법들이 있는지 궁금합니다.
    - GAN을 썼었는데 도움이 안됨
  
## 3. 추가내용


## 4. 현장 썰
  - AI 인사이트 최영균 과장님
  - 학업은 모델 위주의 과업
    - 데이터를 보고 모델을 설계
  - 현장은 모델 보단 데이터 위주의 과업
    - 이미 만들어진 모델을 보고 데이터를 모델에 맞게 변환
  - 의료계 반발
    - 병원 연계가 가장 힘듬
    - 힘든 것 중에서 병원이 50퍼, 서류가 10퍼 정도
  - 전처리, Augmentation
    - 수집할 때 전처리가 된 이미지로 수집 -> 의사들이 이미 전처리가 된 이미지를 보고 진단
  - 좋은 데이터의 영향 <<<<< 불량 데이터의 영향
    - 클리닝이 매우 중요
  - 수익 모델
    - 웹페이지에 이미지를 업로드하면 구분해주는 모델
    - 의료 기기로 병원에 납품