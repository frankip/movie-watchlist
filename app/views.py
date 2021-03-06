from flask import render_template,request,redirect,url_for
from app import app 

from .request import get_movies, get_single_movie,  search_movie

from .models.reviews import Review
from .form import ReviewForm

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

    search_movie = request.args.get('movie_query')

    if search_movie:
        return redirect(url_for('search',movie_name=search_movie))
    else:
        return render_template('index.html', title=title,popular = popular_movies,  upcoming = upcoming_movie, now_showing = now_showing_movie)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_single_movie(movie_id)
    title = f'{movie.title}'

    reviews = Review.get_reviews(movie.id)

    print('------', reviews)

    return render_template('movie.html',title = title,movie = movie, reviews = reviews)


@app.route('/search/<movie_name>')
def search(movie_name):
    '''
    View function to display the search results
    '''
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    # print('serached', searched_movies)
    title = f'search results for {movie_name}'
    if searched_movies:
        return redirect(url_for('search',movie_name=search_movie))
    else:
        return '<h3> There is is no movie found</h3>'


@app.route('/movie/review/new/<int:movie_id>', methods=['GET', 'POST'])
def new_review(movie_id):
    form = ReviewForm()
    movie = get_single_movie(movie_id)

    if form.validate_on_submit():
        title =  form.title.data
        review = form.review.data
        new_review = Review(movie.id, title, movie.poster, review)
        # print(dir(new_review))
        new_review.save_review()
        return redirect(url_for('movie', movie_id = movie.id ))
        
    title = f'{movie.title} review'
    return render_template('new_review.html',title = title, review_form=form, movie=movie)