class Confifg:
    """
    common confugurations
    """
    MOVIE_API_KEY = '<Your Api Key>'
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'


class DevelopmentConfig(Confifg):
    """
    common confugurations
    """

    DEBUG = True


class ProductionConfig(Confifg):
    """
    Production config
    """
    pass
