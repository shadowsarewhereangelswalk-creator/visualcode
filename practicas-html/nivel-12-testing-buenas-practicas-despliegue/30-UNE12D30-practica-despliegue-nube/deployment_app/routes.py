import time

from flask import Blueprint, current_app, jsonify, render_template, request

from .quality import evaluate_checks

web = Blueprint("web", __name__)


def service_status():
    return {
        "name": current_app.config["APP_NAME"],
        "environment": current_app.config["APP_ENV"],
        "version": current_app.config["APP_VERSION"],
        "release": current_app.config["RELEASE_SHA"],
        "uptime_seconds": round(time.time() - current_app.config["STARTED_AT"], 3),
    }


@web.get("/")
def index():
    return render_template("index.html", status=service_status())


@web.get("/health")
def health():
    return jsonify(status="ok")


@web.get("/ready")
def ready():
    environment = current_app.config["APP_ENV"]
    status = 200 if environment in {"development", "testing", "production"} else 503
    return jsonify(status="ready" if status == 200 else "not-ready"), status


@web.get("/api/status")
def api_status():
    return jsonify(service_status())


@web.post("/api/checks")
def api_checks():
    data = request.get_json(silent=True) or {}
    result = evaluate_checks(data)
    return jsonify(result), 200 if result["ready"] else 422
