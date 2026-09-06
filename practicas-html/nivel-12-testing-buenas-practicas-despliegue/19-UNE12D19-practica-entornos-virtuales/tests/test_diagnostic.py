import importlib.metadata

from src import diagnostic


def test_paquete_instalado(monkeypatch):
    monkeypatch.setattr(importlib.metadata, "version", lambda paquete: "1.2.3")
    monkeypatch.setattr(diagnostic.sys, "prefix", "/entorno")
    monkeypatch.setattr(diagnostic.sys, "base_prefix", "/sistema")
    resultado = diagnostic.diagnosticar(["pytest"])
    assert resultado["listo"] is True
    assert resultado["instalados"] == {"pytest": "1.2.3"}


def test_paquete_faltante(monkeypatch):
    def no_encontrado(paquete):
        raise importlib.metadata.PackageNotFoundError(paquete)

    monkeypatch.setattr(importlib.metadata, "version", no_encontrado)
    resultado = diagnostic.diagnosticar(["paquete"])
    assert resultado["faltantes"] == ["paquete"]
    assert resultado["listo"] is False
