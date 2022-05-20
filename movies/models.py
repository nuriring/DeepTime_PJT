from django.db import models
from django.conf import settings
# Create your models here.
class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    backdrop_path = models.TextField()
    genre = models.ManyToManyField(Genre, related_name='movie_genre')
    overview = models.TextField()
    popularity = models.FloatField()
    release_date = models.DateField()
    vote_average = models.FloatField()
    poster_path = models.TextField()
    title = models.CharField(max_length=50)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

class OTT(models.Model):
    id = models.IntegerField(primary_key=True)
    movie_id = models.IntegerField()
    provider_name = models.CharField(max_length=50)