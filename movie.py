# 최종 코드

import requests
import json
import csv
import pandas as pd

# f = open('C:/Users/82102/Desktop/movie/movie_data_a.csv', encoding='cp949')
data = pd.read_csv("movie_data_a.csv", encoding='cp949', usecols=[0])
# selectdata = pd.DataFrame(data, columns=['pk'])
a = []
# print(type(data))
df_dict = data.to_dict()
dic_val = df_dict['pk'].values()
dic_list = list(dic_val)
# print(dic_list)
# TMDB_API_KEY = ''

# def get_movie_datas():
#     total_data = []

#     # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
#     for i in range(1, 801):
#         request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
#         movies = requests.get(request_url).json()

#         for movie in movies['results']:
#             if movie.get('release_date', ''):
#                 fields = {
#                     'movie_id': movie['id'],
#                     'title': movie['title'],
#                     'released_date': movie['release_date'],
#                     'popularity': movie['popularity'],
#                     'vote_avg': movie['vote_average'],
#                     'overview': movie['overview'],
#                     'poster_path': movie['poster_path'],
#                     'genres': movie['genre_ids']
#                 }

#                 data = {
#                     "pk": movie['id'],
#                     "model": "movies.movie",
#                     "fields": fields
#                 }

#                 total_data.append(data)

#     with open("movie_data.json", "w", encoding="utf-8") as w:
#         json.dump(total_data, w, ensure_ascii=False)

# get_movie_datas()

TMDB_API_KEY = 'e6149bf41aaefec295f3595be639b5c7'

def get_movie_datas():
    total_data = []

    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    for i in dic_list[0:11]:
        request_url = f"https://api.themoviedb.org/3/movie/{i}/watch/providers?api_key={TMDB_API_KEY}"
        movies = requests.get(request_url).json()

        movie = movies["results"]
        if movie.get('flatrate', ''):
            kr_movie = movie["KR"]
        if movie.get('flatrate', ''):
            ott_movie = kr_movie["flatrate"]
            print(ott_movie)
            for ott in ott_movie: 
                fields = {
                    'provider_id': ott['provider_id'],
                    'logo_path': ott['logo_path'],
                    'provider_name': ott['provider_name']

                }

                data = {
                    "pk": i,
                    "model": "movies.movie",
                    "fields": fields
                }

                total_data.append(data)

    with open("ott_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, ensure_ascii=False)

get_movie_datas()