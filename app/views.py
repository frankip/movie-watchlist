from flask import render_template
from app import app 

from .request import get_movies, get_single_movie,  search_movie

# views
@app.route('/')
def index():
    """
    view root page that returns index page
    """
    popular_movies = get_movies('popular')
    # print(popular_movies)
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title=title,popular = popular_movies,  upcoming = upcoming_movie, now_showing = now_showing_movie)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_single_movie(movie_id)
    title = f'{movie.title}'

    return render_template('movie.html',title = title,movie = movie)


