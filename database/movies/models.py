from django.db import models
from django.conf import settings
# Create your models here.
class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    backdrop_path = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='movies')
    overview = models.TextField()
    popularity = models.FloatField() #인기도
    release_date = models.DateField()
    vote_average = models.FloatField() #평점
    poster_path = models.TextField()
    title = models.CharField(max_length=50)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

class Ott(models.Model):
    id = models.IntegerField(primary_key=True)
    movie_id = models.IntegerField()
    provider_name = models.CharField(max_length=50)

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField (auto_now=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
 