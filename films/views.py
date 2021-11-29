from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Film, Director, Category, Country
from django.views.generic import CreateView, ListView

# Create your views here.
class Homepage(ListView):
    queryset = Film.objects.all().order_by('-added_date')
    context_object_name = 'videos'
    template_name = 'homepage.html'


class FilmCreateView(CreateView):
    model = Film
    fields = '__all__'
    success_url = reverse_lazy('homepage')
    template_name = 'film/create.html'


class DirectorCreateView(CreateView):
    model = Director
    fields = '__all__'
    success_url = reverse_lazy('homepage')
    template_name = 'director/create.html'
