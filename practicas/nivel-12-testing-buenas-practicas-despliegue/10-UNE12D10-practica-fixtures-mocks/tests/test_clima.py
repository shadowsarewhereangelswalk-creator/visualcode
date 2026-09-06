import pytest
from clima import obtener_recomendacion


@pytest.mark.parametrize(
    ("temperatura", "esperada"),
    [(32, "Usa ropa fresca"), (20, "Clima templado"), (12, "Lleva abrigo")],
)
def test_recomendaciones(cliente_clima, temperatura, esperada):
    cliente_clima.consultar.return_value = {"temperatura": temperatura}
    resultado = obtener_recomendacion("Caracas", cliente_clima)
    assert resultado["recomendacion"] == esperada
    cliente_clima.consultar.assert_called_once_with("Caracas")


def test_limite_personalizado(cliente_clima):
    cliente_clima.consultar.return_value = {"temperatura": 25}
    resultado = obtener_recomendacion("Mérida", cliente_clima, limite=24)
    assert resultado["recomendacion"] == "Usa ropa fresca"
