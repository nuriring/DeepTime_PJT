from rest_framework import serializers
from django.contrib.auth import get_user_model

from accounts.models import User
from ..models import Article, Category
from .comment import CommentSerializer

User = get_user_model()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name',)

#게시글 상세 조회 및 생성
class ArticleSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model =  User
            fields = ('id', 'username') #게시글 생성시 유저 정보 필요

    
    user = UserSerializer(read_only=True) #유효성 검사 시 문제없도록
    comments = CommentSerializer(many=True, read_only=True)#게시글에 달린 댓글 보여주기
    like_users = UserSerializer(read_only=True, many=True)




    class Meta:
        model = Article

        fields = ('id', 'user', 'title', 'content', 'category', 'comments', 'created_at', 'like_users' ) #게시글 상세정보에서 보여줄 필드
        read_only_fields = ('category',)

#게시글 리스트 조회
class ArticleListSerializer(serializers.ModelSerializer):
    class UserSerizlizer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id','username') #게시글 리스트에서 작성자 이름 보여주기


    class CategorySerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = ('id', 'name') #게시글 리스트에서 카테고리 이용해서 분류하기

    user = UserSerizlizer(read_only=True) #유효성 검사 시 문제없도록
    category = CategorySerializer(read_only=True) 
    
    # queryset annotate (views에서 채워 줄것!)
    #게시글에 달린 댓글 수 보여주기
    comment_count = serializers.IntegerField()
    #게시글 좋아요 수 보여주기
    like_count = serializers.IntegerField()

    
    class Meta:
        model = Article
        fields = ('id', 'user', 'title', 'content', 'category', 'created_at', 'comment_count', 'like_count') #게시글 리스트에서 보여줄 필드



