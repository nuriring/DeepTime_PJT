from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Article, Comment

User = get_user_model()

#댓글 생성 및 조회 
class CommentSerializer(serializers.ModelSerializer): #게시글 디테일과 게시글 목록처럼 필드를 공유할 수 없는경우 시리얼라이저를 나눠주는거임 댓글은 그럴필요가 없지?
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'user', 'content', 'article', 'created_at') #article 필드가 있어야 어느 게시글에 달린 건지 알 수 있다
        read_only_fields = ('article',) #포린키를 시리얼라이저 만들 때 사용할 수 있도록 리드 온리로 유효성 검사에서 빈값으로 인식하지 않도록 따로 정보를 미리 빼두는 격
        #이렇게 쓸수 있는 이유는 해당 field의 all에 article이 포함되어 있기 때문이다

   