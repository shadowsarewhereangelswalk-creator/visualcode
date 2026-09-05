import re
import unicodedata


def limpiar_espacios(texto):
    return " ".join(texto.strip().split())


def normalizar_nombre(nombre):
    return limpiar_espacios(nombre).title()


def crear_identificador(texto):
    normalizado = unicodedata.normalize("NFKD", limpiar_espacios(texto))
    sin_acentos = "".join(caracter for caracter in normalizado if not unicodedata.combining(caracter))
    return re.sub(r"[^a-z0-9]+", "-", sin_acentos.lower()).strip("-")


def crear_mensaje(nombre, servicio, precio):
    cliente = normalizar_nombre(nombre)
    servicio_limpio = limpiar_espacios(servicio).capitalize()
    codigo = crear_identificador(f"{cliente}-{servicio_limpio}")
    return (
        f"Hola, {cliente}. Tu cotización para {servicio_limpio} "
        f"es de ${precio:,.2f}. Código: {codigo.upper()}."
    )


if __name__ == "__main__":
    print(crear_mensaje("  karen   ramírez ", " automatización   con PYTHON ", 850))
