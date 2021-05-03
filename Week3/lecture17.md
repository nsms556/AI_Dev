# [3주차 - Day1] 17강 검정

## 1.  통계적 가설검정
  - 가설 검정
    - 주장을 검증하는 것
    - 표본평균 bar(X)가 mu<sub>0</sub>보다 얼마나 커야 모평균 mu가 mu<sub>0</sub>보다 크다고 할 수 있는가
      - 표본의 선택에 따라 표본평균이 달라짐

    - 귀무가설 ![image](image/6.png)
    - 대립가설 ![image](image/7.png)
    - 귀무가설의 기긱을 위해서는 bar(X)가 큰 값이 필요
      - 귀무가설이 참으로 가정할 때 랜덤 선택한 표본에서 지금의 bar(X)가 나올 확률
      - 낮으면 귀무가설이 참이 아니라고 판단
    - 확률이 낮다 -> 기준 필요
      - 유의 수준 <img src="https://latex.codecogs.com/png.latex?\dpi{120}&space;\bg_white&space;\large&space;\alpha" title="\large \alpha" />
    - P(bar(X) >= k) <= <img src="https://latex.codecogs.com/png.latex?\dpi{120}&space;\bg_white&space;\large&space;\alpha" title="\large \alpha" />가 되는 k
    - 표준정규확률변수로 변환 -> 검정통계량
      - ![image](image/8.png)

    - 검정
      - H<sub>0</sub>, H<sub>1</sub> 설정
      - 유의수준 <img src="https://latex.codecogs.com/png.latex?\dpi{120}&space;\bg_white&space;\large&space;\alpha" title="\large \alpha" /> 설정
      - 검정통계량 계산
      - 기각역, 임계값 계산
      - 유의성 판정

## 2. 모평균의 검정
  - 대립가설
    - 대립가설 채택을 위한 통계적 증거 확보 필요
    - 증거가 없으면 귀무가설 채택
  - 검정통계량
    - n >= 30인 경우
      - 중심극한정리
      - ![image](image/8.png)
    - 정규모집단, 모표준편차가 있는 경우
      - ![image](image/9.png)
    - 기타
      - p분포 등 기타 

  - 기각역
    - H<sub>0</sub> : μ = 10.5
    - 유의수준 : α
    - H<sub>1</sub> : μ > 10.5 -> Z > z<sub>α</sub>
    - H<sub>1</sub> : μ < 10.5 -> Z < z<sub>α</sub>
    - H<sub>1</sub> : μ >< 10.5 -> |Z| > z<sub>α/2</sub>