from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import DetailView, ListView

from .models import Movie, Category, Actor
from .forms import ReviewForm


# Create your views here.

class MovieList(ListView):
    """All movies list"""
    model = Movie
    template_name = 'movies/movie_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MovieDetail(DetailView):
    model = Movie
    template_name = 'movies/moviesingle.html'
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ActorDetail(DetailView):
    model = Actor
    template_name = "movies/actor.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AddReview(View):
    """Отзывы"""

    def post(self, requst, pk):
        form = ReviewForm(requst.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)  # stop saving form
            form.movie = movie
            form.save()
        return redirect("/movies/")
