from django.urls import path

from movies import views

urlpatterns = [
    path('search/', views.search_movies, name='search'),
]