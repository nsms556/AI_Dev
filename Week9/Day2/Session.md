# [Week9 - Day2] Online Session

## 1. 7주차 실습 과제 - 음식 배달 시간 예측
  - *t<sub>i</sub>* : Target Label, *y<sub>i</sub>* : Prediction
    - Under Prediction
      - *t<sub>i</sub>* > *y<sub>i</sub>*
    - Over Prediction
      - *t<sub>i</sub>* < *y<sub>i</sub>*
  - Under Prediction 을 낮추면서 정확성을 높이는 손실함수
    - Under -> (t - y)<sup>2</sup>
    - Over -> 1/2 * (t- y)<sup>2</sup>
    - Under + Over
      - loss = 1/N * \Sigma( max(0, t-y)<sup>2</sup> + 1/2 * max(0, y-t)<sup>2</sup> )
      - max(0, t-y)<sup>2</sup> : t가 y보다 클 때 -> Under Prediction 손실 만족
      - 1/2 * max(0, y-t)<sup>2</sup> : y가 t보다 클 때 -> Over Prediction 손실 만족
        - 1/2 인 이유 : 경험적으로 2배 이상일때 만족도가 최악이 됨
        - coef 하이퍼파리미터 -> 최적화 과정에서 개선 가능

## 2. 커리어
  - 트랙
    - Individual Conributor (IC)
      - 리서치 사이언티스트, 리서치 엔지니어 -> VP -> CTO
    - Manager
      - 매니저 -> 디렉터 -> VP -> CEO
  - 취업
    - 과정
      - 온라인지원, 인맥(referral), 리크루터
      - 전화 인터뷰
      - on-site interview
      - offer
    - Resume
      - 부풀리지 말고 간결하게 핵심 위주로
    - 여러군데 지원시
      - 가장 원하는 곳의 면접을 먼저
      - 비슷한 시기에 오퍼가 온다면 협상에 도움됨<del>(저기는 이만큼 준다던데...)</del>
  - 면접
    - 면접관
      - Hiring Manager (인사팀장)
      - Recruiter (부서팀장)
      - Interviewer (그 외 고용된 면접 전문 담당자)
    - 면접준비
      - 회사, 팀, 인터뷰어에 대한 조사
        - 관련된 질문 다수
      - 기본 점검
        - 좋은 회사, 뛰어난 면접관일수록 기초에 관한 질문 ↑
      - 응용분야 지식보완
      - 프로그래밍 지식
    - 면접
      - 코딩테스트
        - 라이브 코딩
      - 머신러닝 지식
        - 최신 연구 < 기초
      - 시스템 디자인
        - 성공지표, 실험 설계 등
      - 경험 프로젝트
        - 당시 문제점, 본인 수행 역할, 기여
      - 회사문화, 팀문화 적응력
  - 오퍼 이후
    - 연봉협상
      - 시장 조사 필수
      - 회사에서 거절해도 원래 제시된 금액은 보장
      - 사이닝 보너스라도 노려보자
    - 오퍼 거절을 하더라도 인사팀과 좋은 관계를 유지할 것
      - 이직할 경우가 생긴다
  - 연봉
    - 사이닝 보너스
    - 인센티브
    - 스톡옵션

## 3. Q & A
  - 산업군, 도메인 관련된 지식은 어떻게 준비하고 어떻게 쌓을 수 있을까요?
    - 경험, 조사
  - AI 엔지니어로서 이직을 하게 될 때 도메인을 쉽게 바꿀 수 있을까요? 회사마다 도메인이 다르니, 이직이 쉽지 않을 것 같다는 생각이 드네요 ㅠ
    - 하나의 도메인에 올인하는 것도 좋지 않음
    - 장기적인 커리어를 위해서는 여러 도메인에 대한 경험이 필요
  - 대부분 해외에 거주를 하면서 해외취업을 하시나요? 한국에서 오퍼를 받고 나가는 경우도 있을까요? 해외취업에 대해서도 관심이 있는데 두려움이 더 많습니다
    - 해외 대학원이 가장 좋음
    - 사실 국내에서 해외로 나가는 비율은 매우 적음