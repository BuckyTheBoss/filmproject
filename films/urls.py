from django.urls import path
from .views import FilmCreateView, DirectorCreateView, Homepage

urlpatterns = [
    path('film/create/', FilmCreateView.as_view(), name='new_film'),
    path('director/create/', DirectorCreateView.as_view(), name='new_director'),
    path('homepage/', Homepage.as_view(), name='homepage'),
]