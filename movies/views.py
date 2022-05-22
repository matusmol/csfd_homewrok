from django.shortcuts import render

from actors.models import ActorsMovie
from movies.models import Movie
from django.db.models.functions import Lower



def InfoView(request, movie_id):
    response = {}
    movie = Movie.objects.get(id=movie_id)
    actors = ActorsMovie.objects.filter(movie=movie)
    response.update({"actors": actors.order_by(Lower('actor__search_full_name'))})
    response.update({"movie": movie.name})
    return render(request, 'info_movie.html', response)
