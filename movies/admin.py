from django.contrib import admin
from .models import Movie, Ott, Review
# Register your models here.

admin.site.register(Movie)
admin.site.register(Ott)
admin.site.register(Review)
