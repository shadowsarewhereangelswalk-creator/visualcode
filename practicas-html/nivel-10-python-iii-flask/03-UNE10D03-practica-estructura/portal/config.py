import os


class ConfiguracionBase:
    SECRET_KEY = os.getenv("SECRET_KEY", "clave-local")
    JSON_SORT_KEYS = False


class Desarrollo(ConfiguracionBase):
    DEBUG = True


class Pruebas(ConfiguracionBase):
    TESTING = True


class Produccion(ConfiguracionBase):
    DEBUG = False


CONFIGURACIONES = {
    "desarrollo": Desarrollo,
    "pruebas": Pruebas,
    "produccion": Produccion,
}
