import re


PATRON_CORREO = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")


def correo_valido(valor):
    return bool(PATRON_CORREO.fullmatch(str(valor).strip().lower()))


def texto_requerido(valor, minimo=1, maximo=255):
    texto = str(valor).strip()
    return texto if minimo <= len(texto) <= maximo else ""
