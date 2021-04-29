# [2주차 - Day4] 11강, 12강 확률

## 1. 확률
  - 똑같은 실험을 무수히 많이 반복할때 사건이 일어나는 비율
    - 상대도수의 극한

  - 표본 공간
    - 모든 가능한 실험 결과의 집합

  - 사건
    - 관심있는 실험 결과의 집합

  - 사건의 확률
    - 사건의 원소의 수 / 표본공간의 원소의 수
    
  - P(A) : 사건 A가 일어날 확률

## 2. 확률의 계산
  - 조합(Combination)
    - 어떤 집합에서 순서에 관계없이 뽑은 원소의 집합
    - <sub>n</sub>C<sub>r</sub> : n개 중 r개를 뽑는 조합의 수
    - ![image](image/1.png)

  - 덧셈 법칙
    - ![image](image/2.png)

  - 서로 배반
    - 두 사건의 교집합이 공집합

  - 조건부 확률
    - 어떤 사건 a가 일어났을때 사건 B가 일어날 확률
    - ![image](image/3.png)
    - 곱셈 법칙
      - ![image](image/4.png)

  - 서로 독립
    - *P(B|A)* = *P(B)* 인 경우
    - ![image](image/5.png)

  - 여사건
    - 사건 A가 일어나지 않을 사건
    - A<sup>C</sup>
    - A와 A<sup>C</sup>는 서로 배반
      - P(A) = 1 - P(A<sup>C</sup>)

  - 분할 법칙
    - ![image](image/6.png)
    - ![image](image/7.png)
    - ![image](image/8.png)

  - 베이즈 정리
    - 사건 B<sub>1</sub>, B<sub>2</sub>, ..., B<sub>k</sub> 가 표본 공간 *S*의 분할
    - ![image](image/9.png)
    - ![image](image/10.png)
