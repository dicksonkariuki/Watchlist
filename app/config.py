class Config:
    """
    General configuration parent class
    """
    pass
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