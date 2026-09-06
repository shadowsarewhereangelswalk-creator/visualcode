import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from werkzeug.middleware.proxy_fix import ProxyFix

from config import CONFIGURACIONES


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
migrate = Migrate()


def create_app(entorno=None, configuracion=None):
    nombre_entorno = entorno or os.environ.get("FLASK_ENV", "production")
    aplicacion = Flask(__name__)
    aplicacion.config.from_object(CONFIGURACIONES.get(nombre_entorno, CONFIGURACIONES["production"]))
    if configuracion:
        aplicacion.config.update(configuracion)
    if nombre_entorno == "production" and aplicacion.config["SECRET_KEY"] == "desarrollo-cambiar":
        raise RuntimeError("Define SECRET_KEY para producción")
    if nombre_entorno == "production":
        aplicacion.wsgi_app = ProxyFix(aplicacion.wsgi_app, x_for=1, x_proto=1, x_host=1)
    db.init_app(aplicacion)
    migrate.init_app(aplicacion, db)
    from . import models
    from .routes import api, principal
    aplicacion.register_blueprint(principal)
    aplicacion.register_blueprint(api, url_prefix="/api")
    return aplicacion
