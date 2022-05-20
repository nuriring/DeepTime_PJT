from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Movie, Review


User = get_user_model()

#리뷰 생성 및 상세 조회
class ReviewSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username')
    
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title')

    
    user = UserSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)
    # queryset annotate (views에서 채워줄것!)
    # 리뷰 좋아요 수 보여주기
    like_count = serializers.IntegerField()

    class Meta:
        model = Review
        fields = ('id','user','movie','title','content','created_at','like_count') 


#리뷰 리스트 조회
class ReviewListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username')
    
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title')

    
    user = UserSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)
    #like_users = UserSerializer(read_only=True, many=True)
    
    # queryset annotate (views에서 채워줄것!)
    # 리뷰 좋아요 수 보여주기
    like_count = serializers.IntegerField()

    class Meta:
        model = Review
        fields = ('id','user','movie','content','like_count') 
