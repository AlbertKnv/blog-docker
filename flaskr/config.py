import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ['SECRET_KEY']
    MODE = os.environ['MODE']


class DevelopmentConfig(Config):
    
    ENV = 'development'
    DEBUG = True


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    pass
