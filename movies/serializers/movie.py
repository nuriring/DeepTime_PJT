from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Article, Comment, Genre, Movie

User = get_user_model()

#영화 상세 정보 조회 #예고편이랑 ott_provider는 api요청이라 시리얼라이저 없음
class MovieSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username') #영화 좋아요에 유저정보 필요
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('id', 'name') #영화 장르 정보 필요
    
    user = UserSerializer(read_only=True) #유효성 검사시 문제없도록
    genres = GenreSerializer(read_only=True, many=True) #무비 상세정보에 장르 필요
    
    # queryset annotate (views에서 채워줄것!)
    # 영화 좋아요수
    like_users = serializers.IntegerField()
    
    class Meta:
        model = Movie
        fields = ('__all__')


#영화 리스트 조회
class MovieSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username') #영화 좋아요에 유저정보 필요
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('id', 'name') #영화 장르 정보 필요
    
    user = UserSerializer(read_only=True) #유효성 검사시 문제없도록
    genres = GenreSerializer(read_only=True, many=True) #무비 상세정보에 장르 필요
    
    # queryset annotate (views에서 채워줄것!)
    # 영화 좋아요수
    like_users = serializers.IntegerField()
    
    class Meta:
        model = Movie
        fields = ('id','title','vote_average','release_date','poster_path','popularity','genres','like_users') #보여주진 않아도 필터링에 필요한 정보는 입력해 놓았습니다

