import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    pass
    # MODE = 'prod'
    # DEBUG = False
    # TESTING = False
    SECRET_KEY = 'this-really-needs-to-be-changed'
    # # DATABASE_URI = 'sqlite:///:memory:'
    # DATABASE = ''

class DevelopmentConfig(Config):
    MODE = 'dev'
    ENV = 'development'
    DEBUG = True
    # DATABASE = 'sqlite:///' + os.path.join(basedir, 'app.db')
    # DATABASE = os.path.join(basedir, 'flask.sqlite')

class ProductionConfig(Config):
    pass
    # DATABASE_URI = 'mysql://user@localhost/foo'

class TestingConfig(Config):
    TESTING = True