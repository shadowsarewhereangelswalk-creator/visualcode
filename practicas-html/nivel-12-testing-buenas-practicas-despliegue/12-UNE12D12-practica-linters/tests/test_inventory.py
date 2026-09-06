import pytest

from src.inventory import consolidar_movimientos, productos_disponibles


def test_consolidar_movimientos():
    movimientos = [
        {"producto": "A", "cantidad": 4},
        {"producto": "A", "cantidad": -1},
        {"producto": "B", "cantidad": 2},
    ]
    assert consolidar_movimientos(movimientos) == {"A": 3, "B": 2}


def test_existencia_negativa():
    with pytest.raises(ValueError, match="negativa"):
        consolidar_movimientos([{"producto": "A", "cantidad": -1}])


def test_productos_disponibles():
    assert productos_disponibles({"A": 1, "B": 0}) == ["A"]
