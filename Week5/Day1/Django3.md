# [Week5 - Day1] 3강 Template

## 1. Template으로 화면 구성
  - HTML, CSS, JavaScript -> 정적 페이지
  - Django Template를 통해 동적 페이지 생성

  - `django.shortcuts.render(request, page, pageParams)`
    - request : 들어온 요청을 page로 전달
    - page : 페이지를 구성하는 파일
    - pageParams : request, page를 처리하는데 사용할 파라미터(dict)
      - {{parameters}}
        - pageParams의 데이터를 HTML에서 사용 가능
    - 함수의 return 값으로 전달해야 page 출력
    
  - HTML
    - HyperText Markup Language
    - 계층적 구조
    - \<head>와 \<body>로 구성
      - \<head> : html 파일의 메타 데이터
        - \<title> : 페이지의 제목
      - \<body> : 화면을 구성할 내용
    
    - 열린 태그와 닫힌 태그가 쌍으로 구성
      - 일부 태그는 단독 사용
    
    - DOCTYPE
      -  페이지의 HTML 버전이 무엇인지를 웹 브라우저에 알려주는 역할을 하는 선언문
      - HTML 태그 X

  - settings -> TEMPLATES
    - DIRS : 생성한 HTML 파일의 경로를 명시
  - 참고
    - Django는 프로젝트 폴더의 위치를 알 수 없음
      - BASE_DIR을 통해 폴더의 위치를 보관
      - os.path.join을 사용

## 2. Django Template
  - Template filter
    - Pipeline (|) 을 통해 적용
    - length
      - 파라미터의 길이를 리턴
      - EX) {{name | length}} : name 변수의 길이를 리턴
    - upper
      - 대문자로 출력
    - ':' 을 통해 Template filter에 파라미터 전달 가능

  - Template Tag
    - HTML에서는 프로그램 로직 사용 불가능
    - Django에서는 Template Tag를 사용하여 로직을 적용
    - {% \<tag> %} ... {% end\<tag> %}
      - for : endtag 필수
      - if : endtag 필수
        - if not
