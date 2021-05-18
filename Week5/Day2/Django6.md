# [Week5 - Day2] 6강 Form으로 Template에서 Model 수정하기

## 1. Form (폼)
  - forms&#46;py에 forms.ModelForm을 상속받는 클래스로 작성
  - 생성한 클래스의 내부 클래스로 Meta 클래스 생성
    - model : form을 만드는데 필요한 모델 클래스를 명시
    - fields : form에서 입력받을 필드 값을 명시
  - example
    ``` python
    class ItemForm(forms.ModelForm) :
        class Meta :
            model = Item
            fields = ('field1', 'field2', ...)
        pass
    ``` 

## 2. View에서 Template으로 데이터 전달
  - Process
    - views&#46;py
      1. views에 form 클래스를 import
      2. form 객체를 생성하여 render()의 파라미터로 전달
    - template (html)
      1. HTML \<form> 태그 안에 {{ form.as_\<type> }}를 전달
          - type 
            - table : 각 필드를 테이블 행으로 렌더링
            - ul : 각 필드를 리스트 아이템으로 렌더링
            - p : 각 필드를 단락별로 나누어 렌더링
      2. form에서 입력받은 데이터를 서버로 보낼 액션 생성
          - \<form> 태그에 method 추가 (POST)
          - `<button type="submit">` 태그로 버튼 생성
          - \<form> 태그에 {% csrf_token %} Template 태그 추가
          - CSRF Verification 미 처리시 403 Forbbiden 에러
    - views&#46;py
      1. POST 요청일 때 request를 바탕으로 form 완성
         - `form = ItemForm(request.POST)`
      2. form의 데이터들이 전부 유효한지 판단
          - `form.is_valid()`
      3. DB로 저장
          - `form.save()`
          - form 클래스에 모델을 명시해놨으므로 django에서 자동으로 처리

## 3. 정리
  - Form
    - 데이터를 입력받는 양식 클래스
    - 입력받을 데이터를 Form 클래스의 내부 클래스로 명시
  - View
    - Form 클래스 객체를 생성하여 Template으로 전달
  - Template
    - 템플릿 변수를 통해 화면을 구성
    - 입력받은 데이터를 DB로 전달하여 저장
