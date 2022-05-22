from django.urls import path
from . import views

urlpatterns = [
    path(r'<int:actor_id>', views.InfoView, name = 'actor_info'),
]



