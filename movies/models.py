from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=200)
    search_name = models.CharField(max_length=200)
    link = models.CharField(max_length=400)
