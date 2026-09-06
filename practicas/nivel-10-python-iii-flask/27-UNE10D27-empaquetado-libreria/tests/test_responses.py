from career_service_kit import crear_error, crear_respuesta, pagina_valida


def test_pagina_valida():
    assert pagina_valida(1, 25)
    assert not pagina_valida(0, 25)
    assert not pagina_valida(1, 101)


def test_crear_respuesta():
    resultado = crear_respuesta(["a", "b"], total=8, pagina=2, por_pagina=2)
    assert resultado["datos"] == ["a", "b"]
    assert resultado["meta"]["total_paginas"] == 4


def test_crear_error():
    resultado = crear_error("no_encontrado", "No existe", {"id": 99})
    assert resultado["error"]["codigo"] == "no_encontrado"
    assert resultado["error"]["detalles"] == {"id": 99}
