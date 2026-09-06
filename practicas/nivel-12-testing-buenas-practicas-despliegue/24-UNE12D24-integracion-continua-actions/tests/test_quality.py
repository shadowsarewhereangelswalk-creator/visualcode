import pytest

from quality import crear_slug, normalizar_nombre


def test_normalizar_nombre():
    assert normalizar_nombre("  karen   agostini ") == "Karen Agostini"


def test_crear_slug():
    assert crear_slug("Integración Continua") == "integración-continua"


def test_nombre_invalido():
    with pytest.raises(ValueError):
        normalizar_nombre("x")
