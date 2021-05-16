# [Week4 - Day5] 과제 메모

## Mission 1. My New Assistant
### Core
  - Swagger 적용을 위해 기존 flask에서 flask_restx 적용

### Extra
  - IP를 Location으로 변환하는 API 사용
    - 하루 호출량 제한이 매우 작아서 테스트에 매우 부적합

  - Google GeoLocation API
    - https://developers.google.com/maps/documentation/geolocation/overview
    - IP 대신 기지국, Wi-Fi AP 정보를 통한 Location 획득
    - HTTPS 프로토콜 위에서만 호출 가능
      - 현재 app은 http로 동작

  - HTTPS
  
  - 버스 정류장
    - https://www.data.go.kr/data/15000759/openapi.do
    - https://developers.google.com/maps/documentation/places/web-service/overview?hl=ko