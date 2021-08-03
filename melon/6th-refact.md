# [Melon] 6th - Re-Write

## tags_ids_convert -> tags_encoding
  - 기존
    - tag를 tag_set에 넣으면서 if문을 통해 중복 체크
    - _id 변수를 0부터 직접 1씩 더하면서 dict에 추가
  - 신규
    - tags 리스트를 set으로 변환했다가 list로 다시 변환하여 중복 제거
    - 정렬을 통해 비슷한 단어끼리 모이도록 변환
    - enumerate 사용으로 _id 변수 직접 계산 X

## train -> autoencoder_train
  - 중간점검 부분을 mid_check 메서드로 분리

## make_input4tokenizer
  - 토큰화 전처리 메서드

## get_tokens_from_sentences -> sentences_to_tokens
  - 문장들을 토큰화

  