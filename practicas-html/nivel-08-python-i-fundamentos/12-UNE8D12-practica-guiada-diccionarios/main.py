def registrar_cliente(clientes, codigo, nombre, correo, servicios=None):
    codigo = codigo.upper()
    if codigo in clientes:
        raise ValueError("El cliente ya existe")
    clientes[codigo] = {
        "nombre": nombre.strip().title(),
        "correo": correo.strip().lower(),
        "activo": True,
        "servicios": list(servicios or []),
    }


def contratar_servicio(clientes, codigo, servicio):
    cliente = clientes.get(codigo.upper())
    if cliente is None:
        raise KeyError("Cliente no encontrado")
    if servicio not in cliente["servicios"]:
        cliente["servicios"].append(servicio)


def cambiar_estado(clientes, codigo, activo):
    cliente = clientes.get(codigo.upper())
    if cliente is None:
        raise KeyError("Cliente no encontrado")
    cliente["activo"] = bool(activo)


def buscar_activos(clientes):
    return {
        codigo: datos
        for codigo, datos in clientes.items()
        if datos["activo"]
    }


def main():
    clientes = {}
    registrar_cliente(clientes, "cli-001", "ana torres", "ANA@EJEMPLO.COM", ["Landing page"])
    registrar_cliente(clientes, "cli-002", "luis pérez", "luis@ejemplo.com")
    contratar_servicio(clientes, "cli-002", "Automatización")
    cambiar_estado(clientes, "cli-001", False)

    for codigo, datos in buscar_activos(clientes).items():
        servicios = ", ".join(datos["servicios"]) or "Sin servicios"
        print(f'{codigo}: {datos["nombre"]} · {datos["correo"]} · {servicios}')


if __name__ == "__main__":
    main()
