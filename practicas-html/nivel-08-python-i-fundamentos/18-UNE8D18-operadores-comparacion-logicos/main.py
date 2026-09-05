def evaluar_solicitud(edad, experiencia, presupuesto, acepta_terminos, pais):
    edad_valida = 18 <= edad <= 75
    experiencia_valida = experiencia >= 1
    presupuesto_valido = presupuesto >= 500
    ubicacion_valida = pais.lower() in {"españa", "méxico", "colombia", "venezuela"}
    datos_validos = edad_valida and presupuesto_valido and acepta_terminos
    elegible = datos_validos and (experiencia_valida or presupuesto >= 1500) and ubicacion_valida

    razones = []
    if not edad_valida:
        razones.append("edad fuera del rango permitido")
    if not presupuesto_valido:
        razones.append("presupuesto insuficiente")
    if not acepta_terminos:
        razones.append("términos no aceptados")
    if not experiencia_valida and presupuesto < 1500:
        razones.append("falta experiencia o presupuesto ampliado")
    if not ubicacion_valida:
        razones.append("país fuera de cobertura")

    return {
        "elegible": elegible,
        "razones": razones,
        "datos_validos": datos_validos,
        "requiere_revision": datos_validos and not elegible,
    }


def main():
    solicitudes = [
        ("Ana", 31, 3, 900, True, "Colombia"),
        ("Luis", 19, 0, 1800, True, "México"),
        ("Marta", 17, 2, 1200, True, "España"),
        ("Diego", 40, 0, 600, False, "Venezuela"),
    ]

    for nombre, edad, experiencia, presupuesto, acepta, pais in solicitudes:
        resultado = evaluar_solicitud(edad, experiencia, presupuesto, acepta, pais)
        estado = "Aprobada" if resultado["elegible"] else "Rechazada"
        detalle = ", ".join(resultado["razones"]) or "cumple todos los requisitos"
        print(f"{nombre}: {estado} · {detalle}")


if __name__ == "__main__":
    main()
