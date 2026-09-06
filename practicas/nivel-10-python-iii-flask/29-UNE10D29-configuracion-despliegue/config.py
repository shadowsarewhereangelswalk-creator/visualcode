import os


class BaseConfig:
    SECRET_KEY = os.environ.get("SECRET_KEY", "desarrollo-cambiar")
    JSON_SORT_KEYS = False
    MAX_CONTENT_LENGTH = 1_048_576


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    PREFERRED_URL_SCHEME = "https"
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"


CONFIGURACIONES = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
