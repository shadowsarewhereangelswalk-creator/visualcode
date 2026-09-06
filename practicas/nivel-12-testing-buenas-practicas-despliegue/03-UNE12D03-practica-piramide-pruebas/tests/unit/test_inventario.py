import pytest
from src.orders import Inventario


def test_reserva_reduce_existencias():
    inventario = Inventario({"monitor": 4})
    assert inventario.reservar("monitor", 2) == 2


def test_reserva_rechaza_exceso():
    with pytest.raises(ValueError):
        Inventario({"monitor": 1}).reservar("monitor", 2)
