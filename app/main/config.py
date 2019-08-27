import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT')
    SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
    FROM_MAIL = os.getenv('FROM_MAIL')
    DEBUG = False
    # Path for images folder
    # TODO: Remove this when integrating DO Spaces API
    IMGDIR = os.path.join(os.path.expanduser("~"), "ambit-images")
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SUPERUSER_NAME = os.getenv('SUPERUSER_NAME', "admin")


class DevelopmentConfig(Config):
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 3000
    # database URI goes here
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    HOST = '127.0.0.1'
    PORT = 3000
    # database URI goes here
    SQLALCHEMY_DATABASE_URI = 'sqlite://:memory'
    PRESERVE_CONTEXT_ON_EXCEPTION = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    DEBUG = False
    HOST = '0.0.0.0'
    PORT = '443'
    PRESERVE_CONTEXT_ON_EXCEPTION = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
