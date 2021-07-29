from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import DetailView, ListView

from .models import Movie, Actor, Genre, Rating
from .forms import ReviewForm, RatingForm


# Create your views here.

class GenreYear:
    """Жанры и года"""
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=True).values_list('year', flat=True).distinct('year')



class MovieList(GenreYear, ListView):
    """All movies list"""
    model = Movie
    template_name = 'movies/movie_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MovieDetail(GenreYear, DetailView):
    model = Movie
    template_name = 'movies/moviesingle.html'
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['star_form'] = RatingForm()
        return context


class ActorDetail(DetailView):
    model = Actor
    template_name = "movies/actor.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AddReview(View):
    """Отзывы"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)  # stop saving form
            form.movie = movie
            form.save()
        return redirect("/movies/")

class FilterMovieView(GenreYear, ListView):
    """Фильтр фильмов"""
    template_name = 'movies/movie_list.html'
    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre"))
        ).distinct('name')
        return queryset

class AddRating(View):
    """Добавление рейтинга к фильму"""
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        print(x_forwarded_for)
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
            print('1 - ', ip)
        else:
            ip = request.META.get("REMOTE_ADDR")
            print('2 - ', ip)
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                movie_id=int(request.POST.get('movie')),
                defaults={'star_id': int(request.POST.get('star'))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)