from flask import Flask

from .config import CONFIGURACIONES


def create_app(entorno="produccion"):
    app = Flask(__name__)
    app.config.from_object(CONFIGURACIONES[entorno])

    from .views import web

    app.register_blueprint(web)
    return app
