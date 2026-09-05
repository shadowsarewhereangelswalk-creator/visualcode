import unicodedata


def normalizar_nombre(nombre):
    return " ".join(nombre.strip().split()).title()


def crear_codigo(nombre, numero):
    texto = unicodedata.normalize("NFKD", normalizar_nombre(nombre))
    texto = "".join(caracter for caracter in texto if not unicodedata.combining(caracter))
    iniciales = "".join(parte[0] for parte in texto.split()).upper()
    return f"{iniciales}-{numero:04d}"


def moneda(valor, simbolo="USD"):
    return f"{simbolo} {valor:,.2f}"
