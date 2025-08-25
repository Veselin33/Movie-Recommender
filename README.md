# Movie-Recommender
Practice Django app to search and explore movies via the OMDb API — learning, building, and improving my skills.

More features coming soon - Favorites, details & recommendations.


## Features

-User authentication: register, login, and logout.

-Search movies by title using the OMDb API.

-Display detailed information for each movie (title, year, genre, director, actors, plot, poster).

-Add or remove movies from personal favorites.

-Responsive favorites list displayed in a clean grid with posters.

-Admin panel to manage users and movie data.

## Tech Stack

-Python 3.12

-Django 5.2.5

-HTML, CSS (with FontAwesome icons)

-OMDb API for movie data

-PostgreSQL

### Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/Veselin33/Movie-Recommender.git
   ```
    cd Movie-Recommender
2. Create a virtual environment
    python -m venv .venv

    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate

3. pip install -r requirements.txt
4. Apply Migrations
    puthon manage.py migrate
5. Run server
    - python manage.py runserver
6. Open Browser at 
    http://127.0.0.1:8000/
