class Config:
    """
    General configuration parent class
    """
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'

class ProdConfig(Config):
    """
    Production configuration child classes.
    """
    pass
class DevConfig(Config):
    """
    Development configuration child classes
    Args:
        Config:The parent configuration class with general configuration class.
    """
    DEBUG=True