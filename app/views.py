from flask import render_template
from app import app 

from .request import get_movies

# views
@app.route('/')
def index():
    """
    view root page that returns index page
    """
    popular_movies = get_movies('popular')
    # print(popular_movies)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title=title,popular = popular_movies)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('movie.html',id = movie_id)