import os

_basedir = os.path.abspath(os.path.dirname(__file__))


# Creates the default Config Object
class Config(object):
    # APP Settings
    DEBUG = False
    TESTING = False

    SECRET_KEY = "testing_secret_key"

    # Database Config
    DB_PROTOCOL = "postgresql+psycopg2"
    DB_HOST = "localhost"
    DB_PORT = "5432"
    DB_USER = "lmnop"
    DB_PASSWORD = os.getenv("LMNOP_DB_PW")
    DB_NAME = "lmnop"
    DB_TEMPLATE = '{protocol}://{user}:{pw}@{host}:{port}/{db}'

    DB_CONN = DB_TEMPLATE.format(
        protocol=DB_PROTOCOL,
        user=DB_USER,
        pw=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        db=DB_NAME
    )


# Overrides the default Config Object for Production
class ProductionConfig(Config):
    DB_HOST = "change to production value"


# Overrides the default Config Object for Development
class DevelopmentConfig(Config):
    DEBUG = True


# Overrides the default Config Object for Testing
class TestingConfig(Config):
    TESTING = True

    # database configuration
    DB_NAME = "lmnop_test"


del os
