class Movie:
    """
    movie class to define movie objects

    """
    def __init__(self, id, title, overview, poster, vote_avarage, vote_count):
        self.id = id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.vote_avearage  = vote_avarage
        self.vote_count = vote_count
        



class Review:

    all_reviews = []

    def __init__(self, movie_id, title, imageurl, review):
        self.movie_id = movie_id
        self.title =  title
        self.image_url = imageurl
        self.review = review


    def save_review(self):
        Review.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls, id):
        
        response = []
        for review in cls.all_reviews:
            # print(review.__dict__)
            if review.movie_id == id:
                response.append(review)

        return response