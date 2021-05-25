# [Week5 - Day3] Week5 Mission log

## static
  - css 파일과 이미지 파일 사용을 위해 static 폴더를 사용

## CSS
  - index.html
    - 내부 스타일 시트 사용
  - game.html
    - 외부 스타일 시트 사용
    - /static/css/game.css

## game_view
  - views.py 파일에서 해당 메서드의 table_view의 값에 따라 DB를 Unordered List나 Table로 표시
  - 기본은 Table로 표시

## Game CRUD
  - 표에 폼 항목을 하나씩 넣어서 가로 테이블 형태의 폼 생성
  - POST 시 입력된 title과 platform을 복합 기본키 처럼 사용하여 DB 조회
    - 조회된 아이템이 있는 경우 JavaScript alert를 통해 에러 메세지 발생

  - <del>platform과 genre 항목을 select 태그로 변경</del>

  - request 요청에 JSON을 넣어서 보내는 경우와 form에서 입력하는 경우에 모두 대응

  - Django REST Framework를 통해 Update/Delete 구현