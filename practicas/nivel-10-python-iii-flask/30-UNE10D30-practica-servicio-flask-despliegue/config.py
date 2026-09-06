import os


def url_base_datos():
    url = os.environ.get("DATABASE_URL", "sqlite:///solicitudes.db")
    return url.replace("postgres://", "postgresql+psycopg://", 1) if url.startswith("postgres://") else url


class BaseConfig:
    SECRET_KEY = os.environ.get("SECRET_KEY", "desarrollo-cambiar")
    SQLALCHEMY_DATABASE_URI = url_base_datos()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = 1_048_576
    JSON_SORT_KEYS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True
    SECRET_KEY = "clave-pruebas"
    SQLALCHEMY_DATABASE_URI = "sqlite://"


class ProductionConfig(BaseConfig):
    DEBUG = False
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"


CONFIGURACIONES = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
