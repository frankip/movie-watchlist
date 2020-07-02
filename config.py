import os

class Confifg:
    """
    common confugurations
    """
    MOVIE_API_KEY = '91c09537ef238ac29bc0f1d2989ec7f9'
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    SECRET_KEY = '12345abcd'

    # os.environ.get()



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

config_options = {
    'development':DevelopmentConfig,
    'production':ProductionConfig
}
