# [Week5 - Day1] 1강 django 알아보기

## 1. Django
  - 파이썬 기반 웹 프레임워크
  - Django VS Flask
    - Django : 풀스택 프레임워크
      - 프로젝트 내 여러 Application 존재 가능
      - DB 접근을 위한 자체 ORM
    - Flask : 마이크로 프레임워크
      - 프로젝트 내 하나의 Application을 사용
      - 유연하고 편한 확장성

## 2. Django 기초
  - 설치
    - pip install django

  - 프로젝트
    - 생성 : `django-admin startproject <프로젝트 이름>`
    - 시작 : `python manage.py runserver`

  - Django 프로젝트 구성요소
    - manage&#46;py
      - Django 실행
    - <플젝 이름 폴더>
      - \_\_init__&#46;py
        - 해당 디렉토리가 모듈로 인식하도록 동작
      - asgi&#46;py, wsgi&#46;py
        - 서버가 django 실행에 사용
      - settings&#46;py
        - 프로젝트의 설정
          - SECRET_KEY
          - DEBUG
          - ALLOWED_HOSTS
          - INSTALLED_APPS
          - MIDDLEWARE
          - ROOT_URLCONF
          - TEMPLATES
          - WSGI_APPICATION
          - DATABASES
          - AUTH_PASSWORD_VALIDATORS
          - LANGUAGE_CODE, TIME_ZONE, ...
          - STATIC_URL
      - urls&#46;py
        - url 관리
        - urlpatterns

## 3. Django APP
  - 하나의 django 프로젝트는 여러 개의 App으로 구성

  - App 생성
    - `django-admin startapp <App 이름>`

  - 구성요소
    - \_\_init__&#46;py
    - admin&#46;py
      - App의 관리자 페이지
    - apps&#46;py
      - App의 설정
    - models&#46;py
      - App 내에서 사용할 DB의 Schema 등을 클래스 형태로 관리
    - test&#46;py
      - App의 테스트 케이스 관리
    - views&#46;py
      - App의 뷰를 관리

## 4. Django MVT Pattern
  - Model, View, Template
    - 참고 - MVC Pattern : Model, View, Control

  - Model
    - DB 접근을 위한 ORM 등
  - View
    - App들의 views&#46;py
  - Template
    - .html 등의 페이지 템플릿
    - django temaplate 언어를 통해 html 파일 내에서 다른 모델 객체 접근