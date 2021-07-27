from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic.detail import DetailView

from .models import Movie
from .forms import ReviewForm
# Create your views here.

class MovieList(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movies/movies.html', {'movie_list': movies})

class MovieDetail(DetailView):

    model = Movie
    template_name = 'movies/moviesingle.html'
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AddReview(View):
    """Отзывы"""
    def post(self, requst, pk):
        form = ReviewForm(requst.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False) # stop saving form
            form.movie = movie
            form.save()
        return redirect("/movies/")