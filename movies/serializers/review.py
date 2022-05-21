from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Movie, Review


User = get_user_model()



#리뷰 상세 조회
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


    class Meta:
        model = Review
        fields = ('id','user','movie','title','content','created_at') 



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


    class Meta:
        model = Review
        fields = ('id','user','movie','title','content',)
