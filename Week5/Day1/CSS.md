# [Week5 - Day1] 부록 CSS

## 1. CSS (Cascading Style Sheets)
  - 마크업 언어가 실제로 표시되는 방법을 기술하는 언어
    - 주로 HTML, XHTML에서 사용
  - 레이아웃과 스타일을 정의할 때의 자유도 높음

## 2. 문법
  - 수많은 영어 키워드를 통해 다양한 스타일의 속성 이름을 규정
  - 별개의 CSS 코드 파일이 필요없이 HTML에 CSS 키워드를 사용하는 것으로 적용가능

  - 선택자 (Selector)
    - 마크업 자체에 태그와 속성을 일치시킴으로써 어느 부분의 마크업에 스타일을 적용할지 선언
    - 클래스와 ID들은 대소문자를 구분하며 문자로 시작
      -  영숫자와 언더바(_)를 포함 가능
      - 클래스는 어떠한 요소의 어떠한 수의 인스턴스에도 적용 가능
      - ID는 하나의 요소에만 적용 가능

  - 선언 블록 (Declaration Block)
    - 괄호로 이루어진 선언들의 목록
    - 각 선언은 그 자체가 프로퍼티, 콜론( : ), 값으로 구성
    - 한 블록 안에 여러 선언이 있으면, 세미콜론 ( ; )이 개개의 각 선언에 삽입

  - 원천 (Sources)
    - 웹 브라우저, 사용자, 제작자 등등
    - 인라인, 미디어 타입, 중요성, 셀렉터 특정, 규칙 순서, 상속, 프로퍼티 정의로 분류
    - 사용되는 출력 장치에 따라 다른 스타일을 적용 가능
      
## 3. 메모
  - 내부 스타일 시트
    - ``` HTML
      <style> ...
        <HTML Tag name> : { property : value; property2 : value2; ... }
        ...
      </style>
      ```
  - 속성
    - color : 글자색
    - background-color : 글자 배경색
    - background-image : 배경 이미지
      - 값 : `url("example/image.png")`
    - opacity : 불투명도

  - 폰트
    - 구글 웹폰트
      - \<style>에 @import url 추가
      - css에 font-family를 통하여 적용
    - 로컬 서버 폰트
      - \<style>에 @font-face 추가
        - @font-face {font-family:폰트 이름; src:폰트 경로 format('truetype');}
      - css에 font-family를 통하여 적용
      