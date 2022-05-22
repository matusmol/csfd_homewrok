from django.db.models.functions import Lower
from django.shortcuts import render

from .models import Actor, ActorsMovie


def InfoView(request, actor_id):
    response = {}
    actor = Actor.objects.get(id=actor_id)
    movies = ActorsMovie.objects.filter(actor=actor)

    response.update({"movies": movies.order_by(Lower('movie__search_name'))})
    response.update({"full_name": actor.full_name})
    return render(request, 'info_actor.html', response)
