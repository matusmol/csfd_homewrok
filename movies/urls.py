from django.urls import path
from . import views

urlpatterns = [
    path(r'<int:movie_id>', views.InfoView, name = 'movie_info'),
]



