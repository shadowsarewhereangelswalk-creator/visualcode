import pytest

from deployment_app import create_app
from deployment_app.quality import REQUIRED_CHECKS


def test_default_config():
    app = create_app()
    assert app.config["APP_NAME"] == "Deployment Control"


@pytest.fixture
def client():
    app = create_app(
        {
            "TESTING": True,
            "APP_NAME": "Aplicación de prueba",
            "APP_ENV": "testing",
            "APP_VERSION": "2.1.0",
            "RELEASE_SHA": "abc123",
        }
    )
    return app.test_client()


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Aplicación de prueba".encode() in response.data
    assert response.headers["X-Frame-Options"] == "DENY"


def test_health_and_ready(client):
    assert client.get("/health").get_json() == {"status": "ok"}
    assert client.get("/ready").get_json() == {"status": "ready"}


def test_status_api(client):
    data = client.get("/api/status").get_json()
    assert data["environment"] == "testing"
    assert data["version"] == "2.1.0"
    assert data["release"] == "abc123"
    assert data["uptime_seconds"] >= 0


def test_checks_api_approved(client):
    response = client.post(
        "/api/checks",
        json=dict.fromkeys(REQUIRED_CHECKS, True),
    )
    assert response.status_code == 200
    assert response.get_json()["ready"] is True


def test_checks_api_rejected(client):
    response = client.post("/api/checks", json={"tests": True})
    assert response.status_code == 422
    assert "container" in response.get_json()["failed"]
