import environment
import pytest


def test_informacion_entorno(monkeypatch):
    monkeypatch.setenv("APP_ENV", "testing")
    datos = environment.informacion_entorno()
    assert datos["modo"] == "testing"
    assert datos["python"]


def test_validar_version(monkeypatch):
    monkeypatch.setattr(environment.sys, "version_info", (3, 12, 0))
    assert environment.validar_version() is True


def test_version_insuficiente():
    with pytest.raises(RuntimeError, match="Python 99.0"):
        environment.validar_version((99, 0))
