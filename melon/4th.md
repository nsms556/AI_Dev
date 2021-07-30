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
      - 장르 코드를 Key, 대응되는 숫자 라벨(i)을 value로 사용하는 딕셔너리 생성
  5. train과 val json 파일을 읽어서 각각 DataFrame으로 변환
      - tags_and_title_tokenize를 통해 토큰이 분리된 json 파일을 사용
  6. meta의 각 행마다
      - 곡의 id를 idx로 저장
      - 딕셔너리 big_dict, small_dict에 idx를 Key, 대분류와 소분류의 라벨 리스트를 value로 추가
  7. train, val (df) 각 행마다
      - 플레이리스트를 tracks로 저장
      - tracks에 있는 곡들의 id를 사용하여 리스트 df_big, df_small에 곡의 대분류, 소분류 라벨을 추가
  8. df_big, df_small 들을 각 DataFrame의 big, small 컬럼으로 추가
  9. train, val에서 각각 title_token, tags_token 컬럼을 or 연산을 통해 token 컬럼으로 생성
      - combine_tokens(df : pd.DataFrame) -> List
  10. train, val의 updt_date 컬럼을 통해 month 컬럼과 yyyymmdd 컬럼을 생성
      - convert_to_month
      - convert_to_yyyymmdd
      - 이후 updt_date 컬럼은 drop
  11. all_tags, all_tokens Set에 train과 val의 tags, tokens 컬럼을 추가
      - all_tags, all_tokens를 리스트로 변환한후 정렬
  12. all_tags, all_tokens를 통해 tags_dict, tokens_dict 딕셔너리를 생성
      - 각각 태그, 토큰을 Key, 대응되는 숫자 라벨(i)을 value로 사용
      - r_tags_dict, r_tokens_dict에는 태그, 토큰을 value, 숫자 라벨을 Key로 사용
  13. train,val (df)을 통해 df_length_s, df_cols_s, df_length_t, df_cols_t를 생성
      - train_cols_s 기준
      - train의 행을 순서대로
        - songs(플레이리스트)를 extend로 추가
        - tags(태그 리스트)를 tags_dict 사용해 라벨 리스트로 변환, 전체 곡의 개수(tracks_len)를 각 라벨에 더한 후 extend로 추가
        - tokens(토큰 리스트)를 tokens_dict 사용해 라벨 리스트로 변환, 전체 곡의 개수 + 전체 태그의 개수를 각 라벨에 더한 후 extend로 추가
        - big (대분류 라벨 리스트)에 전체 곡 수 + 전체 태그 수 + 전체 토큰 수를 더해 extend로 추가
      - 플레이리스트, 태그 리스트, 토큰 리스트, 대분류 리스트 각각의 길이를 전부 더해서 train_length_s에 append
      - 끝이 t로 끝나는 경우는 big(대분류) 대신 small(소분류) 사용
      - 왜 더하는지는 이유?
  14. df_length_s, df_cols_s, df_length_t, df_cols_t 들을 사용하여 df_spas_s, df_spas_t 생성
      - 1을 df_length_s의 길이만큼 갖는 리스트 values 생성
      - df_length_s 길이 + 1만큼 반복
        - df_length_s[:i]의 합을 rows_idx 리스트에 append
      - (values, train_cols_s, rows_idx)의 압축 희소 열 행렬(CSR Matrix) 생성하여 df_spas_s로 저장
        - shape = (df.shape[0], 전체 곡 수+전체 태그수+전체 토큰 수+대분류 수)
      - df_spas_t는 df_length_s, df_cols_s 대신 df_length_t, df_cols_t 사용
  15. train_spas_s에서 열을 tracks_len만큼 잘라내서 train_spas_s_s 로 저장
      - train_spas_t에서 열이 tracks_len ~ tracks_len+tags_len+tokens_len 인 부분만 슬라이싱하여 train_spas_t_t로 저장
  16. f_s, B2_s, fb_s, f_t, B2_t, fb_t, f_s_s, B2_s_s, fb_s_s, f_t_t, B2_t_t, fb_t_t 계산
      - f_s, B2_s, fb_s 기준
      - f_s
        - train_spas_s의 행 들을 더한 후 1을 빼고 f_s로 저장
        - 0.4 거듭제곱 후 1을 더해서 저장
        - 역수로 전환
        - nan 값을 0 으로 변환
      - B2_s
        - train_spas_s의 열 들을 더한 후 제곱근을 취해서 저장
      - fb_s
        - train_spas_s 와 f_s 를 스칼라 곱(multiply)하여 저장
      - _t는 train_spas_t 사용
      - _s_s 는 train_spas_s_s 사용
      - _t_t 는 train_spas_t_t 사용
  17. KNN
      - month 컬럼 거리 계산
      - like_cnt 컬럼 거리 계산
      - dist = 1 / ((month_dist + like_dist + 1) * 350)
      - diff_s = max(sim_s) - min(sim_s)
        - 0보다 크면 (sim_s - min(sim_s)) / diff_s 를 통해 sim_s 스케일링 후 정렬
        - 0 이하인 경우는 dist값을 sim_s로 불러와서 정렬
      - sims_s_k_ : 대분류에 기반한 곡의 유사도를 계산 (플레이리스트, 태그, 토큰 정보를 전부 포함하여 계산)
      - sims_t_k_ : 소분류에 기반한 곡의 유사도를 계산 (플레이리스트, 태그, 토큰 정보를 전부 포함하여 계산)
      - sims_s_s_k_ : 대분류에 기반한 태그의 유사도를 계산 (플레이리스트 정보만 사용하여 계산)
      - sims_t_t_k_ : 소분류에 기반한 태그의 유사도를 계산 (태그, 토큰 정보만 사용하여 계산)
        - 계산하여 각각 상위 300개만 사용
      - rel_1 : train_spas_s에서 플레이리스트 관련 데이터만 추출 * sims_s_k_ + sims_s_s_k_ 
      - rel_t : train_spas_t에서 태그 관련 데이터만 추출 * sims_t_k_
      - rel_t_t : train_spas_t에서 태그 관련 데이터만 추출 * sims_t_t_k_
      - songs_list : (rel_1 / sims_k_1)에 argsort를 적용하여 추천 플레이리스트로 생성
      - tags_list : (rel_t / sims_t_k_ + rel_t_t / sims_t_t_k_)에 argsort를 적용하여 추천 태그 리스트로 생성
      - 질문 플레이리스트에 생성 시점 이후의 노래는 플레이리스트에 들어갈 수 없으므로 날짜 정보를 통해 필터링
      - 질문 플레이리스트의 id, 필터링 된 추천 플레이리스트, 태그 리스트를 DataFrame으로 통합

## 4. 의문점
  - like_dist 사용 이유?
