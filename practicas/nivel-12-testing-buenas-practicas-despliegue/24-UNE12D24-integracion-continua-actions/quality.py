def normalizar_nombre(valor):
    nombre = " ".join(valor.strip().split())
    if len(nombre) < 3:
        raise ValueError("Nombre no válido")
    return nombre.title()


def crear_slug(valor):
    return "-".join(normalizar_nombre(valor).lower().split())
