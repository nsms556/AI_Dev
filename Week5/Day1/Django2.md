# [Week5 - Day1] 2강  View

## 1. App.views
  - App의 화면을 담당
    - HTML, CSS, JavaScript
  - 동작 확인을 위해 해야할 일
    - 프로젝트의 urls.py 파일에 경로를 추가 필요
    - 프로젝트의 settings.py 파일의 INSTALLED_APPS에 App 등록 필요

## 2. Admin
  - Django 관리자 페이지

  - 관리자 계정 설정
    - `python manage.py createsuperuser`
      - 이름, 이메일, 비밀번호
    - 프로젝트 생성시 같이 생성되는 admin DB 마이그레이션 필요
      - `python manage.py migrate`

  - 사용자 그룹, 권한 설정 가능