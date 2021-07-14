# [Toy] 4th Repository
  - https://github.com/powerzist/kakao-arena-3rd
  - khaiii : 카카오 한글 분석기 v3

## 1. 메서드
  - ```combine_tags(df : pd.DataFrame) -> str```
    - df의 각 tags Column(List[str])을 합쳐서 하나의 스트링으로 생성
  - ```re_sub(series : pd.Series) -> pd.Series```
    - _, ㅋ, 특수문자, 공백, u+3000(표의 공간) 제거
  - ```flatten(list : List) -> List```
    - (m, n) 이중 리스트를 (m*n, 1) 형태 리스트로 변경
  - ```get_token(title : str, tokenizer : khaiiiApi) -> List[Tuple]```
    - title이 없거나 공백 -> 빈 리스트 출력
    - title을 형태소로 분리 (result)
    - result의 각 아이템들을 (형태소, 형태소의 태그) 형태로 변환하여 리턴
  - ```get_all_tags(df : pd.DataFrame) -> List```
    - df의 전체 tags Column을 전부 모아서 하나의 리스트로 생성

## 2. tags_and_title_tokenize
  1. json 파일을 DataFrame으로 변환
      - [tags, id, plylst_title, songs, like_cnt, updt_date]
  2. DataFrame에 combine_tags를 적용하여 comb_tags Column을 생성
      - DataFrame의 각 행별로 태그들을 합친 스트링을 만들어 comb_tags Column으로 저장
  3. DataFrame의 plylst_title Column에 fillna 적용
      - 각 행에서 플레이리스트 제목이 없는 경우를 빈 스트링으로 변환
  4. DataFrame의 plylst_title Column에 re_sub을 적용
      - 플레이리스트 제목에서 _, ㅋ, 특수문자, 공백, u+3000(표의 공간) 제거
  5. DataFrame의 plylst_title Column에 get_token을 적용하여 ply_token Column을 생성
      - 플레이리스트 제목을 형태소 분리하여 (형태소, 태그) 리스트로 변환, ply_token Column에 저장
  6. DataFrame의 comb_tags Column에 re_sub을 적용
      - 각 행마다 태그들을 하나로 합친 스트링에서 _, ㅋ, 특수문자, 공백, u+3000(표의 공간) 제거
  7. DataFrame의 comb_tags Column에 get_token을 적용하여 tag_token Column을 생성
      - 태그 스트링을 형태소 분리하여 (형태소, 태그) 리스트로 변환, tag_token Column에 저장
  8. DataFrame 각 행의 ply_token, tag_token에서 using_pos에 들어있는 태그를 가진 형태소들만 추출
      - using_pos = ['NNG','SL','NNP','MAG','SN', 'NP', 'VA', 'VV', 'XR']
      - 일반 명사(NNG), 대명사(NP), 외국어(SL), 고유 명사(NNP), 일반 부사(MAG), 숫자(SN) 태그만 추출
  9. DataFrame 각 행의 ply_token, tag_token에서 태그를 버리고 형태소들만 추출하여 각각 title_token, tags_token Column으로 저장
  10. DataFrame에서 ply_token, tag_token, comb_tags Column을 Drop
  11. DataFrame을 json으로 출력

## 3. inference
  1. song_meta.json을 읽어서 meta(pd.DataFrame)으로 변환 후 사용하지 않을 컬럼들을 드랍
      - album_id, album_name, artist_id_basket, artist_name_basket, song_name
  2. genre_gn_all.json을 읽어서 genre(pd.DataFrame)으로 변환
      - reset_index()를 사용하여 DataFrame index를 gnr_code 컬럼으로 변경
      - 장르 이름이 담긴 컬럼의 타이틀을 gnr_name으로 변경
  3. genre의 gnr_code 컬럼을 통해 대분류와 소분류로 나눠서 저장
      - gnr_code의 뒷2자리가 00인 경우를 모아서 gnr_big_code로 저장
        - GN9000의 경우 따로 추가
      - gnr_code의 뒷2자리가 00이 아닌 경우를 모아서 gnr_small_code로 저장
      - 추출 후 각각을 리스트로 변경
  4. gnr_big_code와 gnr_small_code를 사용하여 r_big_dict, r_small_dict를 생성
      - r_big_dict[gnr_big_code[i]] = i
      - r_small_dict[gnr_small_code[i]] = i
      - 장르 코드를 Key, 대응되는 라벨(i)을 value로 사용하는 딕셔너리 생성
  5. train과 val json 파일을 읽어서 각각 DataFrame으로 변환
      - tags_and_title_tokenize를 통해 토큰이 분리된 json 파일을 사용
  6. meta의 각 행마다
      - 곡의 id를 idx로 저장
      - 딕셔너리 big_dict, small_dict에 idx를 Key, 대분류와 소분류의 라벨 리스트를 value로 추가
  7. L50