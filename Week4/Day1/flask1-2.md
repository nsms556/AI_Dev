# [4주차 - Day1] 1-2강 Flask 시작하기

## Flask란?
  - 파이썬 기반 마이크로 웹 프레임워크
  - 설치
    - pip install flask
    - conda install flask

## 참고. 파이썬 가상환경
  - virtualenv 모듈
  - 가상환경 생성
    - `virtualenv <가상환경 이름>`
  - 가상환경 실행
    - Mac/Linux
      - `source <가상환경 이름>/bin/activate`
    - Windows
      - `<가상환경이름>\Scripts\activate.bat`

## Flask app 기본 구조
  - from flask import Flask
  - app
    - app.route()
  - `__main__`

# 2강 인터넷과 웹

## Web?
  - 인터넷에 연결된 사용자들이 정보를 공유할 수 있는 공간

## 웹 사용
  - Chrome, Edge, Safari, Firefox, Opera 등등
  - URL

## 웹의 동작방식
  - 클라이언트와 서버간의 소통
  1. 클라이언트가 서버에게 정보 요청을 전송
  2. 서버는 요청에 대한 처리를 진행
  3. 서버가 클라이언트의 요청에 대해 응답을 전송