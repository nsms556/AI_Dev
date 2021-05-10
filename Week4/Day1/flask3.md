# [Week4 - Day1] 3강 REST API

## API?
  - Application Programming Interface
  - 프로그램들이 서로 상호작용하는 것을 도와주는 매개체

## REST?
  - REpresentational State Transfer
  - 웹 서버가 요청을 응답하는 방법론 중 하나
  - 데이터가 아닌 자원(Resource)의 관점으로 접근

## REST API
  - HTTP **URI**를 통해 자원을 명시
    - ※ URL과 URI
      - URI : 인터넷에 있는 자원을 나타내는 유일한 주소
      - URL : 네트워크 상에서 자원이 어디 있는지를 알려주기 위한 규약
        - 그 주소에 접속하려면 해당 URL에 맞는 프로토콜을 알아야 하고, 그와 동일한 프로토콜로 접속해야 한다.
        - URL = 프로토콜 + URI
  - HTTP Method를 통해 해당 자원에 대한 CRUD를 진행
    - GET, POST, PUT, DELETE -> /order
  - Stateless (無상태성)
    - 클라이언트의 컨텍스트를 서버에서 유지 X
    - 서버는 아이템을 GET하기 위해 POST를 진행할 필요 X
      - POST /shoes -> 자원에 새로운 정보를 생성
      - GET /shoes -> DB에 shoes가 있는지 확인 후 해당 자원 반환  

## POSTMAN
  - API 테스트

## 실습
  - `@app.route(URI, method=[HTTP Method])`
    - GET은 보통 생략
    - 그 외의 경우 반드시 명시해야 함

  - `request.get_json()`
    - 들어오는 자료가 json으로 가정
    - json 형태의 데이터를 dict 타입으로 변환