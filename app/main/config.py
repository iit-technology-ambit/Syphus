import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT')
    SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
    FROM_MAIL = os.getenv('FROM_MAIL')
    DEBUG = False
    # Path for images folder
    IMGDIR = os.path.join(os.path.expanduser("~"), "ambit-images")


class DevelopmentConfig(Config):
    DEBUG = True
    # database URI goes here
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://USERNAME:PASSWORD@localhost/DBNAME'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    # database URI goes here
    SQLALCHEMY_DATABASE_URI = 'sqlite://:memory'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
