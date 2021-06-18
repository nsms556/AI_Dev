# [Week8 - Day4] Deep Learning 7 - Train

## 1. GPGPU 기술
  - CUDA
  - OpenCL

## 2. 딥러닝 프레임워크
  - Caffe2
  - PyTorch
  - TensorFlow

## 3. Computational Graph으로 비교하는 NumPy, PyTorch
  - Numpy
    - 가독성 ↑
    - 미분을 직접 계산 해줘야함
    - GPU 활용 X
  - PyTorch
    - 자동으로 미분을 계산
    - GPU 활용 가능

## 4. PyTorch
  - Tensor
    - NumPy Array와 유사하면서 GPU에서 계산 가능
    - NumPy 와 거의 동일하게 사용
  - Autograd
    - `requires_grad` : 미분을 자동으로 계산
    - `no_grad()` : 미분 추적 X
    - `Tensor.grad.zero_()` : 추적된 그래디언트 초기화
    - `torch.autograd.Function`을 상속 받는 클래스 정의를 통해 새로운 함수 생성
  - nn
    - 상위 레벨 Wrapper
    - 가중치를 직접 정의하지 않고 레이어를 쌓아서 모델을 정의
    - `model`을 통해 입력에 대한 예측, 손실함수 계산
    - `model.parameters()` : 가중치들을 리스트형태로 리턴
  - optim
    - `torch.optim`
    - `Adam, Adagrad` 등등 최적화 모델 존재
    - `Optimizer.step()` : 파라미터들을 직접 변경하지 않고 최적화 모델을 통해 진행
    - `Optimizer.zero_grad()` : 역전파할 때, 그래디언트가 초기화되지 않고 누적되므로 `zero_grad`를 통해 그래디언트 초기화
  - Dataloader
    - 데이터셋을 래핑하여 미니 배치의 크기, 셔플 여부, 멀티스레딩 활용 여부 등을 설정 가능
  - Pretrained Model
    - 직접 학습을 시켜 가중치를 얻는 대신 이미 학습된 모델들의 가중치를 받아서 사용 가능
  - 기타
    - visdom
      - 시각화 툴
      - 코드 로깅, 웹브라우저로 시각화 출력
    - tensorboardX
      - 웹 기반 시각화 툴

## 5. Dynamic Computation Graph VS Static Computation Graph
  - Dynamic Computation Graph
    - 연산을 진행하면서 모델 그래프를 적층
    - 1회 진행 후 그래프를 초기화하고 새로운 그래프 적층을 진행
  - Static Computation Graph
    - 연산을 하기전에 그래프를 먼저 쌓은 후 진행
    - 연산이 끝나도 그래프를 초기화하지 않음
    - TensorFlow v1에서 default로 사용
  - 최적화
    - Dynamic
      - 작성한대로 진행
    - Static
      - 단계를 합쳐서 진행 가능
  - 직렬화
    - Dynamic
      - 코드가 계속해서 필요
    - Static
      - 한번 그래프를 생성하면 이후에는 코드가 필요 없음

## 6. TensorFlow
  - v2 이전에는 Static Graph 사용
    - v2 이후 Dynamic Graph 사용
  - Optimizer
    - PyTorch와 유사하게 `tf.optimizers`에서 최적화 모델을 불러서 사용 가능
  - Loss
    - `tf.losses` 에서 미리 정의된 손실 함수 사용 가능
  - Keras
    - 서드 파티 패키지로 존재하다가 v2에서 통합
    - 쉽게 모델을 쌓을 수 있음
    - `model.compile(), model.fit()`을 통해 쉽게 학습 가능
  - `@tf.function`
    - 데코레이터를 통해 Static Graph 사용 가능
  - Pre-Trained Model 사용 가능
    - tf.keras
    - TF-Slim
  - TensorBoard
  - 분산 모델
    - 하나의 모델을 여러 머신에 나눠서 연산 처리 가능
  - TPU 사용 가능

## 7. Static PyTorch
  - Caffe2
  - ONNX
    - 한 프레임워크에서 진행된 모델을 다른 프레임워크에서 쉽게 사용하는 것을 목표로 하는 신경망 모델의 오픈소스 표준
    - 조건이나 반복이 없어야 Export 가능

## 8. PyTorch VS TensorFlow
  - PyTorch
    - 기본적으로 Dynamic Graph 사용
    - 쉬운 개발, 디버깅
    - ONNX를 통해 Export하여 모바일 등에서 사용가능
  - TensorFlow
    - v2 이전에는 Static Graph
    - v2 이후로는 Dynamic Graph 사용
      - 데코레이터를 통해 Static 사용 가능
    - 좀더 안정적인 환경
    - 큰 커뮤니티가 있어 자료를 찾기 쉬움
    - TPU 사용을 위해서는 반드시 선택해야함
  
