import os
import time

from flask import Flask

from .routes import web


def create_app(config=None):
    application = Flask(__name__)
    application.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY", "development-key"),
        APP_NAME=os.environ.get("APP_NAME", "Deployment Control"),
        APP_ENV=os.environ.get("APP_ENV", "development"),
        APP_VERSION=os.environ.get("APP_VERSION", "1.0.0"),
        RELEASE_SHA=os.environ.get("RELEASE_SHA", "local"),
        STARTED_AT=time.time(),
    )
    if config:
        application.config.update(config)
    application.register_blueprint(web)

    @application.after_request
    def security_headers(response):
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        return response

    return application
