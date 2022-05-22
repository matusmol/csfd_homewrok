from django.shortcuts import render
from actors.models import Actor
from movies.models import Movie
from django.db.models.functions import Lower

def FindView(request):
    response = {}
    if request.method == 'POST':
        search_key = request.POST["search_key"]
        movies = Movie.objects.filter(search_name__icontains=search_key).order_by(Lower('search_name'))
        actors = Actor.objects.filter(search_full_name__icontains=search_key).order_by(Lower('search_full_name'))

        response.update({"movies": movies})
        response.update({"actors": actors})
        response.update({"search_key": search_key})
    return render(request, 'base.html', response)