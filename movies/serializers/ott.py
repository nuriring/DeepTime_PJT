from rest_framework import serializers
from ..models import Ott
from ..models import Movie

class OttSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ott
        fields = ('movie_id', 'provider_name')

class MovieOttSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path')