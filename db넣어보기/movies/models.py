from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)


class OTT(models.Model):
    movie_id = models.IntegerField()
    provider_name = models.CharField(max_length=20)