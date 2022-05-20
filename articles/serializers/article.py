from rest_framework import serializers
from django.contrib.auth import get_user_model

from accounts.models import User
from ..models import Article
from .comment import CommentSerializer

User = get_user_model()



#게시글 상세 조회 및 생성
class ArticleSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model =  User
            fields = ('pk', 'username') #게시글 상세정보에서 작성자 이름 보여주기

    user = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)#게시글에 달린 댓글 보여주기
    
    #게시글을 좋아요한 유저 목록 보여줄거면 아래 주석 풀고 필드에 추가
    #like_users = UserSerializer(read_only=True, many=True)
    
    # queryset annotate (views에서 채워줄것!)
    #게시글 좋아요 수 보여주기
    like_count = serializers.IntegerField()
    #게시글에 달린 댓글 수 보여주기
    comment_count = serializers.IntegerField()


    class Meta:
        model = Article
        fields = ('pk', 'user', 'title', 'content', 'comments', 'like_count', 'comment_count' ) #게시글 상세정보에서 보여줄 필드
         

#게시글 리스트 조회
class ArticleListSerializer(serializers.ModelSerializer):
    class UserSerizlizer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk' 'username') #게시글 리스트에서 작성자 이름 보여주기

    user = UserSerizlizer(read_only=True) #게시글 작성자
    
    # queryset annotate (views에서 채워 줄것!)
    #게시글에 달린 댓글 수 보여주기
    comment_count = serializers.IntegerField()
    #게시글 좋아요 수 보여주기
    like_count = serializers.IntegerField()

    
    class Meta:
        model = Article
        fields = ('pk', 'user', 'title', 'content', 'created_at', 'comment_count', 'like_count') #게시글 리스트에서 보여줄 필드



