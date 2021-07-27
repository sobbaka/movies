from django.urls import path
from .views import MovieList, MovieDetail, AddReview

urlpatterns = [

    path('', MovieList.as_view(),),
    path('<slug:slug>/', MovieDetail.as_view(), name='movie_detail'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review')
]