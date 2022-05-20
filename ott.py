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



TMDB_API_KEY = 'e6149bf41aaefec295f3595be639b5c7'

# result = pd.DataFrame()
# def make_csv():
#     global result
#     # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
#     for i in range(1):
#         request_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key=5908342b45ef31ecdbea2e9687fbbcd8&language=ko-KR"
#         movies = requests.get(request_url).json()
#         # print(movies)
#         datafield = pd.DataFrame(movies['genres'])
#         # print(datafield)
#         datafield_preprocessed = datafield[
#             ['id', 'name']]
#     # print(datafield_preprocessed)
#         # result = datafield_preprocessed
        
#         result = pd.concat([result, datafield_preprocessed], ignore_index=True)
#     result.to_csv('genre.csv', encoding="utf-8-sig") 

# make_csv()





# # ott 정보받기
data = pd.read_csv("out1.csv", usecols=[0])
selectdata = pd.DataFrame(data, columns=['id'])

df_dict = data.to_dict()

dic_val = df_dict['id'].values()
dic_list = list(dic_val)



# '''
total_data = {}
for i in dic_list[0:3000]:

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
    
        # # print(kr_movie)
        # rent_list = kr_movie.get('rent')
        # flatrate_list = kr_movie.get('flatrate')
        # if rent_list:
        #     for rent in rent_list:
        #         total_data[i] = rent['provider_name']
        # if flatrate_list:
        #     for flatrate in flatrate_list:
        #         total_data[i] = flatrate['provider_name']
# print(total_data)
with open('./test.csv', 'w', encoding='UTF-8') as f:
    w = csv.writer(f)
    w.writerow(total_data.keys())
    w.writerow(total_data.values())
# json_val = json.dumps(total_data)
# print(json_val)
# '''
# total_data = {}
# for i in dic_list:

#     request_url = f"https://api.themoviedb.org/3/movie/{i}?api_key={TMDB_API_KEY}&language=en-US"
#     movies = requests.get(request_url).json()
#     if movies.get('runtime'):
#         total_data[i] = movies['runtime']
# print(total_data)





