import os

from flask import Flask, jsonify, render_template


def create_app(config=None):
    application = Flask(__name__)
    application.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY", "development-key"),
        APP_ENV=os.environ.get("APP_ENV", "development"),
        APP_VERSION=os.environ.get("APP_VERSION", "1.0.0"),
    )
    if config:
        application.config.update(config)

    @application.get("/")
    def index():
        return render_template(
            "index.html",
            entorno=application.config["APP_ENV"],
            version=application.config["APP_VERSION"],
        )

    @application.get("/health")
    def health():
        return jsonify(
            status="ok",
            environment=application.config["APP_ENV"],
            version=application.config["APP_VERSION"],
        )

    return application
