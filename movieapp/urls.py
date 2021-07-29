from django.urls import path
from .views import MovieList, MovieDetail, AddReview, ActorDetail

urlpatterns = [

    path('', MovieList.as_view(),),
    path('actors/<int:pk>/', ActorDetail.as_view(), name='actor_detail'),
    path('<slug:slug>/', MovieDetail.as_view(), name='movie_detail'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review')
]