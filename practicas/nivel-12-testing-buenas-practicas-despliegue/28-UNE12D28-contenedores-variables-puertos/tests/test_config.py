import pytest
from app import create_app
from config import cargar_configuracion


def test_variables_de_entorno(monkeypatch):
    monkeypatch.setenv("APP_ENV", "production")
    monkeypatch.setenv("APP_MESSAGE", "Contenedor activo")
    monkeypatch.setenv("PORT", "9000")
    configuracion = cargar_configuracion()
    assert configuracion == {
        "entorno": "production",
        "mensaje": "Contenedor activo",
        "puerto": 9000,
    }


def test_puerto_invalido(monkeypatch):
    monkeypatch.setenv("PORT", "70000")
    with pytest.raises(ValueError):
        cargar_configuracion()


def test_endpoint(monkeypatch):
    monkeypatch.setenv("APP_ENV", "testing")
    respuesta = create_app().test_client().get("/")
    assert respuesta.get_json()["entorno"] == "testing"
