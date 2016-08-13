import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:

    MARSHMALLOW_STRICT = True
    MARSHMALLOW_DATEFORMAT = 'rfc'
    SECRET_KEY = 'test_key'
    SECURITY_LOGIN_SALT = 'test'
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_TRACKABLE = True
    SECURITY_PASSWORD_SALT = 'something_super_secret_change_in_production'
    WTF_CSRF_ENABLED = False
    SECURITY_LOGIN_URL = '/test/v1/login/'
    SECURITY_LOGOUT_URL = '/test/v1/logout/'
    # SECURITY_POST_LOGIN_VIEW = '/test/v1/admin/'
    SECURITY_POST_RESET_VIEW = '/test/v1/reset/'
    SECURITY_POST_CONFIRM_VIEW = '/#/home/Account-Confirmed'

    SECURITY_RESET_URL = '/test/v1/reset-password/'
    SECURITY_RESET_PASSWORD_TEMPLATE = 'reset.html'
    SECURITY_REGISTERABLE = True
    SECURITY_CONFIRMABLE = True
    SECURITY_RECOVERABLE = True

    AUTH_HEADER_NAME = 'authentication-token'
    MAX_AGE = 86400

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_DEBUG = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    MAIL_DEFAULT_SENDER = ''
    MAIL_MAX_EMAILS = 100
    MAIL_SUPPRESS_SEND = True
    REDIS_URL = "redis://:@localhost:6379/0"
    RATELIMIT_STORAGE_URL = 'redis://'
    RATELIMIT_STRATEGY = 'fixed-window-elastic-expiry'

    @staticmethod
    def init_app(app):
        pass


class DevConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    HOST = 'mongodb://localhost:27017/test'
    MONGODB_DB = 'pos-api'
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27017


class TestConfig(BaseConfig):
    TESTING = True
    DEBUG = True
    MONGOALCHEMY_DATABASE = 'test'


class ProdConfig(BaseConfig):
    MONGOALCHEMY_DATABASE = 'test'


configs = {
    'dev': DevConfig,
    'testing': TestConfig,
    'prod': ProdConfig,
    'default': DevConfig
}
