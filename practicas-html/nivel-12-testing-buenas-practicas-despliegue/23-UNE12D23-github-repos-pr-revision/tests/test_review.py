from review import validar_pull_request


def test_pull_request_aprobable():
    resultado = validar_pull_request(
        {
            "titulo": "Agrega suite completa",
            "descripcion": "Incluye casos válidos, inválidos y límites.",
            "pruebas_aprobadas": True,
            "revisor": "revisor",
            "autor": "Karen",
            "rama_base": "main",
        }
    )
    assert resultado["aprobable"] is True
    assert resultado["resumen"] == "Karen → main"


def test_pull_request_incompleto():
    resultado = validar_pull_request(
        {
            "titulo": "Cambio",
            "descripcion": "Breve",
            "pruebas_aprobadas": False,
            "revisor": "",
        }
    )
    assert resultado["errores"] == ["titulo", "descripcion", "pruebas", "revisor"]
