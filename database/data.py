import requests
import pandas as pd
import os
import csv

# 장르 데이터 뽑아오기
TMDB_API_KEY = ''

result = pd.DataFrame()
def make_csv():
    global result
    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    for i in range(1):
        request_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=ko-KR"
        movies = requests.get(request_url).json()
        # print(movies)
        datafield = pd.DataFrame(movies['genres'])
        # print(datafield)
        datafield_preprocessed = datafield[
            ['id', 'name']]
    # print(datafield_preprocessed)
        # result = datafield_preprocessed
        
        result = pd.concat([result, datafield_preprocessed], ignore_index=True)
    result.to_csv('genre.csv', encoding="utf-8-sig") 

make_csv()

# 영화 데이터 뽑아오기
def make_csv():
    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    for i in range(1, 10):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()
        # print(movies)
        datafield = pd.DataFrame(movies['results'])
        # print(datafield)
        datafield_preprocessed = datafield[
            ['backdrop_path', 'genre_ids', 'id', 'overview', 'popularity', 'release_date', 'vote_average', 'poster_path', 'title']]
    # print(datafield_preprocessed)
        result = datafield_preprocessed
        result = pd.concat([result, datafield_preprocessed], ignore_index=True)
    result.to_csv('movie.csv', encoding="utf-8-sig") 

make_csv()




# 영화 장르 중개테이블 데이터 뽑아오기
windows_user_name = os.path.expanduser('~')
start_page = 1
end_page = 500 #페이지 수
for page in range(start_page, end_page+1):
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko&region=kr&page={page}'
    data = requests.get(url).json()

    df = pd.DataFrame(data['results'])
    df_preprocessed = df[
        ['genre_ids', 'id']]

    result = pd.concat([result, df_preprocessed], ignore_index=True)
    print(page)


df = pd.DataFrame()

# result.rename(columns={'id':'movie_id'})

id = 0
for i in range(0, len(result)):
    for genre in result.iat[i,0]:
        df = df.append({'movie_id':int(result.iat[i,1]), 'genre_id':int(genre)} , ignore_index=True)
        id += 1

print(df)




df.to_csv(f'{windows_user_name}/Desktop/movie_genre.csv', encoding="utf-8-sig")





# OTT 데이터 구축

data = pd.read_csv("out1.csv", usecols=[0])
selectdata = pd.DataFrame(data, columns=['id'])

df_dict = data.to_dict()

dic_val = df_dict['id'].values()
dic_list = list(dic_val)
# print(dic_list)


total_data = {}
for i in dic_list:

    request_url = f"https://api.themoviedb.org/3/movie/{i}/watch/providers?api_key={TMDB_API_KEY}"
    movies = requests.get(request_url).json()
    if movies.get('results'):
        movie = movies['results']
        if movie.get('KR'):
            kr_movie = movie['KR']
            if kr_movie.get('flatrate'):
                flatrate_list = kr_movie.get('flatrate')
                for flatrate in flatrate_list:
                    total_data[i] = flatrate['provider_name']
            else:
                continue
        else:
            continue
    else:
        continue
    
with open('./test2.csv', 'w', encoding='UTF-8') as f:
    w = csv.writer(f)
    w.writerow(total_data.keys())
    w.writerow(total_data.values())
