from asyncore import read
from rest_framework import serializers
from django.contrib.auth import get_user_model
from articles.models import Article
from articles.serializers.comment import CommentSerializer
from movies.models import Genre
from dj_rest_auth.registration.serializers import RegisterSerializer
User = get_user_model()

#회원가입 시 유저 관련 정보


class CustomRegisterSerializer(RegisterSerializer):

    genre = serializers.IntegerField()

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['genre'] = self.validated_data.get('genre', '')

        return data

#유저관련 프로필 정보
class ProfileSerializer(serializers.ModelSerializer):
    #1
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('id', 'title', 'content') #게시글 에서 보여줄 필드 : id, 제목, 내용 

    #2
    class GenreSerializer(serializers.ModelSerializer): #프로필에서 유저가 좋아하는 장르 보여주기
        class Meta:
            model = Genre
            fields = ('id', 'name')

    #1
    like_articles = ArticleSerializer(many=True) #유저가 좋아요한 게시글
    articles = ArticleSerializer(many=True) #유저가 작성한 게시글
    comments = CommentSerializer(many=True, read_only=True) #유저가 작성한 댓글
    
    #2
    genre = GenreSerializer(read_only=True)

    class Meta:
        model = User

        fields = ('id', 'username', 'like_articles', 'articles', 'genre', 'comments') #유저가 좋아하는 장르도 보여주고 싶은데 이렇게 될라나 모르겠넹


    
