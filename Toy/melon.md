# [Toy] Log

## 1. most_popular
  - train 파일에서 가장 많이 나온 노래 200 곡 리스트 생성
  - train 파일에서 가장 많이 나온 태그 100개 리스트 생성
  - question 파일을 읽어서 list(dict) 형태로 저장
  - 위의 리스트에서 순서대로 아이템으로 하나씩 불러서
    - 200곡 리스트의 곡중 아이템의 곡 리스트에 없는 노래들만 모아서 100개에서 컷 -> song
    - 100개 태그 리스트 중 아이템의 태그 리스트에 없는 태그들만 모아서 10개에서 컷 -> tag
    - 답안 리스트에 아이템의 id, song, tag를 딕셔너리 형태로 추가
  - 답안 리스트를 json으로 출력

## 2. genre_most_popular
  - song_meta.json을 읽어서 각 곡에다가 id를 부여
  - train 파일에서 가장 많이 나온 노래 200 곡 리스트 생성 (song_mp_counter)
  - train 파일에서 가장 많이 나온 태그 100개 리스트 생성 (tag_mp_counter)
  - 장르별로 플레이리스트에 많이 담긴 200곡으로 분리 (song_mp_per_genre)
    - song_meta의 모든 노래를 장르별로 분리한 하나의 dict 형태로 생성
    - 각 장르별로
      - 해당 장르의 곡 id 리스트에 들어있는 id를 순서대로
        - 200곡 리스트에서 해당 id 곡이 나온 횟수를 value로
        - 곡 id를 key로 하는 dict를 생성
        - dict를 Counter로 변경 후 플레이리스트에 많이 담긴 순서대로 최대 200곡 리스트로 변경
