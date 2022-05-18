# 최종 코드

import requests
import json
import csv
import pandas as pd
from pprint import pprint
# import os
# import getpass

# username = getpass.getuser() #컴퓨터 사용자 이름 가져오기
# from pathlib import Path  
# filepath = Path('folder/subfolder/out.csv')  
# filepath.parent.mkdir(parents=True, exist_ok=True)  


# f = open('C:/Users/82102/Desktop/movie/movie_data_a.csv', encoding='cp949')
data = pd.read_csv("out.csv", usecols=[3])
selectdata = pd.DataFrame(data, columns=['id'])
print(selectdata)
# # print(type(data))
df_dict = data.to_dict()
dic_val = df_dict['id'].values()
dic_list = list(dic_val)
print(dic_list)
TMDB_API_KEY = 'e6149bf41aaefec295f3595be639b5c7'

# def get_movie_datas():
total_data = {}

    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
def make_csv():
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
    result.to_csv('out.csv', encoding="utf-8-sig") 



    # print(result)

# get_movie_datas()

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
#                     # 'genres': movie['genre_ids']
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

# TMDB_API_KEY = ''
# print(dic_list[0:10])
# def get_movie_datas():
#     total_data = []

#     # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
for i in dic_list:

    request_url = f"https://api.themoviedb.org/3/movie/{i}/watch/providers?api_key={TMDB_API_KEY}"
    movies = requests.get(request_url).json()
    if movies.get('results'):
        movie = movies['results']
    if movie.get('KR'):
        kr_movie = movie['KR']
        # print(kr_movie)
        rent_list = kr_movie.get('rent')
        flatrate_list = kr_movie.get('flatrate')
        if rent_list:
            for rent in rent_list:
                total_data[i] = rent['provider_name']
        if flatrate_list:
            for flatrate in flatrate_list:
                total_data[i] = flatrate['provider_name']
print(total_data)

#         movie = movies['results']
#         print(movie)
#         kr_movie = movie['KR']
#         print(kr_movie)
#         ott_movie = kr_movie['flatrate']
#         print(ott_movie)
#         for ott in ott_movie: 
#             fields = {
#                 'provider_id': ott['provider_id'],
#                 'logo_path': ott['logo_path'],
#                 'provider_name': ott['provider_name']

#             }

#             data = {
#                 "pk": i,
#                 "model": "movies.movie",
#                 "fields": fields
#             }

#             total_data.append(data)

#     with open("ott_data.json", "w", encoding="utf-8") as w:
#         json.dump(total_data, w, ensure_ascii=False)

# get_movie_datas()