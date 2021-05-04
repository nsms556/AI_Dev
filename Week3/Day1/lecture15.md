# [3주차 - Day1] 15강 표본분포

## 1. 표본 조사
  - 통계적 추론
    - 표본 조사를 통해 모집단에 대한 해석 진행
    - 전수조사는 실질적으로 불가능
  - 반드시 오차 발생
    - 적절한 표본 추출 방법 필요
    - 표본과 모집단의 차이, 관계
    
## 2. 표본 분포
  - 표본 평균의 분포
  - 모수
    - 파악하려는 정보
    - 모평균, 모분산, 모비율 등
  - 통계량
    - 표본의 특성값
    - 표본 평균의 값도 확률 분포를 가짐
    - 통계량의 확률분포 : 표본 분포
    
  - 표본 평균
    - 정규모집단에서 추출된 표본의 측정값
      - *x*<sub>1</sub>, *x*<sub>2</sub>, ..., *x*<sub>n</sub>
    - 모평균을 알아내는데 쓰는 통계량
    - <img src="https://latex.codecogs.com/png.latex?\dpi{120}&space;\bg_white&space;\large&space;\bar{x}&space;=&space;\frac{1}{n}\sum_{n}^{i=1}x_{i}" title="\large \bar{x} = \frac{1}{n}\sum_{n}^{i=1}x_{i}" />
    - <img src="https://latex.codecogs.com/png.latex?\dpi{120}&space;\bg_white&space;\large&space;\bar{X}\sim&space;N(\bar{\mu},&space;\frac{\sigma^{2}}{n})" title="\large \bar{X}\sim N(\bar{\mu}, \frac{\sigma^{2}}{n})" />

## 3. 중심극한정리
  - 모집단에서 추출된 표본의 측정값
    - *x*<sub>1</sub>, *x*<sub>2</sub>, ..., *x*<sub>n</sub>
  - 표본 평균
    - n이 충분히 큰 경우 (n >= 30)
      - 근사적으로 <img src="https://latex.codecogs.com/png.latex?\dpi{120}&space;\bg_white&space;\large&space;\bar{X}\sim&space;N(\bar{\mu},&space;\frac{\sigma^{2}}{n})" title="\large \bar{X}\sim N(\bar{\mu}, \frac{\sigma^{2}}{n})" />
