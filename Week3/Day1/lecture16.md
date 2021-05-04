# [3주차 - Day1] 16강 추정

## 1. 모평균의 추정
  - 모집단이 정규분포
    - 표본평균 사용
    - <img src="https://latex.codecogs.com/png.latex?\dpi{120}&space;\bg_white&space;\large&space;\bar{x}" title="\large \bar{x}" />는 모평균 <img src="https://latex.codecogs.com/png.latex?\dpi{120}&space;\bg_white&space;\large&space;\mu" title="\large \mu" />  추정에 사용

  - 점추정
    - 표본평균이 점 추정값(추정량)
  - 구간추정
    - 모평균 <img src="https://latex.codecogs.com/png.latex?\dpi{120}&space;\bg_white&space;\large&space;\mu" title="\large \mu" />의 100(1-a)% 신뢰구간
    - 정규분포에서 <img src="https://latex.codecogs.com/png.latex?\dpi{120}&space;\bg_white&space;\large&space;\sigma" title="\large \sigma" />를 알 때
      - ![image](image/1.png)
      - 실용적이지 못함
        - 정규분포가 아니거나, 표준편차가 알려져있지 않음
    - 표본의 크기가 클 때
      - 중심극한정리 사용
        - ![image](image/2.png)
        - s : 표본표준편차

## 2. 모비율의 추정
  - 점추정
    - 확률변수 *X*
      - n개의 표본에서 특정 속성을 갖는 표본의 개수
    - 모비율 *p*의 점 추정량
      - ![image](image/3.png)
  - 구간추정
    - n이 충분히 클 때
      - np > 5, n(1-p) > 5일 때
      - X~N(np, np(1-p))
    - 표준화
      - ![image](image/4.png)
      - 근사적으로 표준정규분포 N(0, 1)을 따름
    - 모비율 *p*의 100(1-a)% 신뢰구간
      - ![image](image/5.png)