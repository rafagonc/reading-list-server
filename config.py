

import os

class Config(object):
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = os.environ['HEROKU_POSTGRESQL_PUCE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True