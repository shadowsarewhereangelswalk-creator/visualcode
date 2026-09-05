import os

from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from config import CONFIGURACIONES


def create_app(entorno=None):
    nombre_entorno = entorno or os.environ.get("FLASK_ENV", "production")
    aplicacion = Flask(__name__)
    aplicacion.config.from_object(CONFIGURACIONES.get(nombre_entorno, CONFIGURACIONES["production"]))
    if nombre_entorno == "production" and aplicacion.config["SECRET_KEY"] == "desarrollo-cambiar":
        raise RuntimeError("Define SECRET_KEY para producción")
    aplicacion.wsgi_app = ProxyFix(aplicacion.wsgi_app, x_for=1, x_proto=1, x_host=1)
    from .routes import principal
    aplicacion.register_blueprint(principal)
    return aplicacion
