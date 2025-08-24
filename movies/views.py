import requests
from django.conf import settings
from django.shortcuts import render
from movies.forms import MovieSearchForm


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
