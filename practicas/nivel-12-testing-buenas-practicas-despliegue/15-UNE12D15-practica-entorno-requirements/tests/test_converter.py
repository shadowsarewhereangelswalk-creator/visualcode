from decimal import Decimal

import pytest

from src.converter import convertir


def test_convertir_usd_eur():
    assert convertir(100, "usd", "eur") == Decimal("92.00")


def test_misma_moneda():
    assert convertir("12.5", "USD", "USD") == Decimal("12.50")


def test_conversion_no_disponible():
    with pytest.raises(ValueError, match="disponible"):
        convertir(10, "EUR", "VES")
