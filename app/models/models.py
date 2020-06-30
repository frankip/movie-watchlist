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
        