from django.urls import path
from .views import MovieList, MovieDetail, AddReview, ActorDetail, FilterMovieView, AddRating, MovieSearch

urlpatterns = [
    path('', MovieList.as_view(),),
    path('add-rating/', AddRating.as_view(), name='add_rating'),
    path('search/', MovieSearch.as_view(), name='movie_search'),
    path('filter/', FilterMovieView.as_view(), name='movie_filter'),
    path('actors/<int:pk>/', ActorDetail.as_view(), name='actor_detail'),
    path('<slug:slug>/', MovieDetail.as_view(), name='movie_detail'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review')
]