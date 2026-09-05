from flask import Flask


def create_app(configuracion=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="desarrollo-local",
        JSON_SORT_KEYS=False,
    )
    if configuracion:
        app.config.from_mapping(configuracion)

    from .routes import principal

    app.register_blueprint(principal)
    return app
