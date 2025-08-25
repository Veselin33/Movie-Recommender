from django.urls import path

from movies import views

urlpatterns = [
    path('search/', views.search_movies, name='search'),

    path('detail/<str:imdb_id>/', views.movie_detail_view, name='detail'),
    path('favorites/<str:imdb_id>/', views.add_favorite_movies, name='add_favorite'),

    path('favorites/', views.favorites_list, name='favorites'),

    path('remove-favorite/<str:imdb_id>/', views.remove_favorite_movies, name='remove_favorite')


]