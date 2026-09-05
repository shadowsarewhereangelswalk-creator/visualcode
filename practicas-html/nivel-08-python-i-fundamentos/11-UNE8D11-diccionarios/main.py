catalogo = {
    "WEB01": {"nombre": "Landing page", "precio": 420.0, "duracion": 5},
    "IA02": {"nombre": "Asistente virtual", "precio": 980.0, "duracion": 12},
    "AUT03": {"nombre": "Automatización", "precio": 740.0, "duracion": 8},
}


def consultar_servicio(codigo):
    servicio = catalogo.get(codigo.upper())
    if servicio is None:
        raise KeyError("Servicio no encontrado")
    return {"codigo": codigo.upper(), **servicio}


def actualizar_precio(codigo, nuevo_precio):
    servicio = consultar_servicio(codigo)
    if nuevo_precio <= 0:
        raise ValueError("El precio debe ser positivo")
    catalogo[servicio["codigo"]]["precio"] = float(nuevo_precio)


def agrupar_por_duracion():
    grupos = {"corta": [], "media": [], "larga": []}
    for codigo, servicio in catalogo.items():
        if servicio["duracion"] <= 5:
            grupo = "corta"
        elif servicio["duracion"] <= 10:
            grupo = "media"
        else:
            grupo = "larga"
        grupos[grupo].append(codigo)
    return grupos


def main():
    actualizar_precio("web01", 450)
    for codigo in catalogo:
        servicio = consultar_servicio(codigo)
        print(f'{servicio["codigo"]}: {servicio["nombre"]} · {servicio["precio"]:.2f}')
    print("Duraciones:", agrupar_por_duracion())


if __name__ == "__main__":
    main()
