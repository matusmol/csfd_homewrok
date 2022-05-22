from django.db import models

from movies.models import Movie


class Actor(models.Model):
    full_name = models.CharField(max_length=200)
    search_full_name = models.CharField(max_length=200)
    link = models.CharField(max_length=400)


class ActorsMovie(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
