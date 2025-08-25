import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from movies.forms import MovieSearchForm
from movies.models import FavoriteMovie

OMDB_API_URL = "http://www.omdbapi.com/"

@login_required
def search_movies(request):
    query = request.GET.get("q", "")
    movies = []

    if query:
        api_key = settings.OMDB_API_KEY
        url = f"http://www.omdbapi.com/?apikey={api_key}&s={query}"

        response = requests.get(url)
        data = response.json()

        if data.get("Response") == "True":
            movies = data.get("Search", [])

    context = {
        "query": query,
        "movies": movies,
    }
    return render(request, "movies/movie-search.html", context)

@login_required
def movie_search_view(request):
    form = MovieSearchForm(request.GET or None)
    movies = []

    if form.is_valid():
        query = form.cleaned_data['query']
        movies = search_movies(query)

    return render(request, 'movies/movie-search.html', {
        'search_form': form,
        'movies': movies
    })

@login_required
def movie_detail_view(request, imdb_id):
    api_key = settings.OMDB_API_KEY
    url = f"{OMDB_API_URL}?apikey={api_key}&i={imdb_id}&plot=full"

    response = requests.get(url)
    movie = response.json()

    return render(request, 'movies/movie-details.html', {'movie': movie})

@login_required
def add_favorite_movies(request, imdb_id):


    url = f"http://www.omdbapi.com/?apikey={settings.OMDB_API_KEY}&i={imdb_id}"

    response = requests.get(url)
    data = response.json()

    if data.get('Response') == 'True':
        FavoriteMovie.objects.get_or_create(
            user=request.user,
            imdb_id=imdb_id,
            year=data.get('Year'),
            defaults={
                "title": data.get('Title'),
                'poster_url': data.get('Poster') if data.get('Poster') != 'N/A' else '',
            }
        )

    return redirect('favorites')

@login_required
def remove_favorite_movies(request, imdb_id):
    if request.method == 'POST':
        FavoriteMovie.objects.filter(user=request.user, imdb_id=imdb_id).delete()

    return redirect('favorites')

@login_required
def favorites_list(request):
    favorites = FavoriteMovie.objects.filter(user=request.user)
    return render(request, 'movies/favorites-list.html', {'favorites': favorites})