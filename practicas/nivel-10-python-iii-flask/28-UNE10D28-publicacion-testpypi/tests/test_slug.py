from ai_career_slug import crear_slug


def test_crear_slug():
    assert crear_slug("Inteligencia Artificial") == "inteligencia-artificial"
    assert crear_slug("  API & Flask  ") == "api-flask"
    assert crear_slug("Diseño y Validación") == "diseno-y-validacion"


def test_texto_vacio():
    assert crear_slug("") == ""
